from django.shortcuts import render
from .forms import *
# Create your views here.
def home(request):
    if request.method=='POST':
        form=CadastroVagasForm(request.POST)                
    else:
        form=CadastroVagasForm()
    context={
        'form': form
    }
    return render(request, 'vagas/index.html', context)