"""from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
    
from .models import Producto
from .serializers import ProductoSerializer
    
class ProductoList(APIView):
    def get(self,request):
        prod = Producto.objects.all()[:20]
        data = ProductoSerializer(prod, many=True).data
        return Response(data)
    
class ProductoDetalle(APIView):
    def get(self,request,pk):
        prod = get_object_or_404(Producto, pk=pk)
        data = ProductoSerializer(prod).data
        return Response(data)"""
#Escogiendo cuál clase base usar

"""Hemos visto 4 tipos de vistas

    Vistas Django Puro

    Sub Clases APIView

    Sub Clases generics.*

    viewsets.ModelViewSet

Así que cómo o cuándo usar cual vista.  Aunque no es ley, sólo planteo posibilidades que considero más adecuadas.

    Use viewsets.ModelViewSet cuando va a permitir todas o la mayoría de las operaciones CRUD en un modelo.

    Use genéricos.* Cuando solo desee permitir algunas operaciones en un modelo

    Usa APIView cuando quieras personalizar completamente el comportamiento

Bueno y con esto terminamos esta sección y ya sólo nos falta ver cómo tener control de acceso a nuestra

api."""
#---------
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
#-----
 
from .models import *
from .serializers import ProductoSerializer,CategoriaSerializer,SubCategoriaSerializer,UserSerializer
from django.contrib.auth import authenticate
from .permissions import IsOwner

class ProductoList(generics.ListCreateAPIView):#devuelve una lista de todo get y post
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
 
 
class ProductoDetalle(generics.RetrieveDestroyAPIView):#recupera datos de 1 entidad o eliminar delete o get
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class CategoriaSave(generics.CreateAPIView):#crear entidades pero no lista post
    serializer_class = CategoriaSerializer
 
class SubCategoriaSave(generics.CreateAPIView):
        serializer_class = SubCategoriaSerializer

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
"""class SubCategoriaList(generics.ListCreateAPIView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaSerializer"""

#------------------------------------
class CategoriaDetalle(generics.RetrieveDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class SubCategoriaList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = SubCategoria.objects.filter(categoria_id=self.kwargs["pk"])
        return queryset
    serializer_class = SubCategoriaSerializer

class SubCategoriaAdd(APIView):
    def post(self,request,cat_pk):
        descripcion = request.data.get("descripcion")
        data = {'categoria': cat_pk, 'descripcion':descripcion}
        serializer = SubCategoriaSerializer(data=data)
        if serializer.is_valid():
            subcat = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsOwner]

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer


class LoginView(APIView):
    permission_classes = ()
 
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "error en credenciales"}, status=status.HTTP_400_BAD_REQUEST)