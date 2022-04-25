from django import forms
from django.forms import TextInput

from Administrador.models import Exercicio

class CadastroExercicio(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['serie', 'qntd_serie', 'repeticao', 'carga', 'descanso', 'comentario_ex']