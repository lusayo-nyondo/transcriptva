from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', include('transcriptva_admin.urls')),

    path('', include('transcriptva_clientsite.urls')),
    
    path('clienthub/', include('transcriptva_clienthub.urls')),
    
    path('clientsupport/', include('transcriptva_clientsupport.urls')),

    path('clientaccount/', include('transcriptva_clientaccount.urls')),

    # Grappelli related URLs
    # path('grappelli', include('grappelli.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
