from django.contrib import admin

from pessoas.models import Pessoa


class AdminPessoa(admin.ModelAdmin):
    search_fields: tuple[str] = ("email",)
    list_per_page: int = 25


admin.site.register(Pessoa, AdminPessoa)
