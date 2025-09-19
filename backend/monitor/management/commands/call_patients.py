from django.core.management.base import BaseCommand
from monitor.models import Patient
from django.conf import settings
from twilio.rest import Client

class Command(BaseCommand):
    help = 'Call active patients for check-ins'

    def handle(self, *args, **options):
        account_sid = settings.TWILIO_ACCOUNT_SID
        auth_token = settings.TWILIO_AUTH_TOKEN
        client = Client(account_sid, auth_token)
        base = settings.PUBLIC_BASE_URL.rstrip('/')
        for p in Patient.objects.filter(active=True):
            try:
                call = client.calls.create(
                    to=p.phone,
                    from_=settings.CHECKIN_CALLER_ID,
                    url=f'{base}/api/monitor/voice/?patient_id={p.id}'
                )
                self.stdout.write(self.style.SUCCESS(f'Calling {p.phone}: {call.sid}'))
            except Exception as e:
                self.stderr.write(f'Failed to call {p.phone}: {e}')
