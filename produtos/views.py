from django.shortcuts import render, redirect
from .models import Produto, Categoria
from .forms import ProdutoForm

def lista_produtos(request):
    produtos = Produto.objects.filter(disponivel=True)
    categorias = Categoria.objects.all()
    return render(request, 'produtos/produtos.html', {
        'produtos': produtos,
        'categorias': categorias,
    })

def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')  # volta para a lista de produtos
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastrar.html', {'form': form})

def promocoes(request):
    produtos = Produto.objects.filter(disponivel=True)
    return render(request, 'produtos/promocoes.html', {'produtos': produtos})