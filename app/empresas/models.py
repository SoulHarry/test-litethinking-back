from django.db import models

class Empresas(models.Model):
    id_nit = models.CharField('NIT',max_length=70, null=True, db_index=True)
    nombre = models.CharField('Nombre de la Empresa', max_length=300, null=True)
    direccion = models.CharField('Direccion', max_length=250,null=True)
    telefono = models.CharField('Telefono', max_length=250, null=True)

    class Meta:
        permissions = [("can_list_empresas", "Puede listar Empresas"),
                       ("can_create_empresas", "Puede crear Empresas" ),
                       ("can_edit_empresas", "Puede editar Empresas")]