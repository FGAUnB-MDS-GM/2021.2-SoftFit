class Aluno():
    def __init__(self, idu, nome, email, avaliacao):
        self.__idu=idu
        self.__nome=nome
        self.__email=email
        self.__avaliacao = avaliacao

    @property
    def idu(self):
        return self.__idu

    @idu.setter
    def idu(self, idu):
        self.__idu = idu

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def avaliacao(self):
        return self.__avaliacao

    @avaliacao.setter
    def avaliacao(self, avaliacao):
        self.__avaliacao = avaliacao