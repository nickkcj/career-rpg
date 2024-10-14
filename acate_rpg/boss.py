from atributo import Atributo

class Boss:
    def __init__(self, nome, dificuldade, nivel_requerido, ataque, defesa, hp, estamina, diretor=False):
        super().__init__(ataque, defesa, hp, estamina)
        self.__nome = nome
        self.__dificuldade = dificuldade
        self.__nivel_requerido = nivel_requerido
        self.__diretor = diretor
        self.atributos = {
            'ataque': ataque,
            'defesa': defesa,
            'hp': hp,
            'estamina': estamina
        }


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def nivel_requerido(self):
        return self.__nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, nivel_requerido):
        self.__nivel_requerido = nivel_requerido

    @property
    def diretor(self):
        return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos: Atributo):
        self.__atributos = atributos

        