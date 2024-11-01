import time
class DungeonView:
    def pega_dados_dungeon(self):
        print("\n")
        print("------DADOS DA DUNGEON------")
        nome = input("Digite o nome da dungeon: ")
        nivel_requerido = int(input("Digite o nível requerido da dungeon: "))
        xp_ganho = int(input("Quanto de XP essa dungeon vale? "))
        n_setores = int(input("Digite o número de setores: "))
        return {"nome": nome, "nivel_requerido": nivel_requerido, "xp_ganho": xp_ganho, "n_setores": n_setores}

    def pega_nome_setor(self, numero):
        print(f"-------- DADOS DO SETOR {numero} --------")
        return input("Digite o nome do setor (RH, T.I, Vendas, Financeiro ou Marketing): ")

    def pega_dificuldade_setor(self):
        return int(input("Qual a dificuldade do setor (1-10): "))

    def pega_nome_boss_final(self):
        print("\n")
        return input("Digite o nome do Boss Final da Dungeon: ")
    
    def pega_nome_dungeon(self):
        return input("Digite o nome da dungeon que deseja selecionar: ")

    def pega_opcao_setor(self):
        return input("Selecione o número do setor: ")
    
    def mostra_dungeons_enum(self, dungeons):
        for idx, dungeon in enumerate(dungeons):
            print(f"{idx + 1}. Nome: {dungeon.nome}, Nível Requerido: {dungeon.nivel_requerido}")

    def pega_atributo_alteracao(self):
        return input("Digite o nome do atributo a ser alterado ou 'todos' para alterar tudo: ")

    def confirma_exclusao(self, dungeon_nome):
        return input(f"Tem certeza que deseja excluir a dungeon '{dungeon_nome}'? (s/n): ").lower() == 's'

    def mostra_mensagem(self, msg):
        print("\n")
        print("****************************************")
        print(msg)
        print("****************************************")
        time.sleep(2)

    def mostra_dungeon(self, dungeon):
        print(f"\n--- DUNGEON: {dungeon.nome} ---")
        print(f"Nível Requerido: {dungeon.nivel_requerido}")
        print(f"XP Ganho: {dungeon.xp_ganho}")
        print(f"Dificuldade: {dungeon.dificuldade}")
        print("Setores:")
        for setor in dungeon.setores:
            print(f" - Setor: {setor.nome} (Dificuldade: {setor.dificuldade})")
            print(f"   Boss: {setor.boss.nome}")
        print(f"Boss Final: {dungeon.boss_final.nome}")

