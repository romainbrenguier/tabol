from django.test import TestCase, Client
from django.urls import reverse
from .models import ChatMessage
import json

class ChatAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('messages')

    def test_post_message(self):
        response = self.client.post(
            self.url,
            data=json.dumps({'sender': 'Alice', 'message': 'Hello world'}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        # 1 user message + 1 AI guess message
        self.assertEqual(ChatMessage.objects.count(), 2)
        self.assertEqual(ChatMessage.objects.filter(sender='Alice').count(), 1)
        self.assertEqual(ChatMessage.objects.filter(sender='AI_Bot').count(), 1)

    def test_get_messages(self):
        ChatMessage.objects.create(sender='Alice', message='Hello')
        ChatMessage.objects.create(sender='Bob', message='Hi')

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertEqual(len(data['messages']), 2)
        self.assertEqual(data['messages'][0]['sender'], 'Alice')
        self.assertEqual(data['messages'][1]['sender'], 'Bob')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/index.html')

    def test_game_view(self):
        # Test default japanese
        response = self.client.get(reverse('game', kwargs={'lang_code': 'japanese'}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/game.html')
        self.assertContains(response, 'Japonais')

        # Test german
        response = self.client.get(reverse('game', kwargs={'lang_code': 'german'}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Allemand')

        # Test non-existent language
        response = self.client.get(reverse('game', kwargs={'lang_code': 'klingon'}))
        self.assertEqual(response.status_code, 404)

    def test_reset_history(self):
        from chat.views import history
        # Ensure history is empty initially (or at least we know its state)
        history.clear()

        # Post a message to populate history
        # Mocking AI might be needed if we don't want real API calls,
        # but let's see if we can just check if it's cleared after the call.

        # Manually add to history for testing purposes
        history.append("Test message")
        self.assertEqual(len(history), 1)
        ChatMessage.objects.create(sender='Alice', message='Hello')
        self.assertEqual(ChatMessage.objects.count(), 1)

        # Call reset endpoint
        url_reset = reverse('reset_history')
        response = self.client.post(url_reset)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(history), 0)
        self.assertEqual(ChatMessage.objects.count(), 0)
