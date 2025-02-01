from apps.empresas.models import Empresa, Produto, Venda
from apps.empresas.api.serializers import EmpresaSerializer, ProdutoSerializer, VendaSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

class EmpresaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de empresas.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - id: permite pesquisar os resultados por ID.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EmpresaSerializer: usado para serialização e desserialização de dados.
    """
    queryset = Empresa.objects.all().order_by("id")
    serializer_class = EmpresaSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome',]
    search_fields = ['nome','id',]

class ProdutoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de produtos.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - ProdutoSerializer: usado para serialização e desserialização de dados.
    """
    queryset = Produto.objects.all().order_by("id")
    serializer_class = ProdutoSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['nome','']
    search_fields = ['nome','']

class VendaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de vendas.

    Campos de ordenação:
    - data: permite ordenar os resultados por data.

    Campos de pesquisa:
    - data: permite pesquisar os resultados por data.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - VendaSerializer: usado para serialização e desserialização de dados.
    """
    queryset = Venda.objects.all().order_by("id")
    serializer_class = VendaSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter]
    ordering_fields = ['data','']
    search_fields = ['data',]