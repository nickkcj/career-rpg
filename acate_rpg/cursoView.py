import time
import os
class CursoView():
    def pega_dados_curso(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("---DADOS DO CURSO---")
        ##Aqui tem que realizar diversos testes pra cada variável.
        nome = input("Digite o nome do curso: ")
        nivel_requerido = input("Qual o nível requerido do curso? ")
        xp_ganho = input("Quanto de xp esse curso vale? ")
        setor = input("Esse curso é para qual setor? ")
        dificuldade = input("Qual a dificuldade do curso? ")
        print("\n")
        realizado = False
        return {"nome": nome, 
                "nivel_requerido": nivel_requerido, 
                "xp_ganho": xp_ganho, 
                "setor": setor, 
                "dificuldade": dificuldade, 
                "realizado": realizado}



    def mostra_mensagem(self,mensagem):
        print("\n")
        print("****************************************")
        print(mensagem)
        print("****************************************")
        time.sleep(1)


    def mostra_cursos(self,cursos):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n")
        print("----LISTA DE CURSOS---- \n")
        for curso in cursos:
            print(f"Nome: {curso.nome}, Nível Requerido: {curso.nivel_requerido}, XP Ganhado: {curso.xp_ganho}, "
                  f"Setor: {curso.setor}, Dificuldade: {curso.dificuldade}, Realizado: {curso.realizado} \n")

    def seleciona_curso(self):
        print("\n")
        nome = input("Qual o nome do curso que você quer selecionar?: ")
        ##Aqui tem que testar se o curso está na lista, senão raise exception
        return nome
    
