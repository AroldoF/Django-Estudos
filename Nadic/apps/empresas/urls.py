from django.urls import path
from apps.empresas.views import * 
#index, imagem, buscar,nova_imagem,editar_imagem,deletar_imagem
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('', index, name='index'),
    path('imagem/<int:id>', imagem, name='imagem'),
    path('empresa/<str:empresa>', empresa, name='empresa'),
    path('vendas/<int:id>', vendas, name='vendas'),
    path('buscar/', buscar, name='buscar'),
    path('nova-imagem', nova_imagem, name='nova_imagem'),
    path('nova-empresa', nova_empresa, name='nova_empresa'),
    path('nova-venda/<int:id>', nova_venda, name='nova_venda'),
    path('editar-imagem/<int:id>', editar_imagem, name='editar_imagem'),
    path('deletar-imagem/<int:id>', deletar_imagem, name='deletar_imagem'),
    path('editar-empresa/<str:nome>', editar_empresa, name='editar_empresa'),
    path('deletar-empresa/<int:id>', deletar_empresa, name='deletar_empresa'),
    path('editar-venda/<int:id>', editar_venda, name='editar_venda'),
    path('deletar-venda/<int:id>', deletar_venda, name='deletar_venda'),
    path('filtro/<str:categoria>', filtro, name='filtro'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)