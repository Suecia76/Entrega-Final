from django.contrib import admin
from .models import Libro
from usuarios.models import Avatar

admin.site.register(Libro)
admin.site.register(Avatar)
