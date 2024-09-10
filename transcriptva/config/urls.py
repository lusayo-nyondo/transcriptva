from django.conf import settings
from django.urls import path, include

from django.conf.urls.static import static

#from wagtail import urls as wagtail_urls
#from wagtail.admin import urls as wagtailadmin_urls
#from wagtail.documents import urls as wagtaildocs_urls


urlpatterns = [
    path('model-admin/', include('transcriptva_admin.urls')),

    path('', include('transcriptva_clientsite.urls')),
    
    path('clienthub/', include('transcriptva_clienthub.urls')),
    
    #path('clientsupport/', include('transcriptva_clientsupport.urls')),

    path('clientaccount/', include('transcriptva_clientaccount.urls')),

    # Wagtail URLs
    #path('content-admin/', include(wagtailadmin_urls)),
    #path('documents/', include(wagtaildocs_urls)),
    
    # Wagtail's serving mechanism
    #path('pages/', include(wagtail_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
