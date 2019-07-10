from django.shortcuts import render, redirect
from django.conf import settings
import yagmail

# Create your views here.
def gmail(request):
    """ Atendiendo la petición POST /gmail """

    if "contacto" in request.POST:
        body = "Nombre: {}\n".format(request.POST["name"])
        body += "Email: {}\n".format(request.POST["email"])
        body += "Tel: {}\n".format(request.POST["tel"])
        body += "Mensaje:\n\n{}\n".format(request.POST["message"])
        nexturl = request.POST.get("next", "/")
        yag = yagmail.SMTP(
            user=settings.EMAIL_HOST_USER,
            password=settings.EMAIL_HOST_PASSWORD
        )
        yag.send(
            to="rictor@cuhrt.com",
            subject="Club de cuentos - Contacto",
            contents=body
        )

    return redirect(nexturl)


