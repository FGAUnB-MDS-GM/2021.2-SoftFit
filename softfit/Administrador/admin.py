from django.contrib import admin

from .models import Aluno, AvaliacaoFisica, Professor, EstadoFinanceiro, Objetivo, Exercicio, Treino

# Register your models here.

admin.site.register(Aluno)
admin.site.register(AvaliacaoFisica)
admin.site.register(Professor)
admin.site.register(EstadoFinanceiro)
admin.site.register(Objetivo)
admin.site.register(Exercicio)
admin.site.register(Treino)