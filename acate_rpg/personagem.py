from classePersonagem import ClassePersonagem
from pocao_hp import PocaoHP
from pocao_est import PocaoEstamina

class Personagem():
    def __init__(self, nome, nivel, experiencia, nome_classe: str, pocao_hp: PocaoHP=None, pocao_est: PocaoEstamina=None, pontos_disponiveis=10):
        self.__nome = nome
        self.__nivel = nivel
        self.__experiencia = experiencia
        self.__classe_personagem = ClassePersonagem(nome_classe=nome_classe)

        self.__pocao_hp = pocao_hp if pocao_hp else PocaoHP(quant=3)
        self.__pocao_est = pocao_est if pocao_est else PocaoEstamina(quant=3)
        
        self.__pontos_disponiveis = pontos_disponiveis


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
    def classe_personagem(self):
        return self.__classe_personagem

    @classe_personagem.setter
    def classe_personagem(self, classe_personagem: ClassePersonagem):
        self.__classe_personagem = classe_personagem

    @property
    def pocao_hp(self):
        return self.__pocao_hp

    @pocao_hp.setter
    def pocao_hp(self, pocao_hp: PocaoHP):
        self.__pocao_hp = pocao_hp

    @property
    def pocao_est(self):
        return self.__pocao_est

    @pocao_est.setter
    def pocao_est(self, pocao_est: PocaoEstamina):
        self.__pocao_est = pocao_est

    @property
    def pontos_disponiveis(self):
        return self.__pontos_disponiveis

    @pontos_disponiveis.setter
    def pontos_disponiveis(self, pontos):
        self.__pontos_disponiveis = pontos
