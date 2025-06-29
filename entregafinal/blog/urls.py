from django.urls import path
from .views import (
    LibroListView,
    LibroDetailView,
    LibroCreateView,
    LibroUpdateView,
    LibroDeleteView,
    confirmacion_borrado,
)

urlpatterns = [
    path('/libros', LibroListView.as_view(), name='lista_libros'),                    # Lista de libros
    path('libro/<int:pk>/', LibroDetailView.as_view(), name='detalle_libro'), # Detalle de un libro
    path('crear_libro/', LibroCreateView.as_view(), name='crear_libro'),     # Crear libro
    path('editar_libro/<int:pk>/', LibroUpdateView.as_view(), name='editar_libro'), # Editar libro
    path('confirmacion_libro/<int:pk>/', confirmacion_borrado , name='confirmacion_libro'), # Confirmación de borrado
    path('borrar_libro/<int:pk>/', LibroDeleteView.as_view(), name='borrar_libro'), # Borrar libro
]
