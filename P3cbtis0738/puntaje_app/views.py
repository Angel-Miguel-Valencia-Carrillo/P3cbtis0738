from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")

def clientes(request):
    return render(request,"clientes.html")

def empleado(request):
    return render(request,"empleado.html")

def bebidas(request):
    return render(request,"bebidas.html")

def Provedores(request):
    return render(request,"provedores.html")