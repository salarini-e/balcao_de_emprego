# PARA AS VIEWS
from multiprocessing import context
from django.shortcuts import render, redirect
# AUTH
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
# MODELS E FORMS
from .forms import *
# OUTROS
import requests

# VIEWS
def home(request):    
    vagas=Vaga_Emprego.objects.filter(destaque=True)
    qnt_vagas=len(Vaga_Emprego.objects.all())
    context={
        'vagas': vagas,
        'qnt_vagas': qnt_vagas,
        'qnt_destaque': len(vagas)
    }
    return render(request, 'vagas/index.html', context)

@login_required
def cadastrar_empresa(request):
    if request.method=='POST':        
        form=Form_Empresa(request.POST)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': Form_Empresa(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_empresa.html', context)  
    else:
        form=Form_Empresa(initial={'user':request.user})
    context={
        'form': form,
        'tipo_cadastro': 'Cadastrar',
    }
    return render(request, 'vagas/cadastrar_empresa.html', context)  

@login_required
def cadastrar_vaga(request):
    if request.method=='POST':        
        form=Form_Vaga(request.POST)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': Form_Vaga(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_vaga.html', context)  
    else:
        form=Form_Vaga(initial={'user':request.user})
    context={
        'form': form,
        'tipo_cadastro': 'Cadastrar',
    }
    return render(request, 'vagas/cadastrar_vaga.html', context) 

@login_required
def cadastrar_escolaridade(request):
    if request.method=='POST':        
        form=Form_Escolaridade(request.POST)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': Form_Escolaridade(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_escolaridade.html', context)  
    else:
        form=Form_Escolaridade(initial={'user':request.user})
    context={
        'form': form,
        'tipo_cadastro': 'Cadastrar',
    }
    return render(request, 'vagas/cadastrar_escolaridade.html', context) 

@login_required
def cadastrar_vagaOfertada(request):
    if request.method=='POST':        
        gambiarra={}     
        for item in request.POST:
            if item=='vaga':
                gambiarra[item]=Vaga.objects.get(nome=request.POST[item]).id
            elif item=='empresa':
                gambiarra[item]=Empresa.objects.get(nome=request.POST[item]).id
            else:
                gambiarra[item]=request.POST[item]
        form=CadastroVagasForm(gambiarra)             
        if form.is_valid():                  
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': CadastroVagasForm(initial={'ativo': True,'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_vagaOfertada.html', context)  
    else:
        form=CadastroVagasForm(initial={'ativo': True,'user':request.user})
    context={
        'tipo_cadastro': 'Cadastrar',
        'form': form,
        'hidden': ['user', 'ativo']
    }
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

def get_empresa(request):
    try:
        # empresas=Empresa.objects.filter(nome__startswith=request.GET.get('nome')).order_by('nome')
        empresas=Empresa.objects.filter(nome__icontains=request.GET.get('empresa')).order_by('nome')
    except Exception as E:
        print(E)
        empresas=None
    context={
        'results': empresas,
    }
    return render(request, 'vagas/resultEmpresaSearchs.html', context)


def get_vaga(request):
    try:
        # empresas=Empresa.objects.filter(nome__startswith=request.GET.get('nome')).order_by('nome')
        vagas=Vaga.objects.filter(nome__icontains=request.GET.get('vaga')).order_by('nome')
    except Exception as E:
        print(E)
        vagas=None
    context={
        'results': vagas,
    }
    return render(request, 'vagas/resultVagaSearchs.html', context)

@login_required
def alterar_vaga(request, id):
    if request.method=='POST':    
        gambiarra={}     
        for item in request.POST:
            if item=='vaga':
                gambiarra[item]=Vaga.objects.get(nome=request.POST[item]).id
            elif item=='empresa':
                gambiarra[item]=Empresa.objects.get(nome=request.POST[item]).id
            else:
                gambiarra[item]=request.POST[item]
        form=CadastroVagasForm(gambiarra)    
        vaga=Vaga_Emprego.objects.get(id=id)         
        if form.is_valid():
                
            form=CadastroVagasForm(gambiarra, instance=vaga)  
            form.save()
            return redirect('vagas:vagas')
    else:        
        vaga=Vaga_Emprego.objects.get(id=id)
        form=CadastroVagasForm(instance=vaga)

    context={
        'tipo_cadastro': 'Alterar',
        'form': form,
        'hidden': ['user', 'ativo'],
        'vaga': vaga.vaga.nome,
        'empresa': vaga.empresa.nome
    }
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

def vagas(request):
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True)
    }
    return render(request, 'vagas/vagas_disponiveis.html', context)

def empresas(request):
    context={
        'empresas': Empresa.objects.all()
    }
    return render(request, 'vagas/listar_empresas.html', context)

def listar_vagas(request):
    context={
        'vagas': Vaga.objects.all()
    }
    return render(request, 'vagas/listar_vagas.html', context)

def vagas_table(request):
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True)
    }
    return render(request, 'vagas/vagas.html', context)


def login_view(request):
    if request.method == 'POST':
        #Abaixo recebemos a validação da API do Google do reCAPTCHA
        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': '6LdiIsweAAAAADv7tYKHZ1fCP4pi6FwIZTw4X4Rl',
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        ''' End reCAPTCHA validation '''

        #Se o reCAPTCHA garantir que o usuário é um robô
        if result['success']:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                try:
                    return redirect(request.GET['next'])    
                except:
                    return redirect('vagas:home')
            else:                
                context={
                    'error': True,
                }
                return render(request, 'registration/login.html', context)
        else:
            context={
                'error2': True,            
            }
            return render(request, 'registration/login.html', context)
    return render(request, 'registration/login.html')

@login_required
def sair(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('vagas:home')
    else:
        return redirect('/accounts/login')