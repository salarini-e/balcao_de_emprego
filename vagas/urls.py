
from django.urls import path
from . import views

app_name='vagas'

urlpatterns = [
    path('', views.home, name = 'home'),
]