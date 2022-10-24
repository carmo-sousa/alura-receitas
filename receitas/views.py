from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from receitas.models import Categoria, Receita


def index(request):
    receitas = Receita.objects.order_by("-data_receita").filter(publicada=True)
    paginator = Paginator(receitas, 10)
    page = request.GET.get("page")
    receitas_por_pagina = paginator.get_page(page)

    return render(request, "index.html", {"receitas": receitas_por_pagina})


def detalhe(request, id_receita):
    receita = get_object_or_404(Receita, pk=id_receita)
    return render(request, "receitas/receita.html", {"receita": receita})


def buscar(request):
    pesquisa = request.GET["buscar"] or None

    if pesquisa:
        receitas = Receita.objects.filter(nome_receita__icontains=pesquisa)
    return render(request, "buscar.html", {"receitas": receitas})


class CriaReceita(View):
    def get(self, request):
        categorias = Categoria.objects.all()
        return render(request, "receitas/criar.html", {"categorias": categorias})

    def post(self, request):
        nome_receita = request.POST["nome_receita"]
        ingredientes = request.POST["ingredientes"]
        modo_preparo = request.POST["modo_preparo"]
        tempo_preparo = request.POST["tempo_preparo"]
        rendimento = request.POST["rendimento"]
        categoria_id = request.POST["categoria"]
        foto_receita = request.FILES["foto_receita"]

        categoria = Categoria.objects.get(id=categoria_id)

        receita = Receita(
            nome_receita=nome_receita,
            ingredientes=ingredientes,
            modo_preparo=modo_preparo,
            tempo_preparo=tempo_preparo,
            rendimento=rendimento,
            categoria=categoria,
            foto_receita=foto_receita,
            pessoa=request.user,
        )
        receita.save()
        return redirect("dashboard")


class EditaReceita(View):
    def get(self, request, id_receita):
        receita = get_object_or_404(Receita, pk=id_receita)
        categorias = Categoria.objects.all()
        return render(
            request,
            "receitas/editar.html",
            {"receita": receita, "categorias": categorias},
        )

    def post(self, request, id_receita):
        nome_receita = request.POST["nome_receita"]
        ingredientes = request.POST["ingredientes"]
        modo_preparo = request.POST["modo_preparo"]
        tempo_preparo = request.POST["tempo_preparo"]
        rendimento = request.POST["rendimento"]
        categoria = request.POST["categoria"]

        receita = get_object_or_404(Receita, pk=id_receita)

        receita.nome_receita = nome_receita
        receita.ingredientes = ingredientes
        receita.modo_preparo = modo_preparo
        receita.tempo_preparo = tempo_preparo
        receita.rendimento = rendimento
        receita.categoria = categoria
        if "foto_receita" in request.FILES:
            receita.foto_receita = request.FILES["foto_receita"]
        receita.save()

        messages.success(request, f"Receita {id_receita} editada com sucesso!")
        return redirect(to="dashboard")


# TODO: Modificar o HTML para que ele mostre um modal com uma confirmação antes de deletar a receita.
class DeletaReceita(View):
    def get(self, request, id_receita):
        receita = get_object_or_404(Receita, pk=id_receita)

        if request.user == receita.pessoa:
            receita.delete()
            messages.success(request, "Receita deletada!")
            return redirect(to="dashboard")
        else:
            messages.error(request, "Nao foi possível deletar a receita")
            redirect(to="dashboard")


def error404(request, exception):
    return render(request, "404.html")
