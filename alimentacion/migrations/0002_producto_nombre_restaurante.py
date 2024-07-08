# Generated by Django 4.1.2 on 2024-06-25 05:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alimentacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='nombre_restaurante',
            field=models.ForeignKey(db_column='idRest', default=1, on_delete=django.db.models.deletion.CASCADE, to='alimentacion.restaurante'),
        ),
    ]
