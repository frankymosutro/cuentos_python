from django.contrib import admin
from .models import Usuario, Ventas, Cuento, Cliente


# Register your models here.
admin.site.register(Usuario)

admin.site.register(Cliente)

admin.site.register(Ventas)

admin.site.register(Cuento)
