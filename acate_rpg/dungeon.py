from setor import Setor

class Dungeon(Setor):
    def __init__(self, nome, nivel_requerido, xp_ganho, dificuldade, conquistada=False):
        self._nome = nome
        self._nivel_requerido = nivel_requerido
        self._xp_ganho = xp_ganho
        self._dificuldade = dificuldade
        self._conquistada = conquistada


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nivel_requerido(self):
        return self._nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, nivel_requerido):
        self._nivel_requerido = nivel_requerido

    @property
    def xp_ganho(self):
        return self._xp_ganho

    @xp_ganho.setter
    def xp_ganho(self, xp_ganho):
        self._xp_ganho = xp_ganho

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self._dificuldade = dificuldade

    @property
    def conquistada(self):
        return self._conquistada

    @conquistada.setter
    def conquistada(self, conquistada):
        self._conquistada = conquistada

        