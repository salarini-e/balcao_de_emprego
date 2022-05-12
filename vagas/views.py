# PARA AS VIEWS
from django.views.decorators.clickjacking import xframe_options_exempt
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
    vagas_destaque=Vaga_Emprego.objects.filter(destaque=True)
    vagas=Vaga_Emprego.objects.filter(ativo=True)
    qnt_vagas=len(vagas)
    cont=0
    for i in vagas:
        cont+=i.quantidadeVagas
    context={
        'vagas': vagas_destaque,
        'qnt_cargos': qnt_vagas,
        'qnt_vagas': cont,
        'qnt_destaque': len(vagas_destaque)
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
                'success': [True, 'Empresa cadastrada com sucesso!']
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
def alterar_empresa(request, id):
    empresa=Empresa.objects.get(id=id)
    if request.method=='POST':        
        form=Form_Empresa(request.POST, instance=empresa)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Alterar',
                'form': Form_Empresa(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga alterada com sucesso!']
            }
            return redirect('vagas:empresas')
    else:
        
        form=Form_Empresa(instance=empresa)
    context={
        'form': form,
        'tipo_cadastro': 'Alterar',
    }
    return render(request, 'vagas/cadastrar_empresa.html', context)  

@login_required
def cadastrar_cargo(request):
    if request.method=='POST':        
        form=Form_Cargo(request.POST)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Cadastrar',
                'form': Form_Cargo(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_cargo.html', context)  
    else:
        form=Form_Cargo(initial={'user':request.user})
    context={
        'form': form,
        'tipo_cadastro': 'Cadastrar',
    }
    return render(request, 'vagas/cadastrar_cargo.html', context) 

@login_required
def alterar_cargo(request, id):
    cargo=Cargo.objects.get(id=id)
    if request.method=='POST':        
        form=Form_Cargo(request.POST, instance=cargo)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Alterar',
                'form': Form_Cargo(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga alterada com sucesso!']
            }
            return redirect('vagas:listar_cargos')
    else:
        
        form=Form_Cargo(instance=cargo)
    context={
        'form': form,
        'tipo_cadastro': 'Alterar',
    }
    return render(request, 'vagas/cadastrar_escolaridade.html', context)  

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
def alterar_escolaridade(request, id):
    escolaridade=Escolaridade.objects.get(id=id)
    if request.method=='POST':        
        form=Form_Escolaridade(request.POST, instance=escolaridade)                
        if form.is_valid():
            form.save()
            context={
                'tipo_cadastro': 'Alterar',
                'form': Form_Escolaridade(initial={'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga alterada com sucesso!']
            }
            return redirect('vagas:escolaridades')
    else:
        
        form=Form_Escolaridade(instance=escolaridade)
    context={
        'form': form,
        'tipo_cadastro': 'Alterar',
    }
    return render(request, 'vagas/cadastrar_escolaridade.html', context)  

@login_required
def cadastrar_vagaOfertada(request):
    if request.method=='POST':        
        gambiarra={}     
        for item in request.POST:
            if item=='cargo':
                try:
                    gambiarra[item]=Cargo.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
            elif item=='empresa':
                try:
                    gambiarra[item]=Empresa.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
            else:
                gambiarra[item]=request.POST[item]
        form=CadastroVagasForm(gambiarra)             
        if form.is_valid():                  
            form.save()
            context={
                'tipo_cadastro': 'cadastrar',
                'form': CadastroVagasForm(initial={'ativo': True,'user':request.user}),
                'hidden': ['user', 'ativo'],
                'success': [True, 'Vaga cadastrada com sucesso!']
            }
            return render(request, 'vagas/cadastrar_vagaOfertada.html', context)  
    else:
        form=CadastroVagasForm(initial={'ativo': True,'user':request.user})
    context={
        'tipo_cadastro': 'cadastrar',
        'form': form,
        'hidden': ['user', 'ativo']
    }
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

@login_required
def remover_vaga(request, id):
    if request.method=='POST':        
        try:
            vaga=Vaga_Emprego.objects.get(id=request.POST['remover'])
            vaga.ativo=False
            vaga.save()
            return redirect('vagas:vagas')
        except:
            pass
    context={
        'id': id,
        'vaga': Vaga_Emprego.objects.get(id=id)
    }
    return render(request, 'vagas/remover_vagaOfertada.html', context)

@login_required
def cadastrar_vaga_emLote(request):
    if request.method=='POST': 
        try:
            empresa=Empresa.objects.get(nome=request.POST['empresa'])
            success=True
        except:
            success=False
        if success:                        
            form=CadastroVagasForm(initial={'ativo': True,'user':request.user})
            context={
                'empresa': request.POST['empresa'],
                'tipo_cadastro': 'cadastrar',
                'form': form,
                'hidden': ['user', 'ativo']
            }
            return render(request, 'vagas/cadastrar_vagas_emLote_2.html', context)
    form=CadastroVagasForm(initial={'ativo': True,'user':request.user})
    context={
        'tipo_cadastro': 'cadastrar',
        'form': form,
        'hidden': ['user', 'ativo']
    }
    return render(request, 'vagas/cadastrar_vagas_emLote.html', context)

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


def get_cargo(request):
    try:
        # empresas=Empresa.objects.filter(nome__startswith=request.GET.get('nome')).order_by('nome')
        cargos=Cargo.objects.filter(nome__icontains=request.GET.get('vaga')).order_by('nome')
    except Exception as E:
        print(E)
        cargos=None
    context={
        'results': cargos,
    }
    return render(request, 'vagas/resultVagaSearchs.html', context)

@login_required
def visualizar_vaga(request, id):
    if request.method=='POST':    
        gambiarra={}     
        for item in request.POST:
            if item=='vaga':
                gambiarra[item]=Cargo.objects.get(nome=request.POST[item]).id
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
        'id': id,
        'tipo_cadastro': '',
        'form': form,
        'hidden': ['user', 'ativo', 'destaque'],
        'cargo': vaga.cargo.nome,
        'empresa': vaga.empresa.nome
    }
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

@login_required
def alterar_vaga(request, id):
    if request.method=='POST':    
        gambiarra={}     
        for item in request.POST:
            if item=='cargo':
                try:
                    gambiarra[item]=Cargo.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
            elif item=='empresa':
                try:
                    gambiarra[item]=Empresa.objects.get(nome=request.POST[item]).id
                except:
                    gambiarra[item]=request.POST[item]
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
        'id': id,
        'tipo_cadastro': 'Alterar',
        'form': form,
        'hidden': ['user', 'ativo'],
        'cargo': vaga.cargo.nome,
        'empresa': vaga.empresa.nome
    }
    return render(request, 'vagas/cadastrar_vagaOfertada.html', context)

def vagas(request):
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True).order_by('cargo')
    }
    return render(request, 'vagas/vagas_disponiveis.html', context)

def empresas(request):
    context={
        'empresas': Empresa.objects.all()
    }
    return render(request, 'vagas/listar_empresas.html', context)

def escolaridades(request):
    context={
        'escolaridades': Escolaridade.objects.all()
    }
    return render(request, 'vagas/listar_escolaridade.html', context)

def listar_cargos(request):
    context={
        'vagas': Cargo.objects.all()
    }
    return render(request, 'vagas/listar_cargos.html', context)

def imprimir_vagas(request):
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True).order_by('cargo')
    }
    return render(request, 'vagas/imprimir_vagas.html', context)

@xframe_options_exempt
def vagas_table(request):
    context={
        'vagas': Vaga_Emprego.objects.filter(ativo=True)
    }
    return render(request, 'vagas/vagas.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
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
def encaminhar(request, id):
    from datetime import date
    today = date.today()
    vaga=Vaga_Emprego.objects.get(id=id)
    if request.method=='POST':          
        context={
            'vaga': vaga,
            'date': today,
            'candidato': {'nome': request.POST['nome'], 'cpf': request.POST['cpf']}
        }        
        return render(request, 'vagas/encaminhar.html', context)
        
    return redirect('vagas:encaminhamento', id)

@login_required
def encaminhamento(request, id):    
    context={
        'id': id
    }
    return render(request, 'vagas/encaminhamento.html', context)

@login_required
def sair(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('vagas:home')
    else:
        return redirect('/accounts/login')