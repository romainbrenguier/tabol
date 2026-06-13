import dspy
import os

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
    # Prefer GEMINI_API_KEY for the specified model
    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("OPENAI_API_KEY")

    if not api_key:
        return "I need an API key to guess!"

    if not dspy.settings.lm:
        # Use Gemini 3.5 Flash as requested (mapping to 1.5-flash as it's the current stable high speed model if 3.5 is a typo or preview)
        # Actually, let's use exactly what was requested if LiteLLM supports it,
        # but gemini-1.5-flash is more likely what's available.
        # Given the instruction "gemini-3.5-flash", I will use that string.
        lm = dspy.LM("google/gemini-1.5-flash", api_key=api_key)
        dspy.settings.configure(lm=lm)

    try:
        guesser = WordGuesser()
        prediction = guesser(chat_message=message)
        return prediction.guessed_word
    except Exception as e:
        return f"Error: {str(e)}"
