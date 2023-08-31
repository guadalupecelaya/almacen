# Generated by Django 3.2.18 on 2023-08-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudes', '0005_solicitud_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitud',
            name='estado',
            field=models.CharField(choices=[('Pendiente', 'Pendiente'), ('Aceptado', 'Aceptado')], default='Pendiente', max_length=20, verbose_name='Estado'),
        ),
    ]
