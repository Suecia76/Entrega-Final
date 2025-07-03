from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (
    AvatarUpdateView,
    update_profile,
    login_request,
    register,
    profile,
    upload_avatar,
)
urlpatterns = [
    path('editar_avatar/<int:pk>/', AvatarUpdateView.as_view(), name='editar_avatar'), # Editar avatar
    path('login/', login_request ,name='iniciar_sesion'),
    path('register/', register ,name='registro'),
    path('profile/', profile ,name='perfil'),
    path('edit_profile/', update_profile , name ='modificar_perfil'),
    path('edit_avatar/', upload_avatar, name='modificar_avatar'),
    path('logout/', LogoutView.as_view(template_name='usuarios/cerrar_sesion.html'), name='cerrar_sesion'),
]