import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Patient
from django.conf import settings
from twilio.rest import Client
from django.views.decorators.http import require_http_methods

def patients_list(request):
    qs = Patient.objects.all()
    data = [{'id':p.id,'name':p.name,'phone':p.phone,'active':p.active} for p in qs]
    return JsonResponse(data, safe=False)

@csrf_exempt
@require_http_methods(['POST'])
def trigger_call(request):
    body = json.loads(request.body.decode('utf-8'))
    pid = body.get('patient_id')
    try:
        p = Patient.objects.get(id=pid)
    except Patient.DoesNotExist:
        return JsonResponse({'error':'not found'}, status=404)
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    base = settings.PUBLIC_BASE_URL.rstrip('/')
    call = client.calls.create(to=p.phone, from_=settings.CHECKIN_CALLER_ID, url=f'{base}/api/monitor/voice/?patient_id={p.id}')
    return JsonResponse({'sid': call.sid})
