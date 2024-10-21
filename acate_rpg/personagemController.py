from personagemView import PersonagemView
from personagem import Personagem
import time


class PersonagemController:
    def __init__(self):
        self.__personagens = []
        self.__personagemView = PersonagemView()

    @property
    def personagens(self):
        return self.__personagens

    def pega_personagem_por_nome(self, nome: str):
        for personagem in self.__personagens:
            if personagem.nome == nome:
                return personagem
        return None

    def cadastrar_personagem(self, nome, nivel=1, experiencia=0, nome_classe=""):
        if self.pega_personagem_por_nome(nome) is not None:
            raise ValueError(f"O personagem {nome} já existe!")


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

    def upar_atributos(self, personagem: Personagem):
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

    def upar_nivel(self, personagem: Personagem):
        if personagem.experiencia >= self.__calcular_exp_para_proximo_nivel(personagem.nivel):
            personagem.nivel += 1
            personagem.experiencia = 0
            personagem.pontos_disponiveis += 5
            self.__personagemView.mostra_mensagem(f"{personagem.nome} subiu para o nível {personagem.nivel}!")
        else:
            self.__personagemView.mostra_mensagem(f"{personagem.nome} não tem experiência suficiente para subir de nível.")

    def __calcular_exp_para_proximo_nivel(self, nivel_atual):
        return 100 + (10 * nivel_atual)

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
            item_nomes = {
                1: "Poção de HP",
                2: "Poção de Estamina"
            }
            item_nome = item_nomes.get(tipo_item, "Item desconhecido")
            self.__personagemView.mostra_mensagem(f"{personagem.nome} não tem {item_nome} disponível!")

    def usar_habilidade(self, classe_personagem: Personagem):
        #colocar a logica em que o jogador escolhe qual habilidade ele quer usar,
        #podendo escolher entre 3 habilidades, que tem efeitos diferentes no inimigo.
        pass

    