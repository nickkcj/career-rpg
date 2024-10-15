from personagemView import PersonagemView
from personagem import Personagem
from bossController import BossController

class PersonagemController():
    def __init__(self):
        self.__personagens = []
        self.__personagemView = PersonagemView()


    def pega_personagem_por_nome(self, nome: str):
        for personagem in self.__personagens:
            if (personagem.nome == nome):
                return personagem
        return None

    def cadastrar_personagem(self, nome, nivel=1, experiencia=0, nome_classe=""):
        personagem = Personagem(
            nome=nome,
            nivel=nivel,
            experiencia=experiencia,
            nome_classe=nome_classe
        )
        self.__personagens.append(personagem)
        return personagem

    def mostrar_status(self, personagem: Personagem):
        status = {
            'nome': personagem.nome,
            'nivel': personagem.nivel,
            'experiencia': personagem.experiencia,
            'ataque': personagem.classe_personagem.atributos['ataque'],
            'defesa': personagem.classe_personagem.atributos['defesa'],
            'hp': personagem.classe_personagem.atributos['hp'],
            'estamina': personagem.classe_personagem.atributos['estamina'],
            'pontos_disponiveis': personagem.pontos_disponiveis,
            'pocoes_hp': personagem.pocao_hp.quant,
            'pocoes_est': personagem.pocao_est.quant
        }
        self.__personagemView.mostrar_status(status)

    def upar_atributos(self, personagem):
        if personagem.pontos_disponiveis > 0:
            atributo_escolhido = self.__personagemView.escolher_atributo()
            pontos = self.__personagemView.pega_quantidade_pontos()
            if pontos <= personagem.pontos_disponiveis:
                if atributo_escolhido in personagem.classe_personagem.atributos:
                    personagem.classe_personagem.atributos[atributo_escolhido] += pontos
                    personagem.pontos_disponiveis -= pontos
                    self.__personagemView.mostra_mensagem(f"Atributo {atributo_escolhido} aumentado em {pontos} pontos!")
                else:
                    self.__personagemView.mostra_mensagem("Atributo inválido.")
            else:
                self.__personagemView.mostra_mensagem("Pontos insuficientes.")
        else:
            self.__personagemView.mostra_mensagem("Você não tem pontos disponíveis para distribuir.")
    def usar_item(self, personagem: Personagem):
        tipo_item = self.__personagemView.escolher_item()
        if tipo_item == 1 and personagem.pocao_hp and personagem.pocao_hp.quant > 0:
            personagem.classe_personagem.atributos['hp'] += personagem.pocao_hp.valor
            personagem.pocao_hp.quant -= 1
            self.__personagemView.mostra_mensagem(f"{personagem.nome} usou Poção de HP!")
        elif tipo_item == 2 and personagem.pocao_est and personagem.pocao_est.quant > 0:
            personagem.classe_personagem.atributos['estamina'] += personagem.pocao_est.valor
            personagem.pocao_est.quant -= 1
            self.__personagemView.mostra_mensagem(f"{personagem.nome} usou Poção de Estamina!")
        else:
            self.__personagemView.mostra_mensagem(f"{self.nome} não tem Poção de {tipo_item} disponível!")

    def usar_habilidade(self, classe_personagem: Personagem, boss: BossController):
        #colocar a logica em que o jogador escolhe qual habilidade ele quer usar,
        #podendo escolher entre 3 habilidades, que tem efeitos diferentes no inimigo.
        pass

    