from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from .settings.swagger import urlpatterns_swagger as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')),
] + doc_urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
