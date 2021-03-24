from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from dj_puro.models import Categoria

# Create your views here.
def categoria_list(request):
    categorias=Categoria.objects.all().values("id","descripcion","activo")
    data={'datos':list(categorias)}
    return JsonResponse(data)
 
def categoria_detalle(request,id):
    cat = get_object_or_404(Categoria, id=id)
    data = {"results": {"descripcion": cat.descripcion,"activo": cat.activo }}
    return JsonResponse(data)