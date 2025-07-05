from django.db import models

# Create your models here.
from django.db import models
from usuarios.models import Cliente
from produtos.models import Produto


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('EM_PREPARO', 'Em preparo'),
        ('PRONTO', 'Pronto'),
        ('ENTREGUE', 'Entregue'),
    ]

    PAGAMENTO_CHOICES = [
        ('PIX', 'PIX'),
        ('CARTAO', 'Cartão'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')
    data_hora = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(max_length=10, choices=PAGAMENTO_CHOICES)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente.nome} - {self.status}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto_base = models.ForeignKey(Produto, on_delete=models.CASCADE, related_name='itens_base_pedido')
    preco_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item #{self.id} - {self.produto_base.nome}"