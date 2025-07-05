from django.contrib import admin
from django.contrib.auth.admin import UserAdmin  # Importe UserAdmin
from .models import Cliente, Endereco

# Registre o model Cliente apenas UMA vez:
admin.site.register(Cliente, UserAdmin)  # Usando UserAdmin para manter a interface padrão
admin.site.register(Endereco)
