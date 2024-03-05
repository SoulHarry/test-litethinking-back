from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from app.empresas.permissions import IsAdminOrReadOnly
from app.empresas.models import Empresas
from app.empresas.serializers import EmpresasSerializer

class EmpresasViewSet(viewsets.ModelViewSet):
    queryset = Empresas.objects.all()
    serializer_class = EmpresasSerializer
    permission_classes = [IsAdminOrReadOnly, IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def getData(self, request):
        empresas = Empresas.objects.all()
        serializer = self.get_serializer(empresas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def getEmpresas(self, request, pk=None):
        empresas = self.get_object()
        serializer = self.get_serializer(empresas, many=False)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        if not request.data or request.data.is_empty():
            return Response({'error': 'No se proporcionaron datos'}, status=400)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        empresa = self.get_object()
        serializer = self.get_serializer(instance=empresa, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        empresa = self.get_object()
        self.perfom_destroy(empresa)
        return Response('Empresa Eliminada con Exito')
