from models.setor import Setor
from bossController import BossController
from acate_rpg.exceptions.exceptions import CriacaoSetorException
from setorView import SetorView

class SetorController:
    def __init__(self):
        self.__bossController = BossController()
        self.__setorView = SetorView()

    def criar_setor_com_boss(self, nome_setor, dificuldade_setor, nivel_requerido, nome_dungeon):
        try:
            boss = self.__bossController.criar_boss(nome=f"Diretor de {nome_setor} da {nome_dungeon}", dificuldade=dificuldade_setor, nivel_requerido=nivel_requerido, ataque=0, defesa=0, hp=0, estamina=0)
            return Setor(nome=nome_setor, dificuldade=dificuldade_setor, boss=boss)
        except Exception as e:
            raise CriacaoSetorException(f"Erro ao criar setor: {str(e)}")

    def criar_setor_de_dicionario(self, setor_data):
        try:
            boss = self.__bossController.criar_boss(
                nome=setor_data["boss"]["nome"],
                dificuldade=setor_data["boss"]["dificuldade"],
                nivel_requerido=setor_data["boss"]["nivel_requerido"],
                ataque=0,
                defesa=0,
                hp=0,
                estamina=0
            )
            return Setor(nome=setor_data["nome"], dificuldade=setor_data["dificuldade"], boss=boss)
        except KeyError as e:
            raise Exception(f"Erro ao acessar dados do setor: chave ausente {str(e)}")
        except Exception as e:
            raise Exception(f"Erro ao criar setor: {str(e)}")

    def to_dict(self, setor):
        return {
            "nome": setor.nome,
            "dificuldade": setor.dificuldade,
            "boss": self.__bossController.to_dict(setor.boss)
        }
    
    def escolher_setor(self, dungeon):
        escolha = self.__setorView.selecionar_setor(dungeon)
        for setor in dungeon.setores:
            if setor.nome == escolha:
                boss = setor.boss

        return boss
