class CursoView():
    def pega_dados_curso(self):
        print("---DADOS DO CURSO---")
        nome = input("Digite o nome do curso: ")
        nivel_requerido = input("Qual o nível requerido do curso? ")
        xp_ganho = input("Quanto de xp esse curso vale? ")
        setor = input("Esse curso é para qual setor? ")
        dificuldade = input("Qual a dificuldade do curso? ")
        realizado = False
        return {"nome": nome, "nivel_requerido": nivel_requerido, "xp_ganho": xp_ganho, "setor": setor, "dificuldade": dificuldade, "realizado": realizado}



    def mostra_mensagem(self,mensagem):
        print(mensagem)