from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from ventas.forms import *
from ventas.models import *

# Create your views here.






def add_product_view(req):
    info = ""
    if req.method == "POST":
        form = AddproductForm(req.POST, req.FILES)
        if form.is_valid():
            add = form.save(commit=False)
            add.status = True
            add.save()
            form.save_m2m()
            info = "Guardado satisfactoriamente"
            return HttpResponseRedirect("/productos/" + str(add.id))
    else:
        form = AddproductForm
    return render(req, 'ventas/addProducto.html', {'form': form, 'informacion': info})


# def add_product_view(req):
#     info = "Inicializado"
#     if req.user.is_authenticated:
#         if req.method == 'POST':
#             form = AddproductForm(req.POST, req.FILES)
#             if form.is_valid():
#                 nombre = form.cleaned_data['nombre']
#                 descripcion = form.cleaned_data['descripcion']
#                 imagen = form.cleaned_data['imagen']
#                 precio = form.cleaned_data['precio']
#                 stock = form.cleaned_data['stock']
#                 p = Producto()
#                 if imagen:
#                     p.imagen = imagen
#                 p.nombre = nombre
#                 p.descripcion = descripcion
#                 p.precio = precio
#                 p.stock = stock
#                 p.status = True
#                 p.save()
#                 info = "Se guardo la informacion"
#             else:
#                 info = "informacion con datos incorrectos"
#             form = AddproductForm()
#             return render(req, 'ventas/addProducto.html', {'form': form, 'informacion': info})
#         else:
#             form = AddproductForm()
#         return render(req, 'ventas/addProducto.html', {'form': form})
#     else:
#         return HttpResponseRedirect('/')


# def edit_produc(req, id_prod):
#     p = Producto.objects.get(id=id_prod)
#     if req.method == "POST":
#         form = AddproductForm(req.POST, req.FILES)
#         if form.is_valid():
#             nombre = form.cleaned_data["nombre"]
#             descripcion = form.cleaned_data["descripcion"]
#             imagen = form.cleaned_data["imagen"]
#             precio = form.cleaned_data["precio"]
#             stock = form.cleaned_data["stock"]
#             p.nombre = nombre
#             p.descripcion = descripcion
#             p.imagen = imagen
#             p.precio = precio
#             p.stock = stock
#             if imagen:
#                 p.imagen = imagen
#             p.save()
#             return HttpResponseRedirect('/productos/' + str(p.id))
#     if req.method == "GET":
#         form = AddproductForm(initial={
#             'nombre': p.nombre,
#             'descripcion': p.descripcion,
#             'precio': p.precio,
#             'stock': p.stock,
#         })
#
#     return render(req, 'ventas/edit_product.html', {'form': form, 'producto': p})


def edit_produc(req, id_prod):
    info = ""
    prod = Producto.objects.get(pk=id_prod)
    if req.method == "POST":
        form = AddproductForm(req.POST, req.FILES, instance=prod)
        if form.is_valid():
            edit_prod = form.save(commit=False)
            form.save_m2m()
            edit_prod.status = True
            edit_prod.save()
            info = "Correcto"
            return HttpResponseRedirect('/productos/' + str(edit_prod.id))
    else:
        form = AddproductForm(instance=prod)
    return render(req, 'ventas/edit_product.html', {'informacion': info, 'form': form, 'producto': prod})