from django import forms
from django.forms import TextInput

from .models import Aluno, AvaliacaoFisica, Professor, Objetivo

class CadastroAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['idu', 'nome', 'email']

class CadastroAvaliacao(forms.ModelForm):
    class Meta:
        model = AvaliacaoFisica
        fields = ['peso', 'altura', 'braco_d', 'perna_e', 'cintura', 'comentario_af']

class CadastroProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['idu', 'nome', 'email',
                'segunda_manha', 'segunda_tarde', 'segunda_noite',
                'terca_manha', 'terca_tarde', 'terca_noite',
                'quarta_manha', 'quarta_tarde', 'quarta_noite',
                'quinta_manha', 'quinta_tarde', 'quinta_noite',
                'sexta_manha', 'sexta_tarde', 'sexta_noite',
                'sabado_manha', 'sabado_tarde',
                'domingo_manha']

class CadastroObjetivo(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = ['opcao', 'comentario']