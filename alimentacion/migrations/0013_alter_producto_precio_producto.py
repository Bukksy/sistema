# Generated by Django 4.1.2 on 2024-07-08 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentacion', '0012_delete_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_producto',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]