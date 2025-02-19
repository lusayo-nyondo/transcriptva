from django.urls import path

from .views import (
    index,
    notifications,

    sign_in,
    sign_out,
    register,

    orders_list,
    order_transcript,
    make_order_payment,
    view_order,

    transcripts_list,
    view_transcript
)

urlpatterns = [
    path('', index, name="clienthub"),
    path('notifications', notifications, name="notifications"),

    path('sign_in', sign_in, name="sign_in"),
    path('sign_out', sign_out, name="sign_out"),
    path('register', register, name="register"),
    
    path('orders', orders_list, name="orders"),
    path('order_transcript', order_transcript, name="order_transcript"),
    path('view_order/<int:order_id>', view_order, name="view_order"),
    path('make_order_payment/<int:order_id>', make_order_payment, name="make_order_payment"),

    path('transcripts', transcripts_list, name="transcripts"),
    path('view_transcript/<int:transcript_id>', view_transcript, name="view_transcript")
]
