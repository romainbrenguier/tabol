import json
import re
import unicodedata
from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from django.templatetags.static import static
from requests.packages import target
from .models import ChatMessage, Language
from .ai import get_guessed_word, WrongLanguageReply, ErrorReply
from .vocabulary import VOCABULARY, get_language_data, get_guess_words

CATEGORY_EMOJIS = {
    "Alimentation": "🍽️",
    "Corps & Objets": "👤",
    "Expressions & Pensée": "💭",
    "Verbes d'action": "⚡",
    "Verbes de mouvement": "🚶",
    "Social & Famille": "👨\u200d👩\u200d👧",
    "Pronoms & Lieux": "📍",
    "Pronoms": "🗣️",
    "Lieux": "🧭",
    "Maison & Ville": "🏠",
    "Temps": "⏰",
    "État": "🌤️",
    "Temps (suite) & État": "🌤️",
    "Temps & État": "🌤️",
    "Adjectifs": "✨",
    "Adjectifs d'état": "🙂",
    "Adjectifs de description": "✨",
    "Couleurs & Taille": "🎨",
    "Adjectifs & Divers": "🎨",
    "Chiffres & Quantité": "🔢",
    "Politesse": "🤝",
    "Divers": "📝",
    "Modaux & Phrases": "🛠️",
    "Interrogations": "❓",
    "Connecteurs": "🔗",
}

LANGUAGE_FLAGS = {
    'japanese': '🇯🇵',
    'german': '🇩🇪',
    'dutch': '🇳🇱',
    'turkish': '🇹🇷',
    'spanish': '🇪🇸',
    'italian': '🇮🇹',
}


def game_view(request, lang_code='japanese'):
    if lang_code not in VOCABULARY:
        raise Http404("Language not found")

    if request.GET.get('new_game') == '1':
        history.clear()
        ChatMessage.objects.all().delete()

    target_language = _coerce_language(lang_code)
    original_language = _coerce_language(request.GET.get('original_language'))
    if target_language is None or original_language is None:
        return redirect('index')

    difficulty = request.GET.get('difficulty', 'normal').lower()
    if difficulty not in ('easy', 'normal', 'hard'):
        difficulty = 'normal'

    lang_data = get_language_data(lang_code)
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

    sprite_filename_by_language = {
        'japanese': 'Japanese.png',
        'german': 'German.png',
        'dutch': 'Dutch.jfif',
        'turkish': 'Turkish.jfif',
        'spanish': 'Spanish.jfif',
        'italian': 'Italian.png',
    }
    sprite_filename = sprite_filename_by_language.get(lang_code, 'Japanese.png')

    context = {
        'lang_code': lang_code,
        'display_name': lang_data['display_name'],
        'target_language': target_language.value,
        'original_language': original_language.value,
        'categories': categories,
        'category_columns': columns,
        'difficulty': difficulty,
        'game_words': get_guess_words(
            categories,
            difficulty=difficulty,
            original_language=original_language.value,
        ),
        'chat_sprite_url': static(f'chat/img/{sprite_filename}'),
    }
    return render(request, 'chat/game.html', context)

def index_view(request):
    languages = []
    for code, data in VOCABULARY.items():
        vocabulary_data = get_language_data(code)
        word_count = sum(len(cat['words']) for cat in vocabulary_data['categories'])

        languages.append({
            'code': code,
            'display_name': data['display_name'],
            'flag': LANGUAGE_FLAGS.get(code, '🏳️'),
            'word_count': word_count,
        })
    return render(request, 'chat/index.html', {'languages': languages})

# TODO : this shouldn’t be static
history: list[str] = []


def _normalize_for_match(value: str) -> str:
    lowered = value.strip().lower()
    normalized = unicodedata.normalize('NFD', lowered)
    without_accents = ''.join(char for char in normalized if unicodedata.category(char) != 'Mn')
    alnum_spaces = re.sub(r'[^a-z0-9\s]', ' ', without_accents)
    squashed = re.sub(r'\s+', ' ', alnum_spaces).strip()
    return squashed


def _coerce_language(value) -> Language:
    if isinstance(value, Language):
        return value

    if isinstance(value, str):
        normalized = value.strip().lower()

        # Accept enum values (en, fr, ...) and common names used by the frontend.
        mapping = {
            'english': Language.ENGLISH,
            'en': Language.ENGLISH,
            'spanish': Language.SPANISH,
            'es': Language.SPANISH,
            'french': Language.FRENCH,
            'fr': Language.FRENCH,
            'german': Language.GERMAN,
            'de': Language.GERMAN,
            'italian': Language.ITALIAN,
            'it': Language.ITALIAN,
            'portuguese': Language.PORTUGUESE,
            'pt': Language.PORTUGUESE,
            'russian': Language.RUSSIAN,
            'ru': Language.RUSSIAN,
            'chinese': Language.CHINESE,
            'zh': Language.CHINESE,
            'japanese': Language.JAPANESE_ROMAJI,
            'ja': Language.JAPANESE_ROMAJI,
            'ja(ro)': Language.JAPANESE_ROMAJI,
            'korean': Language.KOREAN,
            'ko': Language.KOREAN,
            'dutch': Language.DUTCH,
            'nl': Language.DUTCH,
            'turkish': Language.TURKISH,
            'tr': Language.TURKISH,
        }

        if normalized in mapping:
            return mapping[normalized]

        try:
            return Language(normalized)
        except ValueError:
            return None

    return None

