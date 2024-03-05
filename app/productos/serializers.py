from rest_framework import serializers
from app.productos.models import Productos

class ProductosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Productos
        fields = '__all__'

    def validate_codigo(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'codigo' no puede estar vacío.")
        return value

    def validate_nombre(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'nombre' no puede estar vacío.")
        return value

    def validate_caracteristicas(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'caracteristicas' no puede estar vacío.")
        return value

    def validate_precio(self, value):
        if not value:
            raise serializers.ValidationError("El campo 'precio' no puede estar vacío.")
        return value
    