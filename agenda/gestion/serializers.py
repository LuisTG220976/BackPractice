from rest_framework import serializers
from .models import Importancia

class PruebaSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre  = serializers.CharField(required=True, trim_whitespace=True, max_length=20)
    apellido = serializers.CharField(required=True, trim_whitespace=True, max_length=15) 
    password = serializers.CharField(write_only=True)

    def create(self, data_validada):
        print('Aca se deberia de guardar la info en la BD')
        print(data_validada)
        return


class ImportanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Importancia 
        fields = '__all__'