from django.urls import path, include

from wagtail import urls as wagtail_urls

from .views import (
     contact_client_support,
     raise_order_issue
)

urlpatterns = [
     path('contact_client_support', contact_client_support, name="contact_client_support"),
     path('raise_order_issue/<int:order_id>', raise_order_issue, name="raise_order_issue"),
     
     # The client support pages are handled by wagtail
     path('', include(wagtail_urls))
]
