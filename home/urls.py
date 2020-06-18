from django.urls import path
from home.views import *


urlpatterns = [
    path('', index_view, name='vista_principal'),
    path('about/', about_view, name='vista_about'),
    path('contacto/', contacto_view, name='vista_contacto'),
    path('productos/page/<int:pagina>', producto_view, name='vista_productos'),
    path('productos/<int:id_prod>/', single_product, name='single_prod'),
    path('login/', login_view, name='vista_login'),
    path('logout/', logout_view, name='vista_logout'),
    path('register/', register_view, name='register_view'),
]