from setor import Setor

class Dungeon:
    def __init__(self, nome, nivel_requerido, xp_ganho, dificuldade, setores, boss_final, conquistada=False):
        self._nome = nome
        self._nivel_requerido = nivel_requerido
        self._xp_ganho = xp_ganho
        self._dificuldade = dificuldade
        self._setores = setores
        self._boss_final = boss_final
        self._conquistada = conquistada

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        if not value.strip():
            raise ValueError("O nome não pode ser vazio.")
        self._nome = value

    @property
    def nivel_requerido(self):
        return self._nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Nível requerido deve ser um número inteiro não negativo.")
        self._nivel_requerido = value

    @property
    def xp_ganho(self):
        return self._xp_ganho

    @xp_ganho.setter
    def xp_ganho(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("XP ganho deve ser um número inteiro não negativo.")
        self._xp_ganho = value

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, value):
        if not isinstance(value, (float, int)) or value < 0:
            raise ValueError("Dificuldade deve ser um número não negativo.")
        self._dificuldade = value

    @property
    def setores(self):
        return self._setores

    @property
    def boss_final(self):
        return self._boss_final

    @property
    def conquistada(self):
        return self._conquistada

    @conquistada.setter
    def conquistada(self, conquistada):
        self._conquistada = conquistada
