from django.contrib import admin

from .models import Aluno, AvaliacaoFisica, Professor, EstadoFinanceiro

# Register your models here.

admin.site.register(Aluno)
admin.site.register(AvaliacaoFisica)
admin.site.register(Professor)
admin.site.register(EstadoFinanceiro)