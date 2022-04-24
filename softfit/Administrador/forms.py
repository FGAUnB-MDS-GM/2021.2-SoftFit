from django import forms
from django.forms import TextInput

from .models import Aluno, AvaliacaoFisica, Professor, Objetivo

class CadastroAluno(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        for aluno in Aluno.objects.all():
            if aluno.email == email:
                raise forms.ValidationError('Aluno ou Professor já cadastrado com esse e-mail.')
        for prof in Professor.objects.all():
            if prof.email == email:
                raise forms.ValidationError('Aluno ou Professor já cadastrado com esse e-mail.')
        
        return email

class CadastroAvaliacao(forms.ModelForm):
    class Meta:
        model = AvaliacaoFisica
        fields = ['peso', 'altura', 'braco_d', 'perna_e', 'cintura', 'comentario_af']

class CadastroProfessor(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['nome', 'email',
                'segunda_manha', 'segunda_tarde', 'segunda_noite',
                'terca_manha', 'terca_tarde', 'terca_noite',
                'quarta_manha', 'quarta_tarde', 'quarta_noite',
                'quinta_manha', 'quinta_tarde', 'quinta_noite',
                'sexta_manha', 'sexta_tarde', 'sexta_noite',
                'sabado_manha', 'sabado_tarde',
                'domingo_manha']
                
    def clean_email(self):
        email = self.cleaned_data.get('email')

        for aluno in Aluno.objects.all():
            if aluno.email == email:
                raise forms.ValidationError('Aluno ou Professor já cadastrado com esse e-mail.')
        for prof in Professor.objects.all():
            if prof.email == email:
                raise forms.ValidationError('Aluno ou Professor já cadastrado com esse e-mail.')
        
        return email

class CadastroObjetivo(forms.ModelForm):
    class Meta:
        model = Objetivo
        fields = ['opcao', 'comentario']

class Mensagem(forms.Form):

    def __init__(self, nome, assunto_email, *args,**kwargs):
        super(Mensagem,self).__init__(*args,**kwargs)
        self.fields['corpo_email'].widget = forms.Textarea(attrs={'placeholder': 'Mensagem E-mail', 'rows': 7})
        if assunto_email == 'Estado Financeiro':
            self.fields['corpo_email'].initial='Olá '+ nome + ',\n\nA academia SoftFit está te enviando esse e-mail para te informar acerca de seu Estado Financeiro.\nPercebemos que sua condição está como inadimplente, contamos com o seu pagamento. Caso esteja com algum problema, estamos à disposição para ajudar.\n\nAtenciosamente,\n           Administração SoftFit.'
        else:
            self.fields['corpo_email'].initial='Olá '+ nome + ',\n\nPrezamos por entregar sempre a melhor experiência para os nossos alunos.\nNotamos que você vem sendo ausente nos treinos ultimamente, aconteceu algo? Estamos à disposição para ouvir feedbacks e melhorar no que possível. \n\nAtenciosamente,\n           Administração SoftFit.'
    
    corpo_email = forms.CharField(label='Mensagem', max_length=1500)