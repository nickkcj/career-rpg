from ranking import Ranking
from rankingView import RankingView
from personagemController import PersonagemController

class RankingController:
    def __init__(self, personagem_controller: PersonagemController):
        self.__personagem_controller = personagem_controller
        self.__ranking_view = RankingView()

    def atualizar_personagens_ranking(self):
        # Obtendo os personagens diretamente do controlador de personagens.
        personagens = list(self.__personagem_controller.personagens)  # Convertendo para lista
        return personagens

    def exibir_ranking_nivel(self):
        personagens = self.atualizar_personagens_ranking()
        dados_ranking = [
            {
                "nome": personagem.nome,
                "nivel": personagem.nivel,
                "classe_personagem": {
                    "nome_classe": personagem.classe_personagem.nome_classe,
                    "atributos": {
                        "hp": personagem.classe_personagem.atributos["hp"],
                        "estamina": personagem.classe_personagem.atributos["estamina"],
                        "ataque": personagem.classe_personagem.atributos["ataque"],
                        "defesa": personagem.classe_personagem.atributos["defesa"]
                    }
                },
                "experiencia_total": personagem.experiencia_total,
                "cursos_conquistados": personagem.cursos_conquistados,
                "dungeons_conquistadas": [
                    {"nome": dungeon.nome, "nivel_requerido": dungeon.nivel_requerido}
                    for dungeon in personagem.dungeons_conquistadas
                ]
            }
            for personagem in sorted(personagens, key=lambda p: p.nivel, reverse=True)
        ]
        self.__ranking_view.exibir_ranking_nivel(dados_ranking)




    def exibir_ranking_dungeons(self):
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: len(p.dungeons_conquistadas), reverse=True)
        self.__ranking_view.exibir_ranking_dungeons(personagens_ordenados)

    def exibir_ranking_cursos(self):
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: p.cursos_conquistados, reverse=True)
        self.__ranking_view.exibir_ranking_cursos(personagens_ordenados)


