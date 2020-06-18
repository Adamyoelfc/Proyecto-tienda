from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from ventas.models import Producto
#importar serialisacion
from django.core import serializers


# Create your views here.


def ws_prod_view(req):
    data = serializers.serialize("json", Producto.objects.filter(status=True))
    #retorna la informacion en formato json
    return HttpResponse(data, content_type="application/json")