from django.contrib import admin

from .models import Aluno, AvaliacaoFisica, Professor, EstadoFinanceiro, Objetivo

# Register your models here.

admin.site.register(Aluno)
admin.site.register(AvaliacaoFisica)
admin.site.register(Professor)
admin.site.register(EstadoFinanceiro)
admin.site.register(Objetivo)