# Generated by Django 4.1.2 on 2024-06-25 05:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.AutoField(db_column='idCategorias', primary_key=True, serialize=False)),
                ('nombre_categoria', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
            options={
                'db_table': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20, unique=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('email', models.EmailField(blank=True, max_length=100, null=True, unique=True)),
                ('password', models.TextField(validators=[django.core.validators.MinLengthValidator(2)])),
            ],
            options={
                'db_table': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Restaurante',
            fields=[
                ('id_restaurante', models.AutoField(db_column='idRest', primary_key=True, serialize=False)),
                ('nombre_restaurant', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('descripcion_restaurante', models.CharField(max_length=150, validators=[django.core.validators.MinLengthValidator(1)])),
                ('ubicacion_restaurant', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
                ('id_categoriarest', models.ForeignKey(db_column='idCategorias', on_delete=django.db.models.deletion.CASCADE, to='alimentacion.categoria')),
            ],
            options={
                'db_table': 'restaurantes',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='idProd', primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('descripcion_producto', models.CharField(max_length=500, validators=[django.core.validators.MinLengthValidator(1)])),
                ('cantidad', models.IntegerField()),
                ('categoria_prod', models.ForeignKey(db_column='idCategorias', on_delete=django.db.models.deletion.CASCADE, to='alimentacion.categoria')),
            ],
            options={
                'db_table': 'productos',
            },
        ),
    ]