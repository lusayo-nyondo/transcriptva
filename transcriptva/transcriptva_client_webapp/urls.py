from django.urls import path

from .views import (
    index,
    sign_in,
    sign_out,
    register,

    transcripts_list,
    audios_list,

    support
)

urlpatterns = [
    path('', index, name="clienthub"),

    path('sign_in', sign_in, name="sign_in"),
    path('sign_out', sign_out, name="sign_out"),
    path('register', register, name="register"),
    
    path('transcripts', transcripts_list, name="transcripts"),

    path('audios', audios_list, name="audios"),

    path('support', support, name="support" )
]