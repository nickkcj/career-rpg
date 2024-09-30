from quiz import Quiz

class Curso(Quiz):
    def __init__(self, nome, nivel_requerido, xp_ganho, setor, dificuldade, realizado=False, acertos: Quiz=0):
        self._nome = nome
        self._nivel_requerido = nivel_requerido
        self._xp_ganho = xp_ganho
        self._setor = setor
        self._dificuldade = dificuldade
        self._realizado = realizado
        self._acertos = acertos


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
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, setor):
        self._setor = setor

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self._dificuldade = dificuldade

    @property
    def realizado(self):
        return self._realizado

    @realizado.setter
    def realizado(self, realizado):
        self._realizado = realizado

    @property
    def acertos(self):
        return self._acertos

    @acertos.setter
    def acertos(self, acertos):
        self._acertos = acertos

    def realizar_quiz(self, gabarito):
        pass