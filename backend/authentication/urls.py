from rest_framework import urlpatterns
from . import views
from django.urls import path

urlpatterns = [path("login/", views.LoginView.as_view(), name="login")]
