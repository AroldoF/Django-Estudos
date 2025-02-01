from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','is_staff']

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email', '')
        )
        user.set_password(validated_data['password'])  # Criptografa a senha
        user.save()
        return user
