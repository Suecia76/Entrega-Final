from django.contrib import admin
from django.urls import include,path
from .views import index,about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='inicio'),
    path('blog/', include('blog.urls') , name='blog'),
    path('usuarios/', include('usuarios.urls'), name='usuarios'),
    path('about/', about, name='about'),
]

