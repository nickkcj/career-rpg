from ranking import Ranking
from rankingView import RankingView
from personagemController import PersonagemController

class RankingController:
    def __init__(self, personagem_controller):
        self.__personagem_controller = personagem_controller
        self.__ranking_view = RankingView()

    def atualizar_personagens_ranking(self):
        personagens = self.__personagem_controller.personagens
        return personagens

    def exibir_ranking_nivel(self):
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: p.nivel, reverse=True)
        self.__ranking_view.exibir_ranking_nivel(personagens_ordenados)

    def exibir_ranking_dungeons(self):
        pass
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: len(p.dungeons_conquistadas), reverse=True)
        self.__ranking_view.exibir_ranking_dungeons(personagens_ordenados)
        while True:
            print("\n")
            nome_personagem = input("Deseja ver as dungeons de algum dos personagens? (Digite o nome do personagem ou digite 'sair'): ")
            print("\n")
            if nome_personagem.lower() == 'sair':
                break

            personagem_encontrado = next((p for p in personagens_ordenados if p.nome.lower() == nome_personagem.lower()), None)
        
            if personagem_encontrado:
                self.__ranking_view.exibir_dungeons_personagem(personagem_encontrado)
            else:
                self.__ranking_view.mostrar_mensagem("Personagem não encontrado. Tente novamente.")

    def exibir_ranking_cursos(self):
        personagens = self.atualizar_personagens_ranking()
        personagens_ordenados = sorted(personagens, key=lambda p: p.cursos_conquistados, reverse=True)
        self.__ranking_view.exibir_ranking_cursos(personagens_ordenados)