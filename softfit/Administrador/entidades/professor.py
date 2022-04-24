class Professor():
    def __init__(self, nome, email, segunda_manha, segunda_tarde, segunda_noite, terca_manha, terca_tarde, terca_noite, quarta_manha, quarta_tarde, quarta_noite, quinta_manha, quinta_tarde, quinta_noite, sexta_manha, sexta_tarde, sexta_noite, sabado_manha, sabado_tarde, domingo_manha):
        self.__nome=nome
        self.__email=email

        self.__segunda_manha = segunda_manha
        self.__segunda_tarde = segunda_tarde
        self.__segunda_noite = segunda_noite

        self.__terca_manha = terca_manha
        self.__terca_tarde = terca_tarde
        self.__terca_noite = terca_noite

        self.__quarta_manha = quarta_manha
        self.__quarta_tarde = quarta_tarde
        self.__quarta_noite = quarta_noite

        self.__quinta_manha = quinta_manha
        self.__quinta_tarde = quinta_tarde
        self.__quinta_noite = quinta_noite

        self.__sexta_manha = sexta_manha
        self.__sexta_tarde = sexta_tarde
        self.__sexta_noite = sexta_noite

        self.__sabado_manha = sabado_manha
        self.__sabado_tarde = sabado_tarde

        self.__domingo_manha = domingo_manha

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

    # Segunda
    @property
    def segunda_manha(self):
        return self.__segunda_manha

    @segunda_manha.setter
    def segunda_manha(self, segunda_manha):
        self.__segunda_manha = segunda_manha

    @property
    def segunda_tarde(self):
        return self.__segunda_tarde

    @segunda_tarde.setter
    def segunda_tarde(self, segunda_tarde):
        self.__segunda_tarde = segunda_tarde

    @property
    def segunda_noite(self):
        return self.__segunda_noite

    @segunda_noite.setter
    def segunda_noite(self, segunda_noite):
        self.__segunda_noite = segunda_noite

    # Terça
    @property
    def terca_manha(self):
        return self.__terca_manha

    @terca_manha.setter
    def terca_manha(self, terca_manha):
        self.__terca_manha = terca_manha

    @property
    def terca_tarde(self):
        return self.__terca_tarde

    @terca_tarde.setter
    def terca_tarde(self, terca_tarde):
        self.__terca_tarde = terca_tarde

    @property
    def terca_noite(self):
        return self.__terca_noite

    @terca_noite.setter
    def terca_noite(self, terca_noite):
        self.__terca_noite = terca_noite

    # Quarta
    @property
    def quarta_manha(self):
        return self.__quarta_manha

    @quarta_manha.setter
    def quarta_manha(self, quarta_manha):
        self.__quarta_manha = quarta_manha

    @property
    def quarta_tarde(self):
        return self.__quarta_tarde

    @quarta_tarde.setter
    def quarta_tarde(self, quarta_tarde):
        self.__quarta_tarde = quarta_tarde

    @property
    def quarta_noite(self):
        return self.__quarta_noite

    @quarta_noite.setter
    def quarta_noite(self, quarta_noite):
        self.__quarta_noite = quarta_noite

    # Quinta
    @property
    def quinta_manha(self):
        return self.__quinta_manha

    @quinta_manha.setter
    def quinta_manha(self, quinta_manha):
        self.__quinta_manha = quinta_manha

    @property
    def quinta_tarde(self):
        return self.__quinta_tarde

    @quinta_tarde.setter
    def quinta_tarde(self, quinta_tarde):
        self.__quinta_tarde = quinta_tarde

    @property
    def quinta_noite(self):
        return self.__quinta_noite

    @quinta_noite.setter
    def quinta_noite(self, quinta_noite):
        self.__quinta_noite = quinta_noite

    # Sexta
    @property
    def sexta_manha(self):
        return self.__sexta_manha

    @sexta_manha.setter
    def sexta_manha(self, sexta_manha):
        self.__sexta_manha = sexta_manha

    @property
    def sexta_tarde(self):
        return self.__sexta_tarde

    @sexta_tarde.setter
    def sexta_tarde(self, sexta_tarde):
        self.__sexta_tarde = sexta_tarde

    @property
    def sexta_noite(self):
        return self.__sexta_noite

    @sexta_noite.setter
    def sexta_noite(self, sexta_noite):
        self.__sexta_noite = sexta_noite

    # Sábado
    @property
    def sabado_manha(self):
        return self.__sabado_manha

    @sabado_manha.setter
    def sabado_manha(self, sabado_manha):
        self.__sabado_manha = sabado_manha

    @property
    def sabado_tarde(self):
        return self.__sabado_tarde

    @sabado_tarde.setter
    def sabado_tarde(self, sabado_tarde):
        self.__sabado_tarde = sabado_tarde

    # Domingo
    @property
    def domingo_manha(self):
        return self.__domingo_manha

    @domingo_manha.setter
    def domingo_manha(self, domingo_manha):
        self.__domingo_manha = domingo_manha