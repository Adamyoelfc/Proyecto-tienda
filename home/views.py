from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from ventas.models import Producto
from home.forms import *
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage, InvalidPage   # paginacion django"

# Create your views here.


def index_view(req):
    return render(req, 'home/home.html')


def about_view(req):
    return render(req, 'home/about.html')


def producto_view(req, pagina):
    lista_prod = Producto.objects.filter(status=True)
    paginator = Paginator(lista_prod, 4)
    try:
        page = int(pagina)
    except:
        page = 1
    try:
        productos = paginator.page(page)
    except:
        productos = paginator.page(paginator.num_pages)
    return render(req, 'home/productos.html', {'productos': productos})


def single_product(req, id_prod):
    prod = Producto.objects.get(id=id_prod)
    cat = prod.caregoria.all()
    return render(req, 'home/single_producto.html', {'producto': prod, 'categorias': cat})


def contacto_view(req):
    info_enviado = False
    email = ''
    titulo = ''
    texto = ''
    if req.method == 'POST':
        formulario = ContactForms(req.POST)
        if formulario.is_valid():
            info_enviado = True
            email = formulario.cleaned_data['Email']
            titulo = formulario.cleaned_data['Titulo']
            texto = formulario.cleaned_data['Texto']
    else:
        formulario = ContactForms()


    return render(req, 'home/contacto.html', {'form': formulario, 'email': email, 'titulo': titulo, 'texto': texto, 'info_enviado': info_enviado})


def login_view(req):
    mensaje = ''
    if req.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        if req.method == 'POST':
            form = LoginForm(req.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                usuario = authenticate(username=username, password=password)
                if usuario is not None and usuario.is_active:
                    login(req, usuario)
                    return HttpResponseRedirect('/')
                else:
                    mensaje = "usuario y/o contraseña incorrecta"

        form = LoginForm
        return render(req, 'home/login.html', {'form': form, 'mensaje': mensaje})


def logout_view(req):
    logout(req)
    return HttpResponseRedirect('/')


def register_view(req):
    form = RegisterForm
    if req.method == "POST":
        form = RegisterForm(req.POST)
        if form.is_valid():
            usuario = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password_1 = form.cleaned_data['password_1']
            password_2 = form.cleaned_data['password_2']
            u = User.objects.create_user(username=usuario, email=email, password=password_1)
            u.save()
            return render(req, 'home/gracias_registrarse.html')
        else:
            form = form

    return render(req, 'home/register.html', {'form': form})