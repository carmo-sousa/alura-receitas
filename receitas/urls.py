from django.urls import path

from receitas import views

urlpatterns = [
    path("", views.index, name="index"),
    path("receitas/", views.receitas, name="receita"),
]
