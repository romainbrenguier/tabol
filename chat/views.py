import json
from django.shortcuts import render
from django.http import JsonResponse
from .models import ChatMessage

def game_view(request):
    return render(request, 'chat/vocabulaire-japonais.html')

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

            msg = ChatMessage.objects.create(
                sender=sender,
                message=message_text
            )
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
