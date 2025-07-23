from django.contrib import admin
from django.urls import path, include
from produtos import views
from pedidos import views as v
from usuarios import views as u
app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar'),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('promocoes/', views.promocoes, name='promocoes'),
    path('pedidos/', v.pedido, name='pedido'),
    path('perfil/', u.perfil, name='perfil'),  
]
