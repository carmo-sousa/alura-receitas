from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from receitas.models import Receita


# Create your views here.
def index(request):
    receitas = Receita.objects.order_by("-data_receita").filter(publicada=True)
    paginator = Paginator(receitas, 10)
    page = request.GET.get("page")
    receitas_por_pagina = paginator.get_page(page)

    return render(request, "index.html", {"receitas": receitas_por_pagina})


def receitas(request, id_receita):
    receita = get_object_or_404(Receita, pk=id_receita)
    return render(request, "receita.html", {"receita": receita})


def buscar(request):
    pesquisa = request.GET["buscar"] or None

    if pesquisa:
        receitas = Receita.objects.filter(nome_receita__icontains=pesquisa)
    return render(request, "buscar.html", {"receitas": receitas})


def error404(request, exception):
    return render(request, "404.html")
