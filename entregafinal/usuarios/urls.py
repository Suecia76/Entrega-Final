from django.urls import path

from .views import (
    AvatarUpdateView,
)
urlpatterns = [
    path('editar_avatar/<int:pk>/', AvatarUpdateView.as_view(), name='editar-avatar'), # Editar avatar
    # path('login/',,name='login'),
    # path('register/',,name='register'),
    # path('profile/',,name='profile'),
    # path('profile/<int:id>/',, name ='update_profile'),
]