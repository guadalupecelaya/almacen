# Generated by Django 3.2.18 on 2023-08-30 02:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_alter_producto_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='productos.tipoproducto', verbose_name='Nombre'),
        ),
    ]
