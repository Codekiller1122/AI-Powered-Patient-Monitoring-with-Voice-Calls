from django.contrib import admin
from .models import Patient, CheckIn
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone','active')
@admin.register(CheckIn)
class CheckInAdmin(admin.ModelAdmin):
    list_display = ('id','patient','called_at','response_digits')
