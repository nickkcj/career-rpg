from personagemView import PersonagemView
from personagem import Personagem

class PersonagemController():
    def __init__(self):
        self.__personagem = []
        self.__personagemView = PersonagemView()


    def atacar(self, boss):
        dano = self.classe_personagem.atributos['ataque'] - boss.atributos['defesa']
        dano = max(dano, 1)
        boss.atributos['hp'] -= dano
        print(f"{self.nome} atacou {boss.nome} e causou {dano} de dano!")

    def defender(self):
        #colocar a logica que dobraria o atributo 'defender' durante 1 turno
        pass

    def usar_item(self, tipo_item):
        if tipo_item == "HP" and self.pocao_hp.quant > 0:
            self.classe_personagem.atributos['hp'] += self.pocao_hp.valor
            self.pocao_hp.quant -= 1
            print(f"{self.nome} usou {self.pocao_hp.nome} e recuperou {self.pocao_hp.valor} de HP! Poções restantes: {self.pocao_hp.quant}")
        elif tipo_item == "Estamina" and self.pocao_est.quant > 0:
            self.classe_personagem.atributos['estamina'] += self.pocao_est.valor
            self.pocao_est.quant -= 1
            print(f"{self.nome} usou {self.pocao_est.nome} e recuperou {self.pocao_est.valor} de Estamina! Poções restantes: {self.pocao_est.quant}")
        else:
            print(f"{self.nome} não tem Poção de {tipo_item} disponível!")

    def usar_habilidade(self, classe_personagem):
        #colocar a logica em que o jogador escolhe qual habilidade ele quer usar,
        #podendo escolher entre 3 habilidades, que tem efeitos diferentes no inimigo.
        pass