# Generated by Django 3.2.5 on 2024-03-03 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_nit', models.CharField(db_index=True, max_length=70, null=True, verbose_name='NIT')),
                ('nombre', models.CharField(max_length=300, null=True, verbose_name='Nombre de la Empresa')),
                ('direccion', models.CharField(max_length=250, null=True, verbose_name='Direccion')),
                ('telefono', models.CharField(max_length=250, null=True, verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(db_index=True, max_length=250, null=True, verbose_name='Codigo')),
                ('nombre', models.CharField(max_length=250, null=True, verbose_name='Nombre del Producto')),
                ('caracteristicas', models.TextField(null=True, verbose_name='Caracteristicas')),
                ('precio', models.CharField(max_length=250, null=True, verbose_name='Precio')),
                ('empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_producto', to='app.empresas', verbose_name='Empresa id')),
            ],
        ),
    ]
