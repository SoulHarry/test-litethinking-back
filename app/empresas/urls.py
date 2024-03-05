from django.urls import path
from rest_framework.routers import DefaultRouter
from app.empresas.views import EmpresasViewSet

router = DefaultRouter()
router.register(r'empresas', EmpresasViewSet, basename='empresas')

urlpatterns = [
    path('empresas/data/', EmpresasViewSet.as_view({'get': 'getData'}), name='get_data'),
    path('empresas/<int:pk>/', EmpresasViewSet.as_view({'get': 'getEmpresas'}), name='get_empresas'),
]

urlpatterns += router.urls