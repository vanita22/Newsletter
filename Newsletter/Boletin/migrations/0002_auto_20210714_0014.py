# Generated by Django 2.2 on 2021-07-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Boletin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletin',
            name='categorias',
            field=models.ManyToManyField(blank=True, to='Categoria.Categoria'),
        ),
    ]
