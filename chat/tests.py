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
            data=json.dumps({
                'sender': 'Alice',
                'message': 'Hello world',
                'target_language': 'japanese',
                'original_language': 'fr'
            }),
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
        # Test default japanese with original_language param
        response = self.client.get(reverse('game', kwargs={'lang_code': 'japanese'}) + '?original_language=fr')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/game.html')
        self.assertContains(response, 'Japonais')

        # Test german
        response = self.client.get(reverse('game', kwargs={'lang_code': 'german'}) + '?original_language=fr')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Allemand')

        # Test non-existent language
        response = self.client.get(reverse('game', kwargs={'lang_code': 'klingon'}))
        self.assertEqual(response.status_code, 404)

    def test_timers_view(self):
        response = self.client.get(reverse('timers'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'chat/timers.html')
        self.assertContains(response, 'Machine à laver')
        self.assertContains(response, 'Four')

    def test_reset_history(self):
        session = self.client.session
        session['chat_history'] = ["Test message"]
        session.save()

        # Call reset endpoint
        url_reset = reverse('reset_history')
        response = self.client.post(url_reset)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(self.client.session.get('chat_history'), None)
