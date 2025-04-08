

class Curso():
    def __init__(self, nome, nivel_requerido, xp_ganho, setor, dificuldade, realizado=False):
        self.__nome = nome
        self.__nivel_requerido = nivel_requerido
        self.__xp_ganho = xp_ganho
        self.__setor = setor
        self.__dificuldade = dificuldade
        self.__realizado = realizado
 


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nivel_requerido(self):
        return self.__nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, nivel_requerido):
        self.__nivel_requerido = nivel_requerido

    @property
    def xp_ganho(self):
        return self.__xp_ganho

    @xp_ganho.setter
    def xp_ganho(self, xp_ganho):
        self.__xp_ganho = xp_ganho

    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def realizado(self):
        return self.__realizado

    @realizado.setter
    def realizado(self, realizado):
        self.__realizado = realizado

    