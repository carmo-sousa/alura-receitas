from django.urls import path

from usuarios import views

urlpatterns = [
    path("cadastro", views.cadastro, name="cadastro"),
    path("login", views.LoginView.as_view(), name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
]
