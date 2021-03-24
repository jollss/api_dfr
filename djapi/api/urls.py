from django.urls import path 
from rest_framework.routers import DefaultRouter
from api.apiviews import *
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('v2/productos', ProductoViewSet, basename='productos')

    #luego de iniciar urlpatterns


urlpatterns = [
    path('v1/productos/', ProductoList.as_view(),name='producto_list' ),
    path('v1/productos/<int:pk>', ProductoDetalle.as_view(),name='producto_detalle' ),
    path('v1/categorias/', CategoriaSave.as_view(),name='categoria_save' ),
    path('v1/subcategorias/', SubCategoriaSave.as_view(),name='subcategoria_save'),
    path('v1/categoriaslist/', CategoriaList.as_view(),name='CategoriaList' ),
    path('v1/subcategoriaslist/', SubCategoriaList.as_view(),name='SubCategoriaList'),
    path('v1/categorias/<int:pk>', CategoriaDetalle.as_view(),name='categoria_list' ),
    path('v1/categorias/<int:pk>/subcategorias/', SubCategoriaList.as_view(),name='categoria_list' ),
    path('v1/categorias/<int:cat_pk>/addsubcategorias/', SubCategoriaAdd.as_view(),name='subcategoria_apiview' ),
    path('v3/usuarios/', UserCreate.as_view(), name='usuario_crear'),
    path("v4/login/", LoginView.as_view(), name="login"),
    path("v3/login-drf/", views.obtain_auth_token, name="login_drf"),#chida url
]
urlpatterns += router.urls