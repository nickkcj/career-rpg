from classePersonagem import ClassePersonagem
from pocao_hp import PocaoHP
from pocao_est import PocaoEstamina

class Personagem(ClassePersonagem, PocaoHP, PocaoEstamina):
    def __init__(self, nome, nivel, experiencia, pocao_hp: PocaoHP, pocao_est: PocaoEstamina, classe_personagem: ClassePersonagem):
        self.__nome = nome
        self.__nivel = nivel
        self.__experiencia = experiencia
        if isinstance(pocao_hp, PocaoHP):
            self.__pocao_hp = pocao_hp
        if isinstance(pocao_est, PocaoEstamina):
            self.__pocao_est = pocao_est
        if isinstance(classe_personagem, ClassePersonagem):
            self.__classe_personagem = classe_personagem


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self.__experiencia = experiencia

    @property
    def pocao_hp(self):
        return self.__pocao_hp

    @pocao_hp.setter
    def pocao_hp(self, pocao_hp):
        self.__pocao_hp = pocao_hp

    @property
    def pocao_est(self):
        return self.__pocao_est

    @pocao_est.setter
    def pocao_est(self, pocao_est):
        self.__pocao_est = pocao_est

    @property
    def classe_personagem(self):
        return self.__classe_personagem

    @classe_personagem.setter
    def classe_personagem(self, classe_personagem):
        self.__classe_personagem = classe_personagem