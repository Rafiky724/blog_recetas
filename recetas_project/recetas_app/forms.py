from django import forms
from .models import Receta, Comentario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['titulo', 'descripcion', 'ingredientes', 'instrucciones', 'categoria', 'tiempo_preparacion', 'imagen']

class RegistroUsuarioForm(UserCreationForm):
    
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control'}),
        label="Nombre de Usuario",
    )
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}),
        label="Correo electrónico",
    )
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}),
        help_text=None,
        label="Contraseña",
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'class': 'form-control'}), 
        help_text=None,
        label="Confirmar contraseña",
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {
            'username': None, 
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control'}),
        label=None
    )
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'}),
        label=None
    )
    
    class Meta:
        model = User 
        fields = ['username', 'password']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['contenido'] 
        widgets = {
            'contenido': forms.Textarea(attrs={'placeholder': 'Escribe tu comentario aquí...'}),
        }
