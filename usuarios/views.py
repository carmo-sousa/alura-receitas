from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View

from receitas.models import Receita


# TODO: Trocar todos os prints por messages do django.
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


class LoginView(View):
    def get(self, request):
        return render(request, "usuarios/login.html")

    def post(self, request):
        email: str = request.POST["email"]
        senha: str = request.POST["senha"]

        try:
            user = get_object_or_404(User, email=email)
            user = auth.authenticate(request, username=user.username, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect("dashboard")
            else:
                messages.add_message(
                    request, messages.ERROR, "Usuário ou senha incorretos!"
                )
                return redirect(to="login")
        except Http404:
            messages.add_message(
                request, messages.ERROR, "Usuário ou senha incorretos!"
            )
            return redirect(to="login")


@login_required(login_url="login")
def dashboard(request):
    receitas = Receita.objects.filter(pessoa=request.user.id).order_by("-data_receita")
    paginator = Paginator(receitas, 10)
    page = request.GET.get("page")
    receitas_por_pagina = paginator.get_page(page)
    return render(request, "usuarios/dashboard.html", {"receitas": receitas_por_pagina})


def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
        return redirect(to="index")
    return redirect(to="index")
