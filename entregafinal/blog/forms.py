
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['titulo', 'autor', 'fecha_publicacion', 'descripcion','genero', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'titulo': 'Título',
            'autor': 'Autor',
            'fecha_publicacion': 'Fecha de Publicación',
            'descripcion': 'Descripción',
            'genero': 'Género',
            'imagen': 'Imagen',
        }

