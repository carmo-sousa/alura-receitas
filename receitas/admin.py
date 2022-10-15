from typing import Sequence

from django.contrib import admin

from receitas.models import Classe, Receita


class AdminReceitas(admin.ModelAdmin):
    search_fields: Sequence[str] = ("nome_receita",)
    list_filter = ("categoria",)
    list_per_page: int = 25


admin.site.register(Receita, AdminReceitas)
admin.site.register(Classe)
