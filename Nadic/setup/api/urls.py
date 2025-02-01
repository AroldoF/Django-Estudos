from django.urls import path, include
from rest_framework import routers
from apps.empresas.api.views import EmpresaViewSet, ProdutoViewSet, VendaViewSet
from apps.usuarios.api.views import UsuarioViewSet

router = routers.DefaultRouter()
router.register('empresas', EmpresaViewSet, basename='empresas')
router.register('produtos', ProdutoViewSet, basename='produtos')
router.register('vendas', VendaViewSet, basename='vendas')
router.register('usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
]
