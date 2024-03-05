from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from app.productos.permissions import IsAdminOrReadOnly
from app.productos.models import Productos
from app.productos.serializers import ProductosSerializer

class ProductosViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductosSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def getData(self, request):
        productos = Productos.objects.all()
        serializer = self.get_serializer(productos, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def getProductos(self, request, pk=None):
        productos = self.get_object()
        serializer = self.get_serializer(productos, many=False)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        producto = self.get_object()
        serializer = self.get_serializer(instance=producto, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        producto = self.get_object()
        self.perform_destroy(producto)
        return Response('User successfully deleted!')
