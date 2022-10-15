from django.shortcuts import get_object_or_404, render

from receitas.models import Receita


# Create your views here.
def index(request):
    receitas = Receita.objects.all()
    return render(request, "index.html", {"receitas": receitas})


def receitas(request, id_receita):
    receita = get_object_or_404(Receita, pk=id_receita)
    return render(request, "receita.html", {"receita": receita})
