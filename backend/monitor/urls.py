from django.urls import path
from . import views, api
urlpatterns = [
    path('monitor/health/', views.health),
    path('monitor/voice/', views.voice_call),
    path('monitor/gather/', views.gather),
    path('monitor/incoming/', views.incoming_call_to_provider),
    path('monitor/patients/', api.patients_list),
    path('monitor/trigger_call/', api.trigger_call),
]
