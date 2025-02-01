from django.contrib import admin

from apps.empresas.models import Produto,Venda,Empresa

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id", "nome", "preco", "estoque","categoria",'empresa')
    list_display_links = ("id", "nome")
    search_fields = ("nome","categoria","empresa")
    list_filter = ("categoria","empresa","preco")
    ordering = ['nome',]
    list_per_page = 10

admin.site.register(Produto,ListandoProdutos)

class ListandoVendas(admin.ModelAdmin):
    list_display = ("id", "produto","quantidade","valor_total", "cliente")
    list_display_links = ("id", )
    search_fields = ("produto","quantidade")
    list_filter = ("quantidade","produto",'valor_total')
    ordering = ['produto','quantidade','valor_total']
    list_per_page = 10

admin.site.register(Venda,ListandoVendas)

class ListandoEmpresas(admin.ModelAdmin):
    list_display = ("id", "nome","dono","faturamento_total",)
    list_display_links = ("id","nome",)
    search_fields = ("nome","dono")
    list_filter = ("faturamento_total",)
    ordering = ['nome',]
    list_per_page = 10

admin.site.register(Empresa,ListandoEmpresas)