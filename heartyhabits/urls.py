from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('administrator/', admin.site.urls),
    path('', include('base.urls')),
    path('users/', include('users.urls')),
    path('admin/', include('myadmin.urls')),
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
