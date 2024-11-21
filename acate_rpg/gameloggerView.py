class LogView():

    def listar_registros(self, registros):
        for i, registro in enumerate(registros, 1):
            print(f"Registro {i}:")
            print(f"  Personagem: {registro.personagem.nome} (Nível {registro.personagem.nivel})")
            print(f"  Boss: {registro.boss.nome} (Dificuldade {registro.boss.dificuldade})")
            print(f"  Dungeon: {registro.dungeon.nome}")
            print(f"  Movimento: {registro.acao}")
            print(f"  Data: {registro.data}\n")
            print("****************************************************************")
            print()

        input("Pressione Enter para voltar: ")

        


    def excluir_registro(self, registros):
        index = int(input("Digite o index que você quer alterar o registro: "))
        print()
        if 0 <= index < len(registros):
            del registros[index]
            print(f"Registro {index + 1} excluído com sucesso.")
        else:
            print("Índice inválido.")


    def alterar_registro(self, registros):
        index = int(input("Digite o index que você quer alterar o registro: "))
        if 0 <= index < len(registros):
            print("Informe os novos dados para o registro:")
            personagem = input("Nome do personagem: ")
            nivel = int(input("Nível do personagem: "))
            boss = input("Nome do boss: ")
            dificuldade = int(input("Dificuldade do boss: "))
            dungeon = input("Nome da dungeon: ")
            movimento = input("Movimento realizado: ")
            
            
            dados = {
                "personagem": personagem,
                "nivel": nivel,
                "boss": boss,
                "dificuldade": dificuldade,
                "dungeon": dungeon,
                "movimento": movimento
                    }
            
            print(f"Registro {index + 1} alterado com sucesso.")
        else:
            print("Índice inválido.")

        return dados, index
    

    def mostrar_mensagem(self, mensagem):
        print()
        print(mensagem)
        print()