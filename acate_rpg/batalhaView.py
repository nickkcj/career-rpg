class BatalhaView:
    def tela_opcoes(self):
        print("-------- BATALHA ----------")
        print("Escolha a ação:")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Usar Item")
        print("4 - Usar Habilidade")

        opcao = int(input("Escolha a ação: "))
        return opcao

    def escolher_habilidade(self):
        #colocar a logica do personagem escolher a habilidade
        pass

    def mostra_resultado(self, mensagem):
        print(mensagem)

    def mostra_mensagem(self, msg):
        print(msg)

