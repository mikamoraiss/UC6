from django.shortcuts import render
from .models import Cliente, Produto, Pedido

# Create your views here.
def home(request):
    return render(request, 'home.html')

def contatos(request):
    return render(request, 'contato.html')

def sobre(request):
    return render(request, 'sobre.html')

def endereco(request):
    return render(request, 'endereco.html')

def blog(request):
    return render(request, 'blog.html')

def parceiros(request):
    return render(request, 'parceiros.html')

def cadastrar_cliente(request):
    if request.method == 'post':
        nome = request.post.get['nome']
        telefone = request.post.get['telefone']
        email = request.post.get['email']
        Cliente.objects.create(nome=nome, telefone=telefone, email=email)
    return render(request, 'cadastro_cliente.html')

def cadastrar_produto(request):
    if request.method == 'post':
        nome = request.post.get['nome']
        quantidade = request.post.get['quantidade']
        valor = request.post.get['valor']
        Cliente.objects.create(nome=nome, quantidade=quantidade, valor=valor)
    return render(request, 'cadastro_produto.html')

def pedido(request):
    if request.method == 'post':
        id = request.post.get['id']
        cliente = request.post.get['cliente']
        produto = request.post.get['produto']
        quantidade = request.post.get['quantidade']
        Cliente.objects.create(id=id, cliente=cliente, produto=produto, quantidade=quantidade)
    return render(request, 'pedido.html')



