from django.shortcuts import render
from receitas.models import Receita


# Create your views here.
def index(request):
    receitas = Receita.objects.all()
    return render(request, "index.html", {"receitas": receitas})


def receitas(request):
    return render(request, "receita.html")
