from django.db import models

from datetime import datetime

from django.contrib.auth.models import User

class Empresa(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    faturamento_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def atualizar_faturamento(self, valor):
        self.faturamento_total += valor
        self.save()

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    OPCOES_CATEGORIA = [
        ("ELETRÔNICOS","Eletrônicos"),
        ("ROUPAS", "Roupas"),
        ("ACESSÓRIOS", "Acessórios"),
        ("DECORAÇÃO", "Decoração"),
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='ELETRÔNICOS')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)

    def venda_produto(self,*args, **kwargs):
        # Verifica se há estoque suficiente
        if self.quantidade > self.produto.estoque:
            raise ValueError("Estoque insuficiente para essa venda!")

        # Calcula o valor total da compra
        self.valor_total = self.quantidade * self.produto.preco

        # Atualiza o estoque do produto
        self.produto.estoque -= self.quantidade
        self.produto.save()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"Venda {self.id} - {self.produto.nome}"
    
