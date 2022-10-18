from django.urls import path

from .views import (
    automated_transcription_service,
    home,
    manual_transcription_service,
    privacy_policy,
    terms_and_conditions,
    services,
    tools,
    support
)

urlpatterns = [
    path('', home, name='home'),
    path('privacy_policy', privacy_policy, name='privacy_policy'),
    path('terms_and_conditions', terms_and_conditions, name='terms_and_conditions'),
    path('tools', tools, name='tools'),
    path('support', support, name='support'),

    path('services', services, name='services'),
    path('services/automated_transcription', automated_transcription_service, name='automated_transcription_service'),
    path('services/manual_transcription', manual_transcription_service, name='manual_transcription_service')
]
