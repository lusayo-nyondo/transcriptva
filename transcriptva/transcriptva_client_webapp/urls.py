from django.urls import path

from .views import (
    index,
    sign_in,
    sign_out,
    register,

    orders_list,
    order_transcript,

    transcripts_list,

    support
)

urlpatterns = [
    path('', index, name="clienthub"),

    path('sign_in', sign_in, name="sign_in"),
    path('sign_out', sign_out, name="sign_out"),
    path('register', register, name="register"),
    
    path('orders', orders_list, name="orders"),
    path('order_transcript', order_transcript, name="order_transcript"),

    path('transcripts', transcripts_list, name="transcripts"),

    path('support', support, name="support" )
]