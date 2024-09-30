from classePersonagem import ClassePersonagem


class Personagem():
    def __init__(self, nome, cargo, nivel, experiencia, pocao_hp, pocao_est, classe_personagem):
        self._nome = nome
        self._cargo = cargo
        self._nivel = nivel
        self._experiencia = experiencia
        self._pocao_hp = pocao_hp
        self._pocao_est = pocao_est
        self._classe_personagem = classe_personagem


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo

    @property
    def nivel(self):
        return self._nivel

    @nivel.setter
    def nivel(self, nivel):
        self._nivel = nivel

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self._experiencia = experiencia

    @property
    def pocao_hp(self):
        return self._pocao_hp

    @pocao_hp.setter
    def pocao_hp(self, pocao_hp):
        self._pocao_hp = pocao_hp

    @property
    def pocao_est(self):
        return self._pocao_est

    @pocao_est.setter
    def pocao_est(self, pocao_est):
        self._pocao_est = pocao_est

    @property
    def classe_personagem(self):
        return self._classe_personagem

    @classe_personagem.setter
    def classe_personagem(self, classe_personagem):
        self._classe_personagem = classe_personagem