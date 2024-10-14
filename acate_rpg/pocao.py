class Pocao:
    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

        