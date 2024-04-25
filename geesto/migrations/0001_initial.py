# Generated by Django 5.0.4 on 2024-04-25 21:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(max_length=100, verbose_name='Categoria')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fabricante', models.CharField(max_length=100, verbose_name='Fabricante')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Linha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linha', models.CharField(max_length=100, verbose_name='Linha')),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('produto', models.CharField(max_length=100, verbose_name='Produto')),
                ('ativo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='geesto.categoria', verbose_name='Categoria')),
                ('fabricante', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='geesto.fabricante', verbose_name='Fabricante')),
                ('linha', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='geesto.linha', verbose_name='Linha')),
            ],
        ),
    ]
