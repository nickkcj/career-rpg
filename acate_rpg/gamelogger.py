from datetime import datetime

class LogJogadas:
    def __init__(self):
        self.registros = []  
    
    def adicionar_registro(self, personagem, boss, dungeon, acao):
        registro = {
            "personagem": personagem,  
            "boss": boss,      
            "dungeon": dungeon, 
            "movimento": acao,     
            "data": datetime.now()      
        }
        self.registros.append(registro)
    
    def listar_registros(self):
        for i, registro in enumerate(self.registros, 1):
            print(f"Registro {i}:")
            print(f"  Personagem: {registro['personagem'].nome} (Nível {registro['personagem'].nivel})")
            print(f"  Boss: {registro['boss'].nome} (Dificuldade {registro['boss'].dificuldade})")
            print(f"  Dungeon: {registro['dungeon'].nome}")
            print(f"  Movimento: {registro['movimento']}")
            print(f"  Data: {registro['data']}\n")
            print("****************************************************************")
            print()

        input("Pressione Enter para voltar: ")

    def excluir_registro(self, index):
        if 0 <= index < len(self.registros):
            del self.registros[index]
            print(f"Registro {index + 1} excluído com sucesso.")
        else:
            print("Índice inválido.")

    def alterar_registro(self, index):
        if 0 <= index < len(self.registros):
            print("Informe os novos dados para o registro:")
            personagem = input("Nome do personagem: ")
            nivel = int(input("Nível do personagem: "))
            boss = input("Nome do boss: ")
            dificuldade = int(input("Dificuldade do boss: "))
            dungeon = input("Nome da dungeon: ")
            movimento = input("Movimento realizado: ")
            
            
            self.registros[index] = {
                "personagem": type("Personagem", (), {"nome": personagem, "nivel": nivel}),
                "boss": type("Boss", (), {"nome": boss, "dificuldade": dificuldade}),
                "dungeon": type("Dungeon", (), {"nome": dungeon}),
                "movimento": movimento,
                "data": datetime.now()
            }
            print(f"Registro {index + 1} alterado com sucesso.")
        else:
            print("Índice inválido.")
