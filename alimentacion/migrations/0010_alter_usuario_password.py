# Generated by Django 4.1.2 on 2024-07-06 01:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alimentacion', '0009_alter_diariosemanal_id_diariosemanal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(2)]),
        ),
    ]
