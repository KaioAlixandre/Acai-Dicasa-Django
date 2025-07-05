from django.db import models
from usuarios.models import Cliente
from produtos.models import Produto, Adicional

class Carrinho(models.Model):
    usuario = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)

class ItemCarrinho(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    adicionais = models.ManyToManyField(Adicional, blank=True)  # Opcionais selecionados

    def preco_total(self):
        return self.produto.preco * self.quantidade
