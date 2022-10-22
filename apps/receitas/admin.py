from django.contrib import admin

from receitas.models import Classe, Receita


class AdminReceitas(admin.ModelAdmin):
    list_display = ("nome_receita", "publicada")
    list_editable = ("publicada",)
    search_fields = ("nome_receita", "categoria")
    list_filter = ("categoria",)
    list_per_page: int = 25


admin.site.register(Receita, AdminReceitas)
admin.site.register(Classe)
