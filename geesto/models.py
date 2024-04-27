from django.db import models

class Fabricante(models.Model):
    fabricante = models.CharField(max_length=100, verbose_name='Fabricante')    
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.fabricante
        
class Linha(models.Model):
    linha = models.CharField(max_length=100, verbose_name='Linha')    
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.linha
    

class Categoria(models.Model):
    categoria = models.CharField(max_length=100, verbose_name='Categoria')    
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.categoria


class Produto(models.Model):

    MULTIPLICAR = 'M'
    DIVIDIR = 'D'
    OPERADOR_CHOICES = [
        (MULTIPLICAR,'Multiplicar'),
        (DIVIDIR,'Dividir'),
    ]


    produto = models.CharField(max_length=100, verbose_name='Produto')
    linha = models.ForeignKey(Linha, verbose_name='Linha', on_delete= models.PROTECT)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete= models.PROTECT)
    fabricante = models.ForeignKey(Fabricante, verbose_name='Fabricante', on_delete= models.PROTECT)
    
    unidade_medida_principal = models.CharField(verbose_name='Und. Medida Principal', max_length=2)
    unidade_medida_secundaria = models.CharField(verbose_name='Und. Medida Secundária', max_length=2)

    codigo_barra_und_principal = models.CharField(verbose_name='Código de Barras Und. Principal', max_length=100, blank=True, null=True)
    codigo_barra_und_secundaria = models.CharField(verbose_name='Código de Barras Und. Secundária', max_length=100, blank=True, null=True)

    fator_de_conversao = models.DecimalField(verbose_name='Fator de Conversão', decimal_places=2, max_digits=9, default=1.0)
    operador_de_conversao = models.CharField(verbose_name='Operador de Conversão', choices=OPERADOR_CHOICES, max_length=11, default='Multiplicar')
    
    custo = models.DecimalField(verbose_name='Custo do Produto', decimal_places=2, max_digits=9, default=0.0)
    preco_venda = models.DecimalField(verbose_name='Preço de Venda', decimal_places=2, max_digits=9, default=0.0)
    estoque = models.DecimalField(verbose_name='Estoque', decimal_places=2, max_digits=9, default=0.0)
    
    ativo = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.produto
    
# criar métodos:
    # converter custo
    # converter preço de venda
    # converter estoque