from django.forms import ModelForm
from .models import Cliente
from django import forms

class Contato_Cliente(ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'Nome',
            'Email',
            'Mensagem',
            ]
        widgets = {
          'Mensagem': forms.Textarea(attrs={'rows':8, 'cols':32}),
        }
