import time
from dungeonView import DungeonView
from dungeon import Dungeon
from setorController import SetorController
import os
class DungeonController():
    def __init__(self):
        self.__dungeons = []
        self.__dungeonView = DungeonView()
        self.__setorController = SetorController()

    def cadastrar_dungeon(self):
        while True:
            try:
                setores = []
                dados_dungeon = self.__dungeonView.pega_dados_dungeon()
                erros = []

                try:
                    nivel_requerido = int(dados_dungeon["nivel_requerido"])
                    if not 1 <= nivel_requerido <= 10:
                        erros.append("O nível requerido deve ser um inteiro entre 1 e 10.")
                except ValueError:
                    erros.append("O nível requerido deve ser um número inteiro.")

                
                try:
                    xp_ganho = int(dados_dungeon["xp_ganho"])
                except ValueError:
                    erros.append("O XP ganho deve ser um número inteiro.")

                
                try:
                    n_setores = int(dados_dungeon["n_setores"])
                    if not 1 <= n_setores <= 5:
                        erros.append("O número de setores deve ser entre 1 e 5.")
                except ValueError:
                    erros.append("O número de setores deve ser um número inteiro.")

                
                if erros:
                    self.__dungeonView.mostra_mensagem("Não foi possível cadastrar a dungeon:\n" + "\n".join(erros))
                    time.sleep(3)
                    os.system('cls' if os.name == 'nt' else 'clear')
                    continue  

                
                for i in range(n_setores):
                    setor = self.__setorController.adicionar_setor(i+1)
                    setores.append(setor)

                dificuldade = round(self.__setorController.calcular_media_dificuldades(setores), 1)
                dungeon = Dungeon(dados_dungeon["nome"], nivel_requerido, xp_ganho, dificuldade, setores, dados_dungeon["status"])
                self.__dungeons.append(dungeon)

                self.__dungeonView.mostra_mensagem(f"A dungeon {dados_dungeon['nome']} foi cadastrada com sucesso")
                time.sleep(3)
                break  
            
            except Exception as e:
                self.__dungeonView.mostra_mensagem(f"Erro inesperado: {str(e)}")


    def mostrar_dungeons(self):
        self.__dungeonView.listar_dungeons(self.__dungeons)

