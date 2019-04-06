from django.contrib import admin
from .models import Atendimento
from .models import Categoria
from .models import Chamado
from .models import Funcionario

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    pass
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    pass
@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    pass
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    pass