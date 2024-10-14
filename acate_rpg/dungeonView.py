class DungeonView():
    def pega_dados_dungeon(self):
        print("------DADOS DA DUNGEON------")
        nome = input("Digite o nome da dungeon: ")
        n_setores = input("Digite o número de setores: ")
        return {"nome": nome, "n_setores": n_setores}
    

    def mostra_mensagem(self,mensagem):
        print(mensagem) 
        