def reset_history(request):
    if request.method == 'POST':
        history.clear()
        ChatMessage.objects.all().delete()
        return JsonResponse({'status': 'success'})
    return JsonResponse({'error': 'Invalid method'}, status=405)

I_DONT_UNDERSTAND = {
    Language.ENGLISH: "I don't understand the language of your message. I guess you speak %s.",
    Language.SPANISH: "No entiendo el idioma de tu mensaje. Supongo que hablas %s.",
    Language.FRENCH: "Je ne comprends pas la langue de votre message. Je suppose que vous parlez %s.",
    Language.GERMAN: "Ich verstehe die Sprache deiner Nachricht nicht. Ich vermute, du sprichst %s.",
    Language.ITALIAN: "Non capisco la lingua del tuo messaggio. Suppongo che tu parli %s.",
    Language.PORTUGUESE: "Não entendo a língua da sua mensagem. Suponho que você fale %s.",
    Language.RUSSIAN: "Я не понимаю язык вашего сообщения. Я предполагаю, что вы говорите на %s.",
    Language.CHINESE: "我不懂你消息的语言。我猜你说的是%s。",
    Language.JAPANESE_ROMAJI: "nihongo no messeeji no gengo ga wakarimasen. anata wa %s o hanasu to omotte imasu.",
    Language.KOREAN: "메시지의 언어를 이해하지 못했습니다. 나는 당신이 %s를 말한다고 추측합니다.",
    Language.DUTCH: "Ik begrijp de taal van je bericht niet. Ik vermoed dat je %s spreekt.",
    Language.TURKISH: "Mesajınızın dilini anlamıyorum. Sanırım %s konuşuyorsunuz.",
}

THERE_WAS_AN_ERROR = {
    Language.ENGLISH: "There was an error while trying to guess the word.",
    Language.SPANISH: "Hubo un error al intentar adivinar la palabra.",
    Language.FRENCH: "Il y a eu une erreur lors de la tentative de deviner le mot.",
    Language.GERMAN: "Es gab einen Fehler beim Versuch, das Wort zu erraten.",
    Language.ITALIAN: "C'è stato un errore nel tentativo di indovinare la parola.",
    Language.PORTUGUESE: "Houve um erro ao tentar adivinhar a palavra.",
    Language.RUSSIAN: "Произошла ошибка при попытке угадать слово.",
    Language.CHINESE: "尝试猜测单词时出错。",
    Language.JAPANESE_ROMAJI: "kotoba o atemasu toki ni erā ga okimashita.",
    Language.KOREAN: "단어를 추측하려고 할 때 오류가 발생했습니다.",
    Language.DUTCH: "Er is een fout opgetreden bij het proberen het woord te raden.",
    Language.TURKISH: "Kelimeyi tahmin etmeye çalışırken bir hata oluştu.",
}

I_UNDERSTOOD_YOUR_MESSAGE = {
    Language.ENGLISH: "I understood your message as: %s.",
    Language.SPANISH: "Entendí tu mensaje como: %s.",
    Language.FRENCH: "J'ai compris votre message comme : %s.",
    Language.GERMAN: "Ich habe deine Nachricht verstanden als: %s.",
    Language.ITALIAN: "Ho capito il tuo messaggio come: %s.",
    Language.PORTUGUESE: "Entendi sua mensagem como: %s.",
    Language.RUSSIAN: "Я понял ваше сообщение как: %s.",
    Language.CHINESE: "我理解你的信息为：%s。",
    Language.JAPANESE_ROMAJI: "watashi wa anata no messeeji o %s to rikai shimashita.",
    Language.KOREAN: "나는 당신의 메시지를 다음과 같이 이해했습니다: %s.",
    Language.DUTCH: "Ik begreep je bericht als: %s.",
    Language.TURKISH: "Mesajınızı şu şekilde anladım: %s.",
}

