from django.urls import path
from .libros import (
    LibroListView,
    LibroDetailView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView,
)

urlpatterns = [
    path('', LibroListView.as_view(), name='libro-list'),                    # Lista de libros
    path('libro/<int:pk>/', LibroDetailView.as_view(), name='libro-detail'), # Detalle de un libro
    path('crear_libro/', LibroCreateView.as_view(), name='crear-libro'),     # Crear libro
    path('editar_libro/<int:pk>/', LibroUpdateView.as_view(), name='editar-libro'), # Editar libro
    path('borrar_libro/<int:pk>/', LibroDeleteView.as_view(), name='borrar-libro'), # Borrar libro
]
