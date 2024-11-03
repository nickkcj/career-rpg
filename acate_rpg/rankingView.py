import os
import time

class RankingView:
    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_ranking_nivel(self, personagens_ordenados):
        self.limpar_tela()
        print("-------- RANKING POR NÍVEL --------")
        for i, personagem in enumerate(personagens_ordenados, start=1):
            print(f"{i}. {personagem.nome} - Nível: {personagem.nivel}")
        input("\nPressione Enter para voltar ao menu.")

    def exibir_ranking_dungeons(self, personagens_ordenados):
        self.limpar_tela()
        print("-------- RANKING POR DUNGEONS CONQUISTADAS --------")
        for i, personagem in enumerate(personagens_ordenados, start=1):
            print(f"{i}. {personagem.nome} - Dungeons Conquistadas: {len(personagem.dungeons_conquistadas)}")
        input("\nPressione Enter para voltar ao menu.")

    def exibir_ranking_cursos(self, personagens_ordenados):
        self.limpar_tela()
        print("-------- RANKING POR CURSOS CONQUISTADOS --------")
        for i, personagem in enumerate(personagens_ordenados, start=1):
            print(f"{i}. {personagem.nome} - Cursos Conquistados: {personagem.cursos_conquistados}")
        input("\nPressione Enter para voltar ao menu.")


    def exibir_dungeons_personagem(self, personagem):
        if not personagem.dungeons_conquistadas:
            print(f"{personagem.nome} não conquistou nenhuma dungeon.")
        else:
            print(f"Dungeons conquistadas por {personagem.nome}:")
            for dungeon in personagem.dungeons_conquistadas:
                print(f"- {dungeon.nome}")


    def mostrar_mensagem(self, mensagem):
        print("***************************")
        print(mensagem)
        print("***************************")
       