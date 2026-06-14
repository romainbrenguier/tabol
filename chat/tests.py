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

    def test_game_view(self):
        response = self.client.get(reverse('game'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/vocabulaire-japonais.html')
