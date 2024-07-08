# Generated by Django 4.1.2 on 2024-07-08 04:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentacion', '0013_alter_producto_precio_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_producto',
            field=models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
