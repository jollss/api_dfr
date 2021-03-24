from rest_framework import serializers
from .models import Producto,Categoria,SubCategoria
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class ProductoSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model= Producto
        fields = '__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Categoria
        fields= '__all__'
 
class SubCategoriaSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = SubCategoria
        fields= '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
 
    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])        
        user.save()
        Token.objects.create(user=user) 
        return user