from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Libro
from usuarios.models import Avatar
from .forms import LibroForm

class LibroListView(ListView):
    model = Libro
    template_name = "blog/lista_libros.html"
    context_object_name = "libros"
    ordering = ['-fecha_creacion']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        return context

class LibroDetailView(DetailView):
    model = Libro
    template_name = "blog/detalle_libro.html"
    context_object_name = "libro"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        return context

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "blog/crear_libro.html"
    success_url = reverse_lazy('lista_libros')

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        return context

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "blog/modificar_libro.html"
    success_url = reverse_lazy('lista_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        return context

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "blog/confirmacion_libro.html"
    success_url = reverse_lazy('lista_libros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['avatar'] = Avatar.objects.filter(user=self.request.user).first()
        return context

def confirmacion_borrado(request, pk):
    libro = Libro.objects.get(pk=pk)
    return render(request, 'blog/confirmacion_libro.html', {'libro': libro})