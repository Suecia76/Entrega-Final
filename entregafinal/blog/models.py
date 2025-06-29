from django.db import models
from django.contrib.auth.models import User

class Libro(models.Model):
    titulo = models.CharField(max_length=200)  
    autor = models.CharField(max_length=100)  
    genero = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField()            
    imagen = models.ImageField(upload_to='libros/', blank=True, null=True)
    fecha_publicacion = models.DateField(null=True, blank=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo