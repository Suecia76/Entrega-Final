from django.shortcuts import redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Avatar
from .forms import AvatarForm, UserRegisterForm, EditProfileForm

@login_required
def profile(request):
    avatar = Avatar.objects.filter(user=request.user).first()
    usuario = request.user
    return render(request, 'usuarios/perfil.html', {'avatar': avatar, 'usuario': usuario})

class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'usuarios/modificar_avatar.html'
    success_url = reverse_lazy('perfil')

    def get_object(self, queryset=None):
        avatar, created = Avatar.objects.get_or_create(user=self.request.user)
        return avatar

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasenia)
            if user is not None:
                login(request, user)
            return redirect('inicio')

    form = AuthenticationForm()

    return render(request, "usuarios/iniciar_sesion.html", {"form": form})

def register(request):

      if request.method == 'POST':

            # form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            # form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"usuarios/registro.html" ,  {"form":form})

@login_required 
def update_profile(request):
    usuario = request.user
    
    if usuario.is_staff == True:
         print("El usuario está activo")

    if request.method == 'POST':

        miFormulario = EditProfileForm(request.POST, instance=usuario)

        if miFormulario.is_valid():

            miFormulario.save()

            return redirect('inicio')

    else:

        miFormulario = EditProfileForm(instance=usuario)

    return render(request, "usuarios/modificar_perfil.html", {"form": miFormulario, "usuario": usuario})

@login_required
def upload_avatar(request):
    avatar, created = Avatar.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES, instance=avatar)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = AvatarForm(instance=avatar)
    return render(request, 'usuarios/modificar_avatar.html', {'form': form})


