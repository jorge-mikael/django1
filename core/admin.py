from django.contrib import admin
from .models import Produto, Cliente

# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    search_fields = ('nome',)


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    search_fields = ('nome', 'sobrenome', 'email')
    list_filter = ('sobrenome',)
    ordering = ('sobrenome',)
    list_per_page = 10
    list_editable = ('sobrenome',)
    list_display_links = ('nome',)

admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)