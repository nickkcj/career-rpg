class DungeonView():
    def pega_dados_dungeon(self):
        print("------DADOS DA DUNGEON------")
        nome = input("Digite o nome da dungeon: ")
        nivel_requerido = input("Digite o nível requerido da dungeon: ")
        xp_ganho = input("Quanto de XP essa dungeon vale? ")
        status = False
        n_setores = input("Digite o número de setores: ")
        return {"nome": nome, "nivel_requerido": nivel_requerido, "xp_ganho": xp_ganho, "status": status, "n_setores": n_setores}
    

    def mostra_mensagem(self,mensagem):
        print(mensagem) 
        
