from django.db import models

# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    descricao = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='produtos/')
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Adicional(models.Model):
    nome = models.CharField(max_length=50)  # Ex: "Granola", "Leite Ninho"
    preco_extra = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.nome} (+R${self.preco_extra})"