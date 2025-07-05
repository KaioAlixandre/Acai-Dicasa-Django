
from django.contrib import admin
from django.urls import path
from produtos import views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar'),
]
