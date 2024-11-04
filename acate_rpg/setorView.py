class SetorView():
    
    def pega_dados_setor(self, numero):
        print("\n")
        print(f"--------DADOS DO SETOR {numero}--------")
        nome = input("Digite o nome do setor (RH, T.I, Vendas, Financeiro ou Marketing): ")
        dificuldade = input("Qual a dificuldade do setor: ")
        return {"nome": nome, "dificuldade": dificuldade}
    

    def pega_nome_setor(self, numero):
        print(f"-------- DADOS DO SETOR {numero} --------")
        return input("Digite o nome do setor (RH, T.I, Vendas, Financeiro ou Marketing): ")

    def pega_dificuldade_setor(self):
        return int(input("Qual a dificuldade do setor (1-10): "))
    
    def pega_opcao_setor(self):
        return input("Selecione o número do setor: ")
