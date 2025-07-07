from django.contrib import admin
from django.urls import path, include
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar'),
    path('accounts/', include('django.contrib.auth.urls')),  # Adicione esta linha
]
