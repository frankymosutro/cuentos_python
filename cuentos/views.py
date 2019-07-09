from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    """ Vista para atender la petición de la url / """
    return render(request, "cuentos/index.html")

def nuevo_contacto(request):
    """ Vista para atender la petción de la url contacto """
    return render(request, "cuentos/contacto.html")

def crea_cuento(request):
    """ Vista para atender la petción de la url contacto """
    return render(request, "cuentos/cuento.html")

def registro(request):
    """ Vista para atender la petición de la url / """
    return render(request, "registration/registro.html")  

  
