from django.urls import path
from ventas.views import *

urlpatterns = [
    path('add_product/', add_product_view, name='agregar_prod'),
    path('producto/editar/<int:id_prod>/', edit_produc, name='editar_prod'),
]