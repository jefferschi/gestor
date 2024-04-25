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
    produto = models.CharField(max_length=100, verbose_name='Produto')
    linha = models.ForeignKey(Linha, verbose_name='Linha', on_delete= models.PROTECT)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete= models.PROTECT)
    fabricante = models.ForeignKey(Fabricante, verbose_name='Fabricante', on_delete= models.PROTECT)
    ativo = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.produto
    