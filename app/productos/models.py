from django.db import models
from app.empresas.models import Empresas

class Productos(models.Model):
    codigo = models.CharField('Codigo', max_length=250, null=True, db_index=True)
    nombre = models.CharField('Nombre del Producto', max_length=250, null=True)
    caracteristicas = models.TextField('Caracteristicas', null=True)
    precio = models.CharField('Precio', max_length= 250, null=True)
    empresa = models.ForeignKey(Empresas, on_delete=models.SET_NULL, verbose_name='Empresa id', null=True, blank=True, related_name='empresa_producto')

    class Meta:
        permissions = [("can_list_productos", "Puede listar Productos"),
                       ("can_create_productos", "Puede crear Productos" ),
                       ("can_edit_productos", "Puede editar Productos")]