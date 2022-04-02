from django import forms
from django.forms import TextInput

from .models import Aluno, AvaliacaoFisica

class CadastroAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['idu', 'nome', 'email']

class CadastroAvaliacao(forms.ModelForm):
    class Meta:
        model = AvaliacaoFisica
        fields = ['peso', 'altura', 'braco_d', 'perna_e', 'cintura', 'comentario_af']