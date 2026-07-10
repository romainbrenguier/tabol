from django.db import models
from enum import Enum

class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    ITALIAN = "it"
    PORTUGUESE = "pt"
    RUSSIAN = "ru"
    CHINESE = "zh"
    JAPANESE_ROMAJI = "ja(ro)"
    KOREAN = "ko"
    DUTCH = "nl"
    TURKISH = "tr"

class ChatMessage(models.Model):
    sender = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __clstr__(self):
        return f"{self.sender}: {self.message[:20]}"
