class SetorView():
    
    def pega_dados_setor(self, numero):
        print("\n")
        print(f"--------DADOS DO SETOR {numero}--------")
        nome = input("Digite o nome do setor: ")
        dificuldade = input("Qual a dificuldade do setor: ")
        return {"nome": nome, "dificuldade": dificuldade}
