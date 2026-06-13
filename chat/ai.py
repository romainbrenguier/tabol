import dspy
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class WordGuessSignature(dspy.Signature):
    """Guesser for a word game. Based on the chat message, guess the word the player is thinking of."""
    chat_message = dspy.InputField(desc="The message sent by the player describing a word.")
    guessed_word = dspy.OutputField(desc="A single word guess.")

class WordGuesser(dspy.Module):
    def __init__(self):
        super().__init__()
        self.predictor = dspy.Predict(WordGuessSignature)

    def forward(self, chat_message):
        return self.predictor(chat_message=chat_message)

def get_guessed_word(message):
    """
    Initializes dspy and returns a guessed word based on the chat message.
    """
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")
    # Default model name without provider prefix
    model_name = os.environ.get("AI_MODEL", "gemini-3.5-flash")

    if not api_key:
        return "I need an API key to guess!"

    if not dspy.settings.lm:
        # Use gemini/ provider prefix as requested
        lm = dspy.LM(model=f"gemini/{model_name}", api_key=api_key, max_tokens=8192)
        dspy.settings.configure(lm=lm)

    try:
        guesser = WordGuesser()
        prediction = guesser(chat_message=message)
        return prediction.guessed_word
    except Exception as e:
        return f"Error: {str(e)}"
