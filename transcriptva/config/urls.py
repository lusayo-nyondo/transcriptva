from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('transcriptva_clientsite.urls')),
    
    path('clienthub/', include('transcriptva_clienthub.urls')),
    
    path('clientsupport/', include('transcriptva_clientsupport.urls')),

    # Grappelli related URLs
    # path('grappelli', include('grappelli.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
