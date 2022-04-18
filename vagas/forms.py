from django import forms
from django.forms import ModelForm, ValidationError
from .models import *

class CadastroVagasForm(ModelForm):    
    class Meta:
        model = Vaga_Emprego
        widgets = {'user': forms.HiddenInput()}
        exclude = ['dt_inclusao']

class Form_Empresa(ModelForm):    
    class Meta:
        model = Empresa
        widgets = {'user': forms.HiddenInput()}
        exclude = ['dt_inclusao']

class Form_Cargo(ModelForm):    
    class Meta:
        model = Cargo
        widgets = {'user': forms.HiddenInput()}
        exclude = ['dt_inclusao']

class Form_Escolaridade(ModelForm):    
    class Meta:
        model = Escolaridade
        widgets = {'user': forms.HiddenInput()}
        exclude = ['dt_inclusao']
