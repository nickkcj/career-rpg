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
    
    def escolher_item(self):
        print("Escolha o item para usar:")
        print("1 - Poção de HP")
        print("2 - Poção de Estamina")
        escolha = int(input("Digite o número do item: "))
        if escolha == 1:
            return "HP"
        elif escolha == 2:
            return "Estamina"
        else:
            return
        
    def escolher_habilidade(self):
        #colocar a logica do personagem escolher a habilidade
        pass

    def mostra_resultado(self, mensagem):
        print(mensagem)

    def mostra_mensagem(self, msg):
        print(msg)

        