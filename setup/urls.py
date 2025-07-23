from django.contrib import admin
from django.urls import path, include
from produtos import views
from pedidos import views as pedidos_views
from usuarios import views as usuarios_views

app_name = 'produtos'

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
    path('cadastrar/', views.cadastrar_produto, name='cadastrar'),
    path('accounts/', include('django.contrib.auth.urls')),  # Adicione esta linha
    path('promocoes/', views.promocoes, name='promocoes'),
    path('pedido/', pedidos_views.pedido, name='pedido'),  
    path('perfil/', usuarios_views.peril, name='perfil'),  

]
