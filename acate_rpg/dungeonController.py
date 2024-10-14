from dungeonView import DungeonView
from dungeon import Dungeon
from setorController import SetorController

class DungeonController():
    def __init__(self):
        self.__dungeons = []
        self.__dungeonView = DungeonView()
        self.__setorController = SetorController()

    def cadastrar_dungeon(self):
        dados_dungeon = self.__dungeonView.pega_dados_dungeon()
        dificuldade = self.__setorController.calcular_media_dificuldades
        dungeon = Dungeon(dados_dungeon["nome"], dados_dungeon["nivel_requerido"], dados_dungeon["xp_ganho"], dados_dungeon[dificuldade], dados_dungeon["status"])
        
        for _ in range(dados_dungeon["n_setores"]):
            setor = self.__setorController.adicionar_setor()
            dungeon.setores.append(setor)

        self.__dungeons.append(dungeon)
        self.__dungeonView.mostra_mensagem(f"A dungeon {dados_dungeon["nome"]} foi cadastrada com sucesso")