MY_GUESS_IS = {
    Language.ENGLISH: "My guess for the word you are thinking of is: %s.",
    Language.SPANISH: "Mi suposición para la palabra en la que estás pensando es: %s.",
    Language.FRENCH: "Mon hypothèse pour le mot auquel vous pensez est : %s.",
    Language.GERMAN: "Mein Tipp für das Wort, an das du denkst, ist: %s.",
    Language.ITALIAN: "Il mio indovinello per la parola a cui stai pensando è: %s.",
    Language.PORTUGUESE: "Meu palpite para a palavra que você está pensando é: %s.",
    Language.RUSSIAN: "Моя догадка для слова, о котором вы думаете, это: %s.",
    Language.CHINESE: "我对你正在想的单词的猜测是：%s。",
    Language.JAPANESE_ROMAJI: "watashi no anata ga kangaete iru kotoba no suiri wa %s desu.",
    Language.KOREAN: "내가 생각하는 단어에 대한 내 추측은 다음과 같습니다: %s.",
    Language.DUTCH: "Mijn gok voor het woord waar je aan denkt is: %s.",
    Language.TURKISH: "Düşündüğünüz kelime için tahminim şudur: %s.",
}

WORD_FOUND = {
    Language.ENGLISH: "🎉 Word found. The referee confirms that the translation '%s' matches the word to guess.",
    Language.SPANISH: "🎉 Palabra encontrada. El árbitro confirma que la traducción '%s' coincide con la palabra a adivinar.",
    Language.FRENCH: "🎉 Mot trouvé. L'arbitre confirme que la traduction '%s' correspond au mot à deviner.",
    Language.GERMAN: "🎉 Wort gefunden. Der Schiedsrichter bestätigt, dass die Übersetzung '%s' mit dem zu erratenden Wort übereinstimmt.",
    Language.ITALIAN: "🎉 Parola trovata. L'arbitro conferma che la traduzione '%s' corrisponde alla parola da indovinare.",
    Language.PORTUGUESE: "🎉 Palavra encontrada. O árbitro confirma que a tradução '%s' corresponde à palavra a adivinhar.",
    Language.RUSSIAN: "🎉 Слово найдено. Судья подтверждает, что перевод '%s' соответствует слову для угадывания.",
    Language.CHINESE: "🎉 找到单词。裁判确认翻译“%s”与要猜的单词匹配。",
    Language.JAPANESE_ROMAJI: "🎉 kotoba ga mitsukarimashita. shinsai wa hon'yaku '%s' ga atemasu kotoba ni awatte iru koto o kakunin shimasu.",
    Language.KOREAN: "🎉 단어 찾기. 심판은 번역 '%s'가 추측할 단어와 일치함을 확인합니다.",
    Language.DUTCH: "🎉 Woord gevonden. De scheidsrechter bevestigt dat de vertaling '%s' overeenkomt met het te raden woord.",
    Language.TURKISH: "🎉 Kelime bulundu. Hakem, çevirinin '%s' tahmin edilecek kelimeyle eşleştiğini onaylıyor.",
}

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
            target_language = _coerce_language(data['target_language'])
            original_language = _coerce_language(data['original_language'])

            if target_language is None or original_language is None:
                return JsonResponse({'error': 'Invalid target_language or original_language'}, status=400)

            word_to_guess = data.get('word_to_guess', '')

            msg = ChatMessage.objects.create(
                sender=sender,
                message=message_text
            )
            # Log the message to the console for debugging
            print(f"New message from {sender}: {message_text} (Language: {target_language})")

            # AI Reply Logic
            if not sender.startswith("AI_Bot"):
                print(f"Current chat history: {history}")
                ai_guess = get_guessed_word(
                    message_text,
                    chat_history=history,
                    target_language=target_language,
                    original_language=original_language,
                )
                print(f"AI guess: {ai_guess}, target_language: {target_language}, original_language: {original_language}")
                if isinstance(ai_guess, WrongLanguageReply):
                    ChatMessage.objects.create(
                        sender="AI_Bot",
                        message=I_DONT_UNDERSTAND[target_language] % ai_guess.actual_language
                    )
                elif isinstance(ai_guess, ErrorReply):
                    ChatMessage.objects.create(
                        sender="AI_Bot",
                        message=THERE_WAS_AN_ERROR[target_language]
                    )
                else: 
                    normalized_translation = _normalize_for_match(ai_guess.translation)
                    normalized_word_to_guess = _normalize_for_match(word_to_guess)
                    is_winning_guess = (
                        bool(normalized_word_to_guess)
                        and normalized_translation == normalized_word_to_guess
                    )

                    ChatMessage.objects.create(
                        sender="AI_Bot",
                        message=f"""
                        {I_UNDERSTOOD_YOUR_MESSAGE[target_language] % ai_guess.understood_message}
                        ({ai_guess.understood_message_translation}).
                        {MY_GUESS_IS[target_language] % ai_guess.guessed_word}
                        ({ai_guess.translation}).
                    """
                    )

                    if is_winning_guess:
                        ChatMessage.objects.create(
                            sender="Arbitre",
                            message=WORD_FOUND[target_language] % ai_guess.translation
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
