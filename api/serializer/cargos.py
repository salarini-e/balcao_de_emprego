from rest_framework import serializers
from vagas.models import Cargo

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = ['id', 'nome'] 
        