from classePersonagem import ClassePersonagem
from pocao_hp import PocaoHP
from pocao_est import PocaoEstamina

class Personagem():
    def __init__(self, nome, nivel, experiencia_total, nome_classe: str, pocao_hp: PocaoHP=None, pocao_est: PocaoEstamina=None, pontos_disponiveis=10, dungeons_conquistadas= None, cursos_conquistados=0):
        self.__nome = nome
        self.__nivel = nivel
        self.__experiencia_total = experiencia_total
        self.__classe_personagem = ClassePersonagem(nome_classe=nome_classe)
        self.__classes_historico = [nome_classe]
        self.__habilidades = []
        self.__dungeons_conquistadas = dungeons_conquistadas if dungeons_conquistadas is not None else []
        self.__cursos_conquistados = cursos_conquistados
        self.__dungeons_conquistadas = []
        self.__pocao_hp = pocao_hp if pocao_hp else PocaoHP(quant=3)
        self.__pocao_est = pocao_est if pocao_est else PocaoEstamina(quant=3)
        self.__pontos_disponiveis = pontos_disponiveis

    @property
    def cursos_conquistados(self):
        return self.__cursos_conquistados
    
    @cursos_conquistados.setter
    def cursos_conquistados(self, cursos_conquistados):
        self.__cursos_conquistados = cursos_conquistados

    @property
    def dungeons_conquistadas(self):
        return self.__dungeons_conquistadas
    
    @dungeons_conquistadas.setter
    def dungeons_conquistadas(self, dungeons_conquistadas):
        self.__dungeons_conquistadas = dungeons_conquistadas


    @property
    def dungeons_conquistadas(self):
        return self.__dungeons_conquistadas
    
    @dungeons_conquistadas.setter
    def dungeons_conquistadas(self, dungeons_conquistadas):
        self.__dungeons_conquistadas = dungeons_conquistadas


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
    def experiencia_total(self):
        return self.__experiencia_total

    @experiencia_total.setter
    def experiencia_total(self, experiencia):
        self.__experiencia_total = experiencia
    
    @property
    def classe_personagem(self):
        return self.__classe_personagem

    @classe_personagem.setter
    def classe_personagem(self, nova_classe: ClassePersonagem):
        if nova_classe.nome_classe != self.__classe_personagem.nome_classe:
            self.__classes_historico.append(nova_classe.nome_classe)
        self.__classe_personagem = nova_classe

    @property
    def classes_historico(self):
        return self.__classes_historico
    
    @classes_historico.setter
    def classes_historico(self, valor):
        self.__classes_historico = valor

    @property
    def habilidades(self):
        return self.__habilidades
    
    @habilidades.setter
    def habilidades(self, habilidades):
        self.__habilidades = habilidades

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
