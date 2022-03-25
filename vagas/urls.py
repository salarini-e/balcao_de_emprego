from django.urls import path
from . import views
app_name='vagas'

urlpatterns = [
    path('', views.home, name='home'),    
    path('cadastrar-vaga/', views.cadastrar_vaga, name='cadastrar'),    
    path('alterar-vaga/alt0x#<id>001', views.alterar_vaga, name='alterar_vaga'),    
    path('vagas/', views.vagas, name='vagas'),    
    path('vagas/table/', views.vagas_table, name='vagas_table'),    
    path('logout/', views.sair, name='logout'),
    path('login/', views.login_view, name='login')
]