from django.urls import path
from rest_framework.routers import DefaultRouter
from app.productos.views import ProductosViewSet

router = DefaultRouter()
router.register(r'productos', ProductosViewSet, basename='productos')

urlpatterns = [
    path('productos/data/', ProductosViewSet.as_view({'get': 'getData'}), name='get_data'),
    path('productos/<int:pk>/', ProductosViewSet.as_view({'get': 'getProductos'}), name='get_productos'),
]

urlpatterns += router.urls
