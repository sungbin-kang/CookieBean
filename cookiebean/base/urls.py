from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("account/signup/", views.SingUp.as_view(), name="signup"),
    path("account/", include("django.contrib.auth.urls"), name="login"),
    path("account/logout/", views.logout_request, name="logout"),
]
