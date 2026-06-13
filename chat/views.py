import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import ChatMessage

@csrf_exempt
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
        data = json.loads(request.body)
        msg = ChatMessage.objects.create(
            sender=data.get('sender', 'Anonymous'),
            message=data.get('message', '')
        )
        return JsonResponse({
            'status': 'success',
            'message': {
                'sender': msg.sender,
                'message': msg.message,
                'timestamp': msg.timestamp.isoformat()
            }
        }, status=201)
    return JsonResponse({'error': 'Invalid method'}, status=405)
