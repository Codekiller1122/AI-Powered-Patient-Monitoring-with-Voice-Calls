from django.db import models
class Patient(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30, help_text='E.164, e.g. +12345556789')
    timezone = models.CharField(max_length=50, default='UTC')
    active = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.name} ({self.phone})'

class CheckIn(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='checkins')
    called_at = models.DateTimeField(auto_now_add=True)
    response_text = models.TextField(blank=True, null=True)
    response_digits = models.CharField(max_length=50, blank=True, null=True)
    recording_url = models.URLField(blank=True, null=True)
    def __str__(self):
        return f'CheckIn {self.id} for {self.patient.name} at {self.called_at}'
