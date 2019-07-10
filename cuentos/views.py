# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
# from allauth.account.views import *
# from allauth.account.forms import LoginForm, SignupForm



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

# def account_signup(request):
#      """ Vista para atender la petición de la url / """
#      return render(request, "account/signup.html") 
# class MyCustomSignupForm ( SignupForm ):
#      def save ( self , request ):

#         # Ensure you call the parent class's save.
#         # .save() returns a User object.
#         user = super ( MyCustomSignupForm , self ) . save ( request )

#         # Add your own processing here.

#         # You must return the original result.
#         return user

  
