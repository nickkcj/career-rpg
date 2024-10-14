from boss import Boss
from bossView import BossView

class BossController:
    def __init__(self):
        self.__bosses = []
        self.__bossView = BossView()

    def cadastrar_boss(self):
        dados_boss = self.__bossView.pega_dados_boss()
        boss = Boss(dados_boss)
        self.__bossView.mostra_mensagem(f"Boss {self.__boss.nome} cadastrado com sucesso!")

        dados_personagem = self.__personagemView.pega_dados_personagem()
        personagem_existente = self.pega_personagem_por_nome(dados_personagem["nome"])
        if personagem_existente is None:
            classe = dados_personagem["classe"]
            personagem = Personagem(dados_personagem["nome"], dados_personagem["nivel"], dados_personagem["experiencia"], None, None, dados_personagem["classe"])
            self.__personagens.append(personagem)
            self.__personagemView.mostra_mensagem(f"Personagem {dados_personagem['nome']} cadastrado com sucesso!")
        else:
            self.__personagemView.mostra_mensagem(f"O personagem {dados_personagem['nome']} já existe!")

    def mostrar_atributos(self):
        if self.__boss:
            atributos = self.__boss.mostrar_atributos()
            self.__bossView.mostra_atributos(atributos)
        else:
            self.__bossView.mostra_mensagem("Nenhum boss cadastrado.")

