import dspy
import os
from dotenv import load_dotenv
import pydantic

# Load environment variables from .env file
load_dotenv()

class Reply(pydantic.BaseModel):
    """A simple reply model that takes a message and returns a reply."""
    is_understood: bool = pydantic.Field(description="Whether the message is understandable in your language.")
    understood_message: str = pydantic.Field(description="The chat message as you understood it, in the language you understand, without any lexical or grammatical errors.")
    understood_message_translation: str = pydantic.Field(description="A translation of the understood message in english.")
    guessed_word: str = pydantic.Field(description="A single word guess, in your language, that you think the player is thinking of.")
    translation: str = pydantic.Field(description="A translation of the guessed word in english.")

class WordGuessSignature(dspy.Signature):
    """Guesser for a word game. Based on the chat message, guess the word the player is thinking of."""
    language = dspy.InputField(desc="The only language you understand.", default="english")
    chat_message = dspy.InputField(desc="The message sent by the player describing a word. Assumed to be in the language you understand.")
    reply = dspy.OutputField(desc="A reply to the player, including whether you understood the message, your understanding of the message, a guessed word, and translations.")

class WordGuesser(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predictor = dspy.Predict(WordGuessSignature)

    def forward(self, chat_message):
        return self.predictor(chat_message=chat_message)

def get_guessed_word(message:str) -> Reply:
    """
    Initializes dspy and returns a guessed word based on the chat message.
    """
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    # Default model name without provider prefix
    model_name = os.environ.get("AI_MODEL", "gemini-3.5-flash")

    if not api_key:
        return Reply(
            is_understood=False,
            understood_message="I need an API key to guess!",
            understood_message_translation="I need an API key to guess!",
            guessed_word="None",
            translation="None"
        )

    if not dspy.settings.lm:
        # Use gemini/ provider prefix as requested
        lm = dspy.LM(model=f"gemini/{model_name}", api_key=api_key, max_tokens=8192)
        dspy.settings.configure(lm=lm)

    try:
        guesser = WordGuesser()
        prediction = guesser(chat_message=message)
        return prediction.reply
    except Exception as e:
        return Reply(
            is_understood=False,
            understood_message=f"Error: {str(e)}",
            understood_message_translation=f"Error: {str(e)}",
            guessed_word="None",
            translation="None"
        )
