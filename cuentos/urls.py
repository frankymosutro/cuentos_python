from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path("/accounts/signup/", allauth.account.views.SignupView(template_name="registration/login.html"), name="account_signup"),
    # path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("contacto/", views.nuevo_contacto, name="nuevo_contacto"),
    path("crear/cuento/", views.crea_cuento, name="crea_cuento"),
    path("crear/cuento/preview/", views.crea_cuento, name="cuento_preview"),
]