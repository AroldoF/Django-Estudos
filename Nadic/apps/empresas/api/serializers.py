from rest_framework import serializers
from apps.empresas.models import Empresa, Produto, Venda

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        read_only_fields = ('dono',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        request = self.context.get('request')
        
        # Remove o faturamento_total se o usuário não for o dono
        if request and request.user != instance.dono:
            data.pop('faturamento_total', None)
        
        return data
    
class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'
