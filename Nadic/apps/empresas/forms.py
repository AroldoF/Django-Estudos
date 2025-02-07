from django import forms

from apps.empresas.models import Produto,Venda,Empresa

class ProdutoForms(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'categoria', 'preco', 'estoque', 'empresa']
        labels = {
            'nome': 'Nome do Produto',
            'descricao': 'Descrição',
            'categoria': 'Categoria',
            'preco': 'Preço',
            'estoque': 'Quantidade em Estoque',
            'empresa': 'Empresa',
        }
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}),
            "descricao": forms.Textarea(attrs={'class': 'form-control'}),
            "categoria": forms.Select(attrs={'class': 'form-control'}),
            "preco": forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            "estoque": forms.NumberInput(attrs={'class': 'form-control'}),
            "empresa": forms.Select(attrs={'class': 'form-control'}),
        }
            

class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        #'produto','valor_total'
        fields = [ 'quantidade', 'cliente']
        labels = {
            #'produto': 'Produto',
            'quantidade': 'Quantidade',
            #'valor_total': 'Valor total',
            'cliente': 'Cliente',
        }
        
        widgets = {
            #"produto": forms.Select(attrs={'class': 'form-control'}),
            "quantidade": forms.NumberInput(attrs={'class': 'form-control'}),
            #"valor_total": forms.NumberInput(attrs={'class': 'form-control'}),
            "cliente": forms.TextInput(attrs={'class': 'form-control'}),
            
        }

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome', 'faturamento_total', 'dono']
        labels = {
            'nome': 'Nome',
            'faturamento_total': 'Faturamento Total',
            'dono': 'Dono',
        }
        
        widgets = {
            "nome": forms.TextInput(attrs={'class': 'form-control'}),
            "faturamento_total": forms.NumberInput(attrs={'class': 'form-control'}),
            "dono": forms.Select(attrs={'class': 'form-control'})
        }