from cursoController import CursoController
from quizController import QuizController



class SistemaController:
    def __init__(self):
        self.curso_controller = CursoController()
        self.quiz_controller = QuizController()
        
        # Para permitir que o QuizController tenha acesso ao CursoController
        self.quiz_controller._QuizController__cursoController = self.curso_controller

    def menu_principal(self):
        while True:
            opcao = input("\nMenu Principal:\n1. Gerenciar Cursos\n2. Realizar Quiz\n3. Sair\nEscolha uma opção: ")

            if opcao == '1':
                self.menu_curso()
            elif opcao == '2':
                self.quiz_controller.realizar_quiz()
            elif opcao == '3':
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def menu_curso(self):
        while True:
            opcao = input("\nMenu de Cursos:\n1. Cadastrar Curso\n2. Alterar Curso\n3. Excluir Curso\n4. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.curso_controller.cadastrar_curso()
            elif opcao == '2':
                self.curso_controller.alterar_curso()
            elif opcao == '3':
                self.curso_controller.excluir_curso()
            elif opcao == '4':
                break
            else:
                print("Opção inválida! Tente novamente.")

s = SistemaController()
s.menu_principal()