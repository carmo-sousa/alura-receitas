from django.views import View
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from receitas.models import Receita


def cadastro(request):
    if request.method == "POST":
        nome = request.POST["nome"]
        email = request.POST["email"]
        senha = request.POST["password"]
        confirmacao_senha = request.POST["password2"]

        if not nome.strip():
            print("Nome inválido")
            return redirect("cadastro")

        if not email.strip():
            print("E-mail inválido")
            return redirect("cadastro")

        if not senha.strip():
            print("Senha inválida")
            return redirect("cadastro")

        if not confirmacao_senha.strip() and confirmacao_senha.strip() != senha.strip():
            print("Senha de confirmacao está incorreta")
            return redirect("cadastro")

        if User.objects.filter(email=email).exists():
            return redirect("cadastro")

        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()

        return redirect("login")
    return render(request, "usuarios/cadastro.html")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        senha = request.POST["senha"]

        try:
            user = get_object_or_404(User, email=email)
            user = auth.authenticate(request, username=user.username, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
        except Http404:
            messages.add_message(request, messages.ERROR, "Usuário nao encontrado!")
            return redirect(to="login")
    return render(request, "usuarios/login.html")


@login_required(login_url="login")
def dashboard(request):
    receitas = get_list_or_404(Receita, pessoa=request.user.id)
    return render(request, "usuarios/dashboard.html", {"receitas": receitas})


def logout(request):
    if request.user.is_authenticated:
        # Logout
        auth.logout(request)
        return redirect(to="index")
    return redirect(to="index")


class CriaReceita(View):
    def get(self, request):
        return render(request, "usuarios/cria_receita.html")

    def post(self, request):
        return HttpResponse("Receita criada!")
