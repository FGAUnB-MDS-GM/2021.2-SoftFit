from django import forms
from django.forms import TextInput

from Administrador.models import Exercicio, Treino

class CadastroExercicio(forms.ModelForm):
    class Meta:
        model = Exercicio
        fields = ['serie', 'qntd_serie', 'carga', 'descanso', 'comentario_ex']

class CadastroTreino(forms.Form):
    treino = forms.ChoiceField(choices=[(treino.id, treino.descricao) for treino in Treino.objects.all()], widget=forms.Select(attrs={'class':'form-control'}))