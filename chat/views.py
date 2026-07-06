import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from .models import ChatMessage
from .ai import get_guessed_word
from .vocabulary import VOCABULARY

CATEGORY_EMOJIS = {
    "Alimentation": "🍽️",
    "Corps & Objets": "👤",
    "Expressions & Pensée": "💭",
    "Verbes d'action": "⚡",
    "Social & Famille": "👨\u200d👩\u200d👧",
    "Pronoms & Lieux": "📍",
    "Maison & Ville": "🏠",
    "Temps": "⏰",
    "Temps (suite) & État": "🌤️",
    "Adjectifs": "✨",
    "Adjectifs & Divers": "🎨",
    "Chiffres & Quantité": "🔢",
    "Politesse": "🤝",
    "Divers": "📝",
}


def game_view(request, lang_code='japanese'):
    if lang_code not in VOCABULARY:
        raise Http404("Language not found")

    lang_data = VOCABULARY[lang_code]
    categories = lang_data['categories']

    # Sort by number of words descending, then pair largest with smallest
    # so each column has one tall and one short category
    sorted_cats = sorted(
        [dict(cat) for cat in categories],
        key=lambda c: len(c['words']), reverse=True
    )
    for i, cat in enumerate(sorted_cats):
        cat['color_class'] = f'cat-color-{i % 14}'
        cat['emoji'] = CATEGORY_EMOJIS.get(cat['name'], '📚')

    columns = []
    left, right = 0, len(sorted_cats) - 1
    while left <= right:
        if left == right:
            columns.append([sorted_cats[left]])
        else:
            columns.append([sorted_cats[left], sorted_cats[right]])
        left += 1
        right -= 1

    context = {
        'display_name': lang_data['display_name'],
        'categories': categories,
        'category_columns': columns,
    }
    return render(request, 'chat/game.html', context)

def index_view(request):
    languages = []
    for code, data in VOCABULARY.items():
        languages.append({
            'code': code,
            'display_name': data['display_name'],
            'word_count': sum(len(cat['words']) for cat in data['categories'])
        })
    return render(request, 'chat/index.html', {'languages': languages})

# TODO : this shouldn’t be static
history: list[str] = []

def reset_history(request):
    if request.method == 'POST':
        history.clear()
        ChatMessage.objects.all().delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

def messages(request):
    if request.method == 'GET':
        msgs = ChatMessage.objects.all().order_by('timestamp')
        return JsonResponse({
            'messages': [
                {
                    'sender': m.sender,
                    'message': m.message,
                    'timestamp': m.timestamp.isoformat()
                } for m in msgs
            ]
        })
    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            sender = data.get('sender', 'Anonymous')
            if len(sender) > 100:
                sender = sender[:97] + "..."

            message_text = data.get('message', '')
            language = data.get('language', 'japanese (romaji)')

            msg = ChatMessage.objects.create(
                sender=sender,
                message=message_text
            )
            # Log the message to the console for debugging
            print(f"New message from {sender}: {message_text} (Language: {language})")

            # AI Reply Logic
            if not sender.startswith("AI_Bot"):
                print(f"Current chat history: {history}")
                ai_guess = get_guessed_word(message_text, chat_history=history, language=language)
                print(f"AI guess: {ai_guess}")
                if not ai_guess.is_understood:
                    ChatMessage.objects.create(
                        sender="AI_Bot",
                        message=f"""
                        I'm sorry, I couldn't understand your message.
                        Are you trying to say: {ai_guess.understood_message}?
                        Translation: {ai_guess.understood_message_translation}."""
                    )
                else: 
                    ChatMessage.objects.create(
                        sender="AI_Bot",
                        message=f"""
                        I understood your message as: {ai_guess.understood_message}.
                        Translation: {ai_guess.understood_message_translation}.
                    My guess for the word you are thinking of is: {ai_guess.guessed_word}.
                    Translation: {ai_guess.translation}.
                    """
                    )
                    history.append(message_text)
                    history.append(f"My guess: {ai_guess.guessed_word}")
            else:
                print("Message from AI_Bot, no reply generated.")

            return JsonResponse({
                'status': 'success',
                'message': {
                    'sender': msg.sender,
                    'message': msg.message,
                    'timestamp': msg.timestamp.isoformat()
                }
            }, status=201)
        except (json.JSONDecodeError, KeyError):
            return JsonResponse({'error': 'Invalid data'}, status=400)

    return JsonResponse({'error': 'Invalid method'}, status=405)
