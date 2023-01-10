from django.urls import path, include

from .views import support

urlpatterns = [
     path('', include('cms.urls')),
]
