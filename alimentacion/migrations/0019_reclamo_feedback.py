# Generated by Django 4.1.2 on 2024-07-13 07:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alimentacion', '0018_alter_profile_id_profile_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reclamo',
            fields=[
                ('id_reclamo', models.AutoField(primary_key=True, serialize=False)),
                ('comentario_reclamo', models.CharField(max_length=1000, validators=[django.core.validators.MinLengthValidator(1)])),
                ('nombre_restaurante', models.ForeignKey(db_column='idRest', default=1, on_delete=django.db.models.deletion.CASCADE, to='alimentacion.restaurante')),
            ],
            options={
                'db_table': 'reclamos',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id_Feedback', models.AutoField(primary_key=True, serialize=False)),
                ('comentario_Feedback', models.CharField(max_length=1000, validators=[django.core.validators.MinLengthValidator(1)])),
                ('nombre_restaurante', models.ForeignKey(db_column='idRest', default=1, on_delete=django.db.models.deletion.CASCADE, to='alimentacion.restaurante')),
            ],
            options={
                'db_table': 'Feedback',
            },
        ),
    ]
