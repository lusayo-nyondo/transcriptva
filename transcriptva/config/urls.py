from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('transcriptva_site.urls')),
    path('blog/', include('transcriptva_blog.urls')),
    path('clienthub/', include('transcriptva_client_webapp.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
