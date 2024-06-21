# Generated by Django 5.0.6 on 2024-06-12 14:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Titulo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medal', models.CharField(blank=True, choices=[('GOLD', 'Gold'), ('SILVER', 'Silver'), ('BRONZE', 'Bronze')], max_length=10, verbose_name='Tipo de valor')),
                ('name', models.CharField(help_text='Poner el nombre así y sólo como está escrito en el artículo', max_length=150, unique=True, verbose_name='Titulo')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, default='https://www.pornhub.com/information/terms#faq', null=True, verbose_name='Descripción')),
                ('image', models.ImageField(blank=True, null=True, upload_to='goods_images', verbose_name='Imagen')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Precio')),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Descuento en %')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Cantidad de stock')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.categories', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'product',
                'ordering': ('id',),
            },
        ),
    ]