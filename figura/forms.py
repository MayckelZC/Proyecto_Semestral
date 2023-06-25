from django import forms
from figura.models import Contacto, Figuras
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields='__all__'
            
class FigurasForm(forms.ModelForm):

    class Meta:
        model = Figuras
        fields='__all__'
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields=['username', "first_name","email","password1","password2"]