from django.urls import path, include
from .views import authView, home
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", home, name="home"),
    path("signup/", authView, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),

]

