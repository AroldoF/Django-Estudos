from django.shortcuts import render, get_object_or_404,redirect

from apps.empresas.models import Empresa, Produto, Venda

from apps.empresas.forms import ProdutoForms, VendaForm, EmpresaForm

from django.contrib import messages



def index(request):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')
    produtos = Produto.objects.order_by("nome")
    return render(request, 'galeria/index.html', {"cards": produtos})

def imagem(request,id):
    produto = get_object_or_404(Produto, pk=id)
    return render(request, 'galeria/imagem.html', {"produtos": produto})

def empresa(request,empresa):
    empresa = get_object_or_404(Empresa, nome=empresa)
    return render(request, 'galeria/empresa.html', {"empresa": empresa})

def vendas(request,id):
    vendas = Venda.objects.filter(produto=id)  # Busca todas as vendas do produto
    produto = Produto.objects.get(id=id)
    return render(request, 'galeria/vendas.html', {"vendas": vendas, "produto": produto})

def buscar(request):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')

    produtos = Produto.objects.order_by("nome")

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            produtos = produtos.filter(nome__icontains=nome_a_buscar)

    return render(request, "galeria/index.html", {"cards": produtos})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')
    
    if request.method == 'POST':
        form = ProdutoForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo Produto cadastrado!')
            return redirect('index')

    form = ProdutoForms
    return render(request, 'galeria/nova_imagem.html',{'form': form})

def nova_empresa(request):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')
    
    if request.method == 'POST':
        form = EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Novo Empresa cadastrado!')
            return redirect('index')

    form = EmpresaForm
    return render(request, 'galeria/nova_empresa.html',{'form': form})

def nova_venda(request, id):
    if not request.user.is_authenticated:
        messages.success(request, "Usuário não logado!")
        return redirect('login')
    
    #produto = get_object_or_404(Produto, id=id)
    produto = Produto.objects.get(id=id)
    empresa = produto.empresa
    if request.method == 'POST':
        form = VendaForm(request.POST, produto)  # Passa o produto para o formulário
        if form.is_valid():
            venda = form.save(commit=False)  
            venda.produto = produto  # Garante que o produto será salvo com a venda
            venda.venda_produto()
            empresa.atualizar_faturamento(venda.valor_total)
            venda.save()  
            empresa.save()
            messages.success(request, 'Nova Venda cadastrada!')
            return redirect('index')

    form = VendaForm
    return render(request, 'galeria/nova_venda.html', {'form': form, 'produto':produto})

def editar_empresa(request, nome):
    empresas = Empresa.objects.get(nome=nome)
    form = EmpresaForm(instance=empresas)

    if request.method == 'POST':
        form = EmpresaForm(request.POST, instance=empresas)
        if form.is_valid():
            form.save()
            messages.success(request, 'Empresa editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_empresa.html', {"form": form, 'nome': nome})

def deletar_empresa(request, id):
    empresas = Empresa.objects.get(id=id)
    empresas.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def editar_imagem(request,id):
    produtos = Produto.objects.get(id=id)
    form = ProdutoForms(instance=produtos)

    if request.method == 'POST':
        form = ProdutoForms(request.POST, instance=produtos)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {"form": form, 'id': id})

def deletar_imagem(request, id):
    produtos = Produto.objects.get(id=id)
    produtos.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def editar_venda(request,id):
    venda = Venda.objects.get(id=id)
    form = VendaForm(instance=venda)

    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            messages.success(request, 'Venda editada com sucesso!')
            return redirect('index')

    return render(request, 'galeria/editar_venda.html', {"form": form, 'id': id})

def deletar_venda(request, id):
    venda = Venda.objects.get(id=id)
    venda.delete()
    messages.success(request, 'Deleção feita com sucesso!')
    return redirect('index')

def filtro(request, categoria):
    produtos = Produto.objects.order_by("nome").filter(categoria=categoria)
    return render(request, 'galeria/index.html', {"cards": produtos})