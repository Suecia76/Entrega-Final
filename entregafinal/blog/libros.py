from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Libro
from .forms import LibroForm

class LibroListView(ListView):
    model = Libro
    template_name = "libros/libro_list.html"
    context_object_name = "libros"
    ordering = ['-fecha_creacion']

class LibroDetailView(DetailView):
    model = Libro
    template_name = "libros/libro_detail.html"
    context_object_name = "libro"

class LibroCreateView(LoginRequiredMixin, CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libros/libro_form.html"
    success_url = 'libro-list'

    def form_valid(self, form):
        form.instance.creado_por = self.request.user
        return super().form_valid(form)

class LibroUpdateView(LoginRequiredMixin, UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = "libros/libro_form.html"
    success_url = 'libro-list'



class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "libros/libro_confirm_delete.html"
    success_url = 'libro-list'

