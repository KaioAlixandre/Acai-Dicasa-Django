from django.shortcuts import render, redirect

# Create your views here.
def pedido(request):
    return render(request, 'pedidos/pedido.html')