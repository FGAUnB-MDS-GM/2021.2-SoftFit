class Professor():
    def __init__(self, idu, nome, email, rotina):
        self.__idu=idu
        self.__nome=nome
        self.__email=email
        self.__rotina = rotina

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
    def rotina(self):
        return self.__rotina

    @rotina.setter
    def rotina(self, rotina):
        self.__rotina = rotina