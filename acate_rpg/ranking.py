from personagem import Personagem

class Ranking(Personagem):
    def __init__(self, tipo, id, personagem:Personagem):
        self.__tipo = tipo
        self.__id = id
        self.__personagens = list[personagem] ## sabemos que não é assim!


    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def personagens(self):
        return self.__personagens

    @personagens.setter
    def personagens(self, personagens):
        self.__personagens = personagens

    def adicionar_personagem(self, personagem):
        self.__personagens.append(personagem)

    def remover_personagem(self, personagem):
        self.__personagens.remove(personagem)

    def ranking_nivel(self):
        pass

    def ranking_dungeons(self):
        pass

    def ranking_cursos(self):
        pass

    