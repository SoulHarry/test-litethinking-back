from rest_framework import serializers
from app.empresas.models import Empresas

class EmpresasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empresas
        fields = '__all__'

    def validate_id_nit(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'id_nit' no puede estar vacío.")
        return value

    def validate_nombre(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'nombre' no puede estar vacío.")
        return value

    def validate_direccion(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'direccion' no puede estar vacío.")
        return value

    def validate_telefono(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'telefono' no puede estar vacío.")
        return value
    