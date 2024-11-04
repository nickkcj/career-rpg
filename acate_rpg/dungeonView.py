import time
class DungeonView:
    def pega_dados_dungeon(self):
        print("\n")
        print("------DADOS DA EMPRESA------")
        nome = input("Digite o nome da empresa: ")
        nivel_requerido = int(input("Digite o nível requerido da empresa: "))
        xp_ganho = int(input("Quanto de XP essa empresa vale? "))
        n_setores = int(input("Digite o número de setores desta empresa: "))
        return {"nome": nome, "nivel_requerido": nivel_requerido, "xp_ganho": xp_ganho, "n_setores": n_setores}



    def pega_nome_boss_final(self):
        print("\n")
        return input("Digite o nome do Boss Final da Dungeon: ")
    
    def pega_nome_dungeon(self):
        return input("Digite o nome da empresa que deseja selecionar: ")


    def pega_atributo_alteracao(self):
        return input("Digite o nome do atributo a ser alterado ou 'todos' para alterar tudo: ")

    def confirma_exclusao(self, dungeon_nome):
        return input(f"Tem certeza que deseja excluir a empresa '{dungeon_nome}'? (s/n): ").lower() == 's'

    def mostra_mensagem(self, msg):
        print("\n")
        print("****************************************")
        print(msg)
        print("****************************************")
        time.sleep(1)

    def mensagem_basica(self, msg):
        print(msg)

    def mostra_dungeons_enum(self, dungeons):
        for idx, dungeon in enumerate(dungeons):
            print(f"{idx + 1}. Nome: {dungeon.nome}, Nível Requerido: {dungeon.nivel_requerido}")

    def mostra_dungeon(self, dungeon):
        print(f"\n--- EMPRESA: {dungeon.nome} ---")
        print(f"Nível Requerido: {dungeon.nivel_requerido}")
        print(f"XP Ganho: {dungeon.xp_ganho}")
        print(f"Dificuldade: {dungeon.dificuldade}")
        print("Setores:")
        for setor in dungeon.setores:
            print(f" - Setor: {setor.nome} (Dificuldade: {setor.dificuldade})")
            print(f"   Diretor: {setor.boss.nome} - Dificuldade: {setor.boss.dificuldade} - Nivel: {setor.boss.nivel_requerido}")
        print(f"Diretor Geral: {dungeon.boss_final.nome} - Dificuldade: {dungeon.boss_final.dificuldade} - Nivel: {dungeon.boss_final.nivel_requerido}")

