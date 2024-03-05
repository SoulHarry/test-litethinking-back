# Generated by Django 3.2.5 on 2024-03-03 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresas',
            options={'permissions': [('can_list_empresas', 'Puede listar Empresas'), ('can_create_empresas', 'Puede crear Empresas'), ('can_edit_empresas', 'Puede editar Empresas')]},
        ),
        migrations.AlterModelOptions(
            name='productos',
            options={'permissions': [('can_list_productos', 'Puede listar Productos'), ('can_create_productos', 'Puede crear Productos'), ('can_edit_products', 'Puede editar Productos')]},
        ),
    ]
