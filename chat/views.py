import json
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from .models import ChatMessage
from .ai import get_guessed_word
from .vocabulary import VOCABULARY

def game_view(request, lang_code='japanese'):
    if lang_code not in VOCABULARY:
        raise Http404("Language not found")

    context = VOCABULARY[lang_code]
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
