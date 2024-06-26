# Generated by Django 5.0.4 on 2024-04-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geesto', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='codigo_barra_und_principal',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Código de Barras Und. Principal'),
        ),
        migrations.AddField(
            model_name='produto',
            name='codigo_barra_und_secundaria',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Código de Barras Und. Secundária'),
        ),
        migrations.AddField(
            model_name='produto',
            name='custo',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Custo do Produto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Estoque'),
        ),
        migrations.AddField(
            model_name='produto',
            name='fator_de_conversao',
            field=models.DecimalField(decimal_places=2, default=1.0, max_digits=9, verbose_name='Fator de Conversão'),
        ),
        migrations.AddField(
            model_name='produto',
            name='operador_de_conversao',
            field=models.CharField(choices=[('M', 'Multiplicar'), ('D', 'Dividir')], default='Multiplicar', max_length=11, verbose_name='Operador de Conversão'),
        ),
        migrations.AddField(
            model_name='produto',
            name='preco_venda',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Preço de Venda'),
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade_medida_principal',
            field=models.CharField(default='', max_length=2, verbose_name='Und. Medida Principal'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade_medida_secundaria',
            field=models.CharField(default='', max_length=2, verbose_name='Und. Medida Secundária'),
            preserve_default=False,
        ),
    ]
