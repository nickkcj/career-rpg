from dungeonView import DungeonView
from dungeon import Dungeon
from setorController import SetorController

class DungeonController():
    def __init__(self):
        self.__dungeons = []
        self.__dungeonView = DungeonView()
        self.__setorController = SetorController()

    def cadastrar_dungeon(self):
        setores = []
        dados_dungeon = self.__dungeonView.pega_dados_dungeon()
        for _ in range(int(dados_dungeon["n_setores"])):
            setor = self.__setorController.adicionar_setor()
            setores.append(setor)

        dificuldade = self.__setorController.calcular_media_dificuldades

        dungeon = Dungeon(dados_dungeon["nome"], dados_dungeon["nivel_requerido"], dados_dungeon["xp_ganho"], dificuldade, setores, dados_dungeon["status"])

        self.__dungeons.append(dungeon)
        self.__dungeonView.mostra_mensagem(f"A dungeon {dados_dungeon["nome"]} foi cadastrada com sucesso")

