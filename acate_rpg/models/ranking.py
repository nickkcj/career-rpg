from personagem import Personagem

class Ranking:
    def __init__(self, tipo: str):
        self.__tipo = tipo
        self.__personagens = []

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @property
    def personagens(self):
        return self.__personagens

    @personagens.setter
    def personagens(self, personagens: list):
        self.__personagens = personagens
    