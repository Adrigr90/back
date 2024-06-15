from rest_framework import serializers
from .models import Vehiculo

class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ['matricula', 'usuario', 'marca', 'modelo', 'categoria','anio']
