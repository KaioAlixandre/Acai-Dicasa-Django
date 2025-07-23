from django.shortcuts import render, redirect

# Create your views here.
def perfil(request):
    return render(request, 'usuarios/perfil.html')