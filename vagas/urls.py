from django.urls import path
from . import views
app_name='vagas'

urlpatterns = [
    path('', views.home, name='home'),  
    path('cadastrar-escolaridade', views.cadastrar_escolaridade, name='cadastrar_escolaridade'),
    path('cadastrar-vaga-ofertada/', views.cadastrar_vagaOfertada, name='cadastrar'),    
    path('cadastrar-empresa/', views.cadastrar_empresa, name='cadastrar_empresa'),    
    path('cadastrar-vaga/', views.cadastrar_vaga, name='cadastrar_vaga'),    
    path('alterar-vaga/alt0x#<id>001', views.alterar_vaga, name='alterar_vaga'),    
    path('vagas/', views.vagas, name='vagas'),    
    path('listar-vagas/', views.listar_vagas, name='listar_vagas'),    
    path('empresas/', views.empresas, name='empresas'),    
    path('vagas/table/', views.vagas_table, name='vagas_table'),    
    path('get_vaga/', views.get_vaga, name='get_vaga' ),
    path('get_empresa/', views.get_empresa, name='get_empresa' ),
    path('logout/', views.sair, name='logout'),
    path('login/', views.login_view, name='login')
]