from django.shortcuts import render

# Create your views here.
def peril(request):
    return render(request, 'usuarios/perfil.html')