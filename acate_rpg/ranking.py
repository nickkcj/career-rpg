class Ranking:
    def __init__(self, tipo):
        self._tipo = tipo
        self._personagens = []


    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def adicionar_personagem(self, personagem):
        self._personagens.append(personagem)

    def remover_personagem(self, personagem):
        self._personagens.remove(personagem)

    def ranking_nivel(self):
        pass

    def ranking_dungeons(self):
        pass

    def ranking_cursos(self):
        pass