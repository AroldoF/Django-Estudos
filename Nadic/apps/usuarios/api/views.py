from django.contrib.auth.models import User
from rest_framework import viewsets
from apps.usuarios.api.serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de usuários.

    Campos de ordenação:
    - id: permite ordenar os resultados por ID.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - UsuarioSerializer: usado para serialização e desserialização de dados.
    """
    queryset = User.objects.all().order_by("id")
    serializer_class = UsuarioSerializer
