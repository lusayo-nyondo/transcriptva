from django.urls import path

from .views import (
    personal_details,
    change_password,
    delete_account,

    payment_details
)

urlpatterns = [
    path('', personal_details, name="personal_details"),
    path('change_password', change_password, name="change_password"),
    path('delete_account', delete_account, name="delete_account"),

    path('payment_details', payment_details, name="payment_details")
]
