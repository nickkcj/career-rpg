class Setor:
    def __init__(self, nome, dificuldade):
        self._nome = nome
        self._dificuldade = dificuldade


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self._dificuldade = dificuldade