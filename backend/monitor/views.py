import os
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from .models import Patient, CheckIn
from twilio.twiml.voice_response import VoiceResponse, Gather

def health(request):
    return JsonResponse({'status':'ok'})

@csrf_exempt
def voice_call(request):
    # Twilio will call this when the patient answers.
    resp = VoiceResponse()
    gather = Gather(input='speech dtmf', timeout=5, num_digits=1, action=f'{settings.PUBLIC_BASE_URL}/api/monitor/gather/', method='POST')
    gather.say('Hello. This is your health check-in. Press 1 or say yes if you are feeling well. Press 2 or say no if you need assistance. You may also describe any symptoms after the tone.')
    resp.append(gather)
    resp.say('No response recorded. Goodbye.')
    return HttpResponse(str(resp), content_type='text/xml')

@csrf_exempt
def gather(request):
    from django.utils import timezone
    digits = request.POST.get('Digits')
    speech = request.POST.get('SpeechResult')
    from_number = request.POST.get('From')
    patient = Patient.objects.filter(phone=from_number).first()
    checkin = CheckIn.objects.create(patient=patient, response_text=speech or '', response_digits=digits or '')
    resp = VoiceResponse()
    resp.say('Thank you. Your response has been recorded. Goodbye.')
    return HttpResponse(str(resp), content_type='text/xml')

@csrf_exempt
def incoming_call_to_provider(request):
    resp = VoiceResponse()
    resp.say('This line is for patient monitoring. Goodbye.')
    return HttpResponse(str(resp), content_type='text/xml')
