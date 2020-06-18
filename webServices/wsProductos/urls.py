from django.urls import path
from webServices.wsProductos.views import *

urlpatterns = [
    path('ws_productos/', ws_prod_view, name='ws_productos_url'),
]