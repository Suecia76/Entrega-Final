from django.contrib import admin
from django.urls import include,path
from .views import index,about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('blog/', include('blog.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('about/', about, name='about'),
]

