from ranking import Ranking
from rankingView import RankingView
from personagemController import PersonagemController

class RankingController:
    def __init__(self, personagem_controller: PersonagemController):
        self.__personagem_controller = personagem_controller
        self.__ranking_view = RankingView()

    def atualizar_personagens_ranking(self):
        # Obtendo os personagens diretamente do controlador de personagens.
        personagens = list(self.__personagem_controller.personagensDAO)  # Convertendo para lista
        return personagens

    def exibir_ranking_nivel(self):
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: p.nivel, reverse=True)
        self.__ranking_view.exibir_ranking_nivel(personagens_ordenados)

    def exibir_ranking_dungeons(self):
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: len(p.dungeons_conquistadas), reverse=True)
        self.__ranking_view.exibir_ranking_dungeons(personagens_ordenados)

    def exibir_ranking_cursos(self):
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: p.cursos_conquistados, reverse=True)
        self.__ranking_view.exibir_ranking_cursos(personagens_ordenados)


