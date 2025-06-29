from django import forms
from .models import Avatar
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        labels = {
            'imagen': 'Imagen de Avatar',
        }

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de usuario",
        help_text="",
    )
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
 
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(label="Ingrese su email:")
    # password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    username = forms.CharField(label="Nombre de usuario")

    last_name = forms.CharField()
    first_name = forms.CharField()
    is_active = forms.BooleanField(required=False, label="¿Está activo?")

    class Meta:
        model = User
        # fields = ('email', 'password')
        fields = ('username', 'email', 'last_name', 'first_name', 'is_active')