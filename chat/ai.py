import dspy
import os
from dotenv import load_dotenv
import pydantic
from pathlib import Path
from chat.models import Language

class LanguageGuessSignature(dspy.Signature):
    """Guesser for the language of a message. Based on the chat message, guess the language(s) of the message."""
    chat_message = dspy.InputField(desc="The message sent by the player describing a word.")
    guessed_language: list[Language] = dspy.OutputField(desc="The language(s) of this message. If there are multiple languages, return them all. If you don't know, return an empty list.")

class Reply(pydantic.BaseModel):
    """A simple reply model that takes a message and returns a reply."""
    understood_message: str = pydantic.Field(description="The chat message as you understood it, in the language you understand, without any lexical or grammatical errors.")
    understood_message_translation: str = pydantic.Field(description="A translation of the understood message in the player's original language.")
    guessed_word: str = pydantic.Field(description="A single word guess, in your language, that you think the player is thinking of. It won't be a word that is inside the sentence, but an object the sentence is talking about.")
    translation: str = pydantic.Field(description="A translation of the guessed word in the player's original language.")

class WordGuessSignature(dspy.Signature):
    """Guesser for a word game. Based on the chat message, guess the word the player is thinking of."""
    target_language: Language = dspy.InputField(desc="The guesser's language: the only language you understands.")
    original_language: Language = dspy.InputField(desc="The player's original language. All translation fields in the reply must be in this language.")
    chat_history: list[str] = dspy.InputField(desc="The chat history, made of messages that were understood and your previous replies, and are meant to make us guess the same word.", default=[])
    chat_message = dspy.InputField(desc="The message sent by the player describing a word. Assumed to be in the language you understand.")
    reply: Reply = dspy.OutputField(desc="A reply to the player, including whether you understood the message, your understanding of the message, a guessed word, and translations.")

class WordGuesser(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predictor = dspy.Predict(WordGuessSignature)

    def forward(self, chat_message, target_language, original_language, chat_history):
        if chat_history is None:
            chat_history = []
        return self.predictor(
            chat_message=chat_message,
            target_language=target_language,
            original_language=original_language,
            chat_history=chat_history,
        )

class WrongLanguageReply(pydantic.BaseModel):
    """Raised when the guessed language is not the target language."""
    actual_language: Language

class ErrorReply(pydantic.BaseModel):
    """Raised when an error occurs during the guessing process."""
    error_message: str

def get_guessed_word(
    message: str,
    chat_history: list[str],
    target_language: Language,
    original_language: Language,
) -> Reply | WrongLanguageReply | ErrorReply:
    """
    Initializes dspy and returns a guessed word based on the chat message.
    """
    if isinstance(target_language, str):
        try:
            target_language = Language(target_language)
        except ValueError:
            return ErrorReply(error_message=f"Unsupported target language: {target_language}")

    if isinstance(original_language, str):
        try:
            original_language = Language(original_language)
        except ValueError:
            return ErrorReply(error_message=f"Unsupported original language: {original_language}")

    # Load .env from project root explicitly.
    env_path = Path(__file__).resolve().parent.parent / ".env"
    load_dotenv(dotenv_path=env_path)
    
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    # Support both names for backward compatibility.
    model_name = os.environ.get("AI_MODEL") or os.environ.get("GEMINI_MODEL") or "gemini-3.5-flash"
    print(f"Using model: {model_name} with API key: {'set' if api_key else 'not set'}")

    if not api_key:
        return ErrorReply(error_message="I need an API key to guess!")

    if not dspy.settings.lm:
        # Use gemini/ provider prefix as requested
        lm = dspy.LM(model=f"gemini/{model_name}", api_key=api_key, max_tokens=8192)
        dspy.settings.configure(lm=lm)

    try:
        language_guesser = dspy.Predict(LanguageGuessSignature)
        language_prediction = language_guesser(chat_message=message)

        guessed_languages = language_prediction.guessed_language or []
        if not isinstance(guessed_languages, list):
            guessed_languages = [guessed_languages]

        if target_language not in guessed_languages:
            return WrongLanguageReply(
                actual_language=guessed_languages[0] if guessed_languages else target_language
            )

        else:
            guesser = WordGuesser()
            prediction = guesser(
                chat_message=message,
                original_language=original_language,
                target_language=target_language,
                chat_history=chat_history,
            )
            return prediction.reply
    except Exception as e:
        return ErrorReply(error_message=f"Error: {str(e)}")
