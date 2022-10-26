from django.contrib.auth.decorators import login_required
from django.urls import path

from receitas import views

app_name = "receitas"
urlpatterns = [
    path("", views.index, name="index"),
    path("receitas/<int:id_receita>", views.detalhe, name="detalhe"),
    path("receitas/buscar", views.buscar, name="buscar"),
    path(
        "receitas/criar",
        login_required(views.CriaReceita.as_view(), login_url="login"),
        name="criar",
    ),
    path(
        "receitas/editar/<int:id_receita>",
        login_required(views.EditaReceita.as_view(), "login"),
        name="editar",
    ),
    path(
        "receitas/deletar/<int:id_receita>",
        login_required(views.DeletaReceita.as_view(), login_url="login"),
        name="deletar",
    ),
]

handler404 = "receitas.views.error404"
