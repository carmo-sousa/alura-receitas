from django.contrib.auth.decorators import login_required
from django.urls import path

from usuarios import views

urlpatterns = [
    path("cadastro", views.cadastro, name="cadastro"),
    path("login", views.LoginView.as_view(), name="login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("logout", views.logout, name="logout"),
    path(
        "usuario/cria-receita",
        login_required(views.CriaReceita.as_view(), login_url="login"),
        name="cria.receita",
    ),
    path(
        "deleta/<int:id_receita>",
        login_required(views.DeletaReceita.as_view(), login_url="login"),
        name="deleta",
    ),
    path(
        "edita/<int:id_receita>",
        login_required(views.EditaReceita.as_view(), "login"),
        name="editar",
    ),
]
