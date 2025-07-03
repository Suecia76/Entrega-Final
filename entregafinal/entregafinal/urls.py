from django.contrib import admin
from django.urls import include,path
from .views import index,about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('blog/', include('blog.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('about/', about, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)