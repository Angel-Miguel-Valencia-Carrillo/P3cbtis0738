from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name="index"),
    path("clientes/",views.clientes,name="clientes"),
    path("empleado/",views.empleado,name="empleado"),
    path("bebidas/",views.bebidas,name="bebidas"),
    path("provedores/",views.Provedores,name="provedores"),
]

