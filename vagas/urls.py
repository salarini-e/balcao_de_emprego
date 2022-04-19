from django.urls import path
from . import views
app_name='vagas'

urlpatterns = [
    path('', views.home, name='home'),  
    path('cadastrar-escolaridade', views.cadastrar_escolaridade, name='cadastrar_escolaridade'),
    path('cadastrar-vaga-ofertada/', views.cadastrar_vagaOfertada, name='cadastrar'),    
    path('cadastrar-empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),    
    path('cadastrar-cargo/', views.cadastrar_cargo, name='cadastrar_cargo'),    
    path('cadastrar-vaga-em-lote/', views.cadastrar_vaga_emLote, name='cadastrar_vaga_emLote'),    
    path('alterar-vaga/alt0x#<id>001', views.alterar_vaga, name='alterar_vaga'),    
    path('alterar-empresa/alt0x#<id>001', views.alterar_empresa, name='alterar_empresa'),    
    path('alterar-escolaridade/alt0x#<id>001', views.alterar_escolaridade, name='alterar_escolaridade'),    
    path('alterar-cargo/alt0x#<id>001', views.alterar_cargo, name='alterar_cargo'),    
    path('visualizar-vaga/alt0x#<id>001', views.visualizar_vaga, name='visualizar_vaga'),    
    path('remover-vaga/alt0x#<id>001', views.remover_vaga, name='remover_vaga'),    
    path('visualizar-vaga/alt0x#<id>/encaminhar', views.encaminhar, name='encaminhar'),    
    path('visualizar-vaga/alt0x#<id>001/encaminhamento', views.encaminhamento, name='encaminhamento'),    
    path('vagas/', views.vagas, name='vagas'),    
    path('listar-cargos/', views.listar_cargos, name='listar_cargos'),    
    path('empresas/', views.empresas, name='empresas'),    
    path('escolaridades/', views.escolaridades, name='escolaridades'),    
    path('vagas/table/', views.vagas_table, name='vagas_table'),    
    path('get_vaga/', views.get_cargo, name='get_vaga' ),
    path('get_empresa/', views.get_empresa, name='get_empresa' ),
    path('logout/', views.sair, name='logout'),
    path('login/', views.login_view, name='login')
]