
class Sistema:
    def __init__(self):
        self.__personagens = []

    @property
    def personagens(self):
        return self.__personagens

    def adicionar_personagem(self, personagem):
        self.__personagens.append(personagem)

    def listar_personagens(self):
        return self.__personagens