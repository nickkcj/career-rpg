from boss import Boss
from bossView import BossView

class BossController:
    def __init__(self):
        self.__boss = None
        self.__boss_view = BossView()

    def cadastrar_boss(self):
        dados_boss = self.__boss_view.pega_dados_boss()
        boss = Boss(**dados_boss)
        self.__boss_view.mostra_mensagem(f"Boss {self.__boss.nome} cadastrado com sucesso!")

    def mostrar_atributos(self):
        if self.__boss:
            atributos = self.__boss.mostrar_atributos()
            self.__boss_view.mostra_atributos(atributos)
        else:
            self.__boss_view.mostra_mensagem("Nenhum boss cadastrado.")

