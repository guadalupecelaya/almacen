# Generated by Django 3.2.18 on 2023-08-27 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20230510_0625'),
        ('departamentos', '0001_initial'),
        ('usuario', '0001_initial'),
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Solicitudes',
            new_name='Solicitud',
        ),
    ]