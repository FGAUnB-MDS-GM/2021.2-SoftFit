class Aluno():
    def __init__(self, nome, email, avaliacao, frequencia, estadof, objetivo):
        self.__nome=nome
        self.__email=email
        self.__avaliacao=avaliacao
        self.__frequencia=frequencia
        self.__estadof=estadof
        self.__objetivo=objetivo

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

    @property
    def frequencia(self):
        return self.__frequencia

    @frequencia.setter
    def frequencia(self, frequencia):
        self.__frequencia = frequencia

    @property
    def estadof(self):
        return self.__estadof

    @estadof.setter
    def estadof(self, estadof):
        self.__estadof = estadof

    @property
    def objetivo(self):
        return self.__objetivo

    @objetivo.setter
    def objetivo(self, objetivo):
        self.__objetivo = objetivo