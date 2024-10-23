class DungeonView():
    def pega_dados_dungeon(self):
        print("\n")
        print("------DADOS DA DUNGEON------")
        nome = input("Digite o nome da dungeon: ")
        nivel_requerido = input("Digite o nível requerido da dungeon: ")
        xp_ganho = input("Quanto de XP essa dungeon vale? ")
        status = False
        n_setores = input("Digite o número de setores: ")
        return {"nome": nome, "nivel_requerido": nivel_requerido, "xp_ganho": xp_ganho, "status": status, "n_setores": n_setores}
    

    def mostra_mensagem(self,mensagem):
        print("\n")
        print(mensagem) 


    def listar_dungeons(self, dungeons):
        print("\n")
        print("----LISTA DE DUNGEONS---- \n")
        for dungeon in dungeons:
           print(f"Nome: {dungeon.nome}, Nível Requerido: {dungeon.nivel_requerido}, XP Ganhado: {dungeon.xp_ganho}, "
                 f"Dificuldade: {dungeon.dificuldade}, Status: {dungeon.conquistada}")
           
           print("\n")

           print("Setores:")
           for setor in dungeon.setores:
                print(f"  - Nome: {setor.nome}, Dificuldade: {setor.dificuldade}")

           print("\n")


        
