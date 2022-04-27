from rest_framework import serializers
from vagas.models import Vaga_Emprego

class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga_Emprego
        fields = ['quantidadeVagas', 'cargo', 'experiencia', 'escolaridade'] 
        