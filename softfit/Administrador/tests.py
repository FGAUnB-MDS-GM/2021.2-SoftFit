from django.test import TestCase
from .models import Usuario, Professor, AvaliacaoFisica, Aluno, Objetivo, EstadoFinanceiro
from .services import prof_service
from django.core.mail import send_mail
from calendar import monthrange
from datetime import date

# Create your tests here.

# H19 - Cadastrar Professores
class ProfessorTestCase(TestCase):
    def setUp(self):
        # O administrador deverá cadastrar o nome do professor para fins de identificação (Teste dá Fail caso não tenha nome).
        # A rotina do professor deve ser preenchida de acordo com os horários de trabalho realizados por ele na academia.
        # O administrador deverá cadastrar o e-mail do professor (válido), para que este receba sua senha e faça login. (O formulário faz esse trabalho, juntamente com o models)
        Professor.objects.create(nome="Marcos", email="softfit123@gmail.com", 
                                    segunda_manha=1, segunda_tarde=1, segunda_noite=1, 
                                    terca_manha=0, terca_tarde=0, terca_noite=0, 
                                    quarta_manha=1, quarta_tarde=1, quarta_noite=1, 
                                    quinta_manha=0, quinta_tarde=0, quinta_noite=0, 
                                    sexta_manha=1, sexta_tarde=1, sexta_noite=1, 
                                    sabado_manha=0, sabado_tarde=0, 
                                    domingo_manha=1)

    def test_cadastro_prof(self):
        marcos = Professor.objects.get(nome="Marcos")
        # O professor receberá um ID de identificação automático.
        self.assertEqual(marcos.id, 1)
        # O professor deve receber a sua senha inicial no e-mail cadastrado.
        corpo_email = "Professor, sua senha provisória de acesso é: " + "senha"
        email_enviado = send_mail('Senha de Acesso - SoftFit', corpo_email, 'softfit123@gmail.com', [marcos.email], fail_silently=False)
        self.assertEqual(email_enviado, 1)

# H18 - Cadastrar Alunos
class AlunoTestCase(TestCase):
    def setUp(self):
        # A avaliação física inicial do aluno deverá ser preenchida: As medidas de peso, altura, braço, coxa, cintura deverão aceitar apenas números maiores que 0. (O formulário valida por si próprio)
        avaliacao = AvaliacaoFisica.objects.create(peso=-10, altura=10, imc=0, braco_d=40, perna_e=80, cintura=120, 
                                                    comentario_af="nenhum")
        objetivo = Objetivo.objects.create(opcao="A Selecionar", comentario="Nenhum, por enquanto")
        estadof = EstadoFinanceiro.objects.create(condicao="Em Dia")
        # O administrador deverá cadastrar o nome do aluno para fins de identificação. (Teste dá Fail caso não tenha nome).
        # O administrador deverá cadastrar o e-mail do aluno (válido), para que este receba sua senha e faça login.
        Aluno.objects.create(nome="Victor", email="victor.pessoal1203@gmail.com", 
                                avaliacao=avaliacao, frequencia=0, objetivo=objetivo, estadof=estadof)
        Aluno.objects.create(nome="Luan", email="luan@gmail.com", 
                                avaliacao=avaliacao, frequencia=10, objetivo=objetivo, estadof=estadof)

    def test_cadastro_aluno(self):
        victor = Aluno.objects.get(nome="Victor")
        # O aluno receberá um ID de identificação automático.
        self.assertEqual(victor.id, 1)
        # A princípio, todos os alunos terão estado financeiro igual a "Em dia". - H18
        # H02 - Consultar Estado Financeiro
        # Essa consulta deverá ocorrer na listagem dos alunos.
        # Deverá ser exibida "Em dia" ou "Inadimplente", dependendo da condição do aluno.
        self.assertEqual(victor.estadof.condicao, "Em Dia")
        # A princípio, todos os alunos terão a frequência de 0 dias.
        self.assertEqual(victor.frequencia, 0)
        # O aluno deve receber a sua senha inicial no e-mail cadastrado.
        corpo_email = "Professor, sua senha provisória de acesso é: " + "senha"
        email_enviado = send_mail('Senha de Acesso - SoftFit', corpo_email, 'softfit123@gmail.com', [victor.email], fail_silently=False)
        self.assertEqual(email_enviado, 1)

    # H05 - Consultar Frequência
    # A frequência é mostrada como: dias_idos/dias_mês. Por exemplo, se o aluno foi 10 dias da academia no mês de março (31 dias), a frequência seria mostrada como 10/31.
    def test_frequencia(self):
        victor = Aluno.objects.get(nome="Victor")
        luan = Aluno.objects.get(nome="Luan")
        dia_mes = monthrange(date.today().year, date.today().month)[1]
        frequencia_victor = str(victor.frequencia) + "/" + str(dia_mes)
        frequencia_luan = str(luan.frequencia) + "/" + str(dia_mes)
        self.assertEqual(frequencia_victor, "0/30")
        self.assertEqual(frequencia_luan, "10/30")

    # H06 - Enviar Mensagens
    def test_message(self):
        victor = Aluno.objects.get(nome="Victor")
        # A mensagem deverá ser enviada por e-mail.
        email = victor.email
        assunto = 1
        # A mensagem deve ser personalizada em Assunto e Nome do Aluno.
        # A mensagem pode ser relacionada ao Estado Financeiro ou a Frequência do aluno.
        # A mensagem terá um formato pré-definido, mas que poderá ser alterada pelo administrador.
        if assunto == 1:
            assunto_email = 'Estado Financeiro'
            corpo_email = 'Olá '+ victor.nome + ',\n\nA academia SoftFit está te enviando esse e-mail para te informar acerca de seu Estado Financeiro.\nPercebemos que sua condição está como inadimplente, contamos com o seu pagamento. Caso esteja com algum problema, estamos à disposição para ajudar.\n\nAtenciosamente,\n           Administração SoftFit.'
        else:
            assunto_email = 'Frequência'
            corpo_email = 'Olá '+ victor.nome + ',\n\nPrezamos por entregar sempre a melhor experiência para os nossos alunos.\nNotamos que você vem sendo ausente nos treinos ultimamente, aconteceu algo? Estamos à disposição para ouvir feedbacks e melhorar no que possível. \n\nAtenciosamente,\n           Administração SoftFit.'
            
        email_enviado = send_mail(assunto_email, corpo_email, 'softfit123@gmail.com', [email], fail_silently=False)
        self.assertEqual(email_enviado, 1)