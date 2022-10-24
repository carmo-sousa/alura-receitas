from django.contrib.auth.decorators import login_required
from django.urls import path

from receitas import views

app_name = "receitas"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_receita>", views.detalhe, name="detalhe"),
    path("buscar", views.buscar, name="buscar"),
    path(
        "criar",
        login_required(views.CriaReceita.as_view(), login_url="login"),
        name="criar",
    ),
    path(
        "editar/<int:id_receita>",
        login_required(views.EditaReceita.as_view(), "login"),
        name="editar",
    ),
    path(
        "deletar/<int:id_receita>",
        login_required(views.DeletaReceita.as_view(), login_url="login"),
        name="deletar",
    ),
]

handler404 = "receitas.views.error404"
