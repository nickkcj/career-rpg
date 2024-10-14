class SetorView():
    
    def pega_dados_setor(self):
        print("--------DADOS DO SETOR--------")
        nome = input("Digite o nome do setor: ")
        dificuldade = input("Qual a dificuldade do setor: ")
        return {"nome": nome, "dificuldade": dificuldade}