from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from requests import request
from rest_framework.parsers import JSONParser
from vagas.models import Cargo, Vaga_Emprego
from .serializer import VagaSerializer, CargoSerializer
from api.serializer import vagas

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import permission_classes
from rest_framework import generics


class Listar_Vagas(generics.ListAPIView):
    queryset=Vaga_Emprego.objects.filter(ativo=True)
    serializer_class=VagaSerializer
    # authentication_classes = (JSONWebTokenAuthentication)
    permission_classes=[IsAuthenticated]

class Listar_Cargos(generics.ListAPIView):
    queryset=Cargo.objects.all()
    serializer_class=CargoSerializer
    # authentication_classes = (JSONWebTokenAuthentication)
    permission_classes=[IsAuthenticated]
