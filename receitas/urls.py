from django.urls import path

from receitas import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id_receita>", views.receitas, name="receita"),
    path("buscar", views.buscar, name="buscar"),
]

handler404 = "receitas.views.error404"
