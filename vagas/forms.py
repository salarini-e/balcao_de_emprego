from django import forms
from django.forms import ModelForm, ValidationError
from .models import *
from .validations import validate_CNPJ
class CadastroVagasForm(ModelForm):    
    class Meta:
        model = Vaga_Emprego
        widgets = {'user': forms.HiddenInput()}
        exclude = ['dt_inclusao']

class Form_Empresa(ModelForm):  
    cnpj = forms.CharField(label='CNPJ', max_length=18, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,icnpj)"}))  
    telefone = forms.CharField(label='telefone', max_length=15, widget = forms.TextInput(attrs={'onkeydown':"mascara(this,itel)"}))  

    class Meta:
        model = Empresa
        widgets = {'user': forms.HiddenInput()}
        exclude = ['dt_inclusao']

    def clean_cnpj(self):
        print(self.cleaned_data["cnpj"])
        cnpj = validate_CNPJ(self.cleaned_data["cnpj"])
        cnpj = cnpj.replace('.', '')
        cnpj = cnpj.replace('-', '')
        return cnpj

    def clean_telefone(self):
        print(self.cleaned_data["telefone"])
        telefone = validate_TELEFONE(self.cleaned_data["telefone"])        
        return telefone

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
