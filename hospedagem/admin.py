from django.contrib import admin

# Register your models here.

from .models import Cliente,Quarto,Consumo, Hospedagem


@admin.register(Cliente)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('get_nome', 'telefone', 'email', 'endereco')

    def get_nome(self, obj):
        return obj.nome
    get_nome.short_description = 'Nome'

@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display=('apartamento', 'valor')

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display=('nome', 'data', 'valor', 'hospedagem')

@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'quarto', 'data_entrada', 'data_saida')

