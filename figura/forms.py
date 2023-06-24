from django import forms

from figura.models import Contacto, Figuras
from django.contrib.auth.forms import UserCreationForm

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields='__all__'
            
class FigurasForm(forms.ModelForm):

    class Meta:
        model = Figuras
        fields='__all__'
class CustomUserCreationForm(UserCreationForm):
    pass