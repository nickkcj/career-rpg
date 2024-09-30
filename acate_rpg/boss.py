class Boss:
    def __init__(self, nome, dificuldade, nivel_requerido, ataque=0, defesa=0, hp=0, estamina=0, diretor=False):
        super().__init__(ataque, defesa, hp, estamina)
        self._nome = nome
        self._dificuldade = dificuldade
        self._nivel_requerido = nivel_requerido
        self._diretor = diretor


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

    @property
    def nivel_requerido(self):
        return self._nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, nivel_requerido):
        self._nivel_requerido = nivel_requerido

    @property
    def diretor(self):
        return self._diretor

    @diretor.setter
    def diretor(self, diretor):
        self._diretor = diretor

    def mostrar_atributos(self):
        return f"Ataque: {self.atributos['ataque']}, Defesa: {self.atributos['defesa']}, HP: {self.atributos['hp']}, Estamina: {self.atributos['estamina']}"
