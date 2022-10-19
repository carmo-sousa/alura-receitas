from django.urls import path

from usuarios import views

urlpatterns = [
    path("cadastro", views.cadastro, name="cadastro"),
    path("login", views.login, name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
    path("usuario/cria-receita", views.CriaReceita.as_view(), name="cria.receita"),
]