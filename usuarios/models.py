from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User

class Cliente(AbstractUser):
    telefone = models.CharField(max_length=15, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    email = models.EmailField('E-mail', unique=True)  # Email único

    # Configurações obrigatórias
    USERNAME_FIELD = 'email'  # Usa email para login
    REQUIRED_FIELDS = ['username', 'telefone']  # Campos para createsuperuser

    def __str__(self):
        return self.email

class Endereco(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='enderecos')
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    principal = models.BooleanField(default=False)  # Se for o endereço padrão do cliente

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.bairro}"