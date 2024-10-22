from cursoController import CursoController
from quizController import QuizController
from bossController import BossController
from dungeonController import DungeonController
from setorController import SetorController
from personagemController import PersonagemController
from batalhaController import BatalhaController
import os



class SistemaController:
    def __init__(self):
        self.curso_controller = CursoController()
        self.quiz_controller = QuizController()
        self.personagem_controller = PersonagemController()
        self.boss_controller = BossController()
        self.setor_controller = SetorController()
        self.dungeon_controller = DungeonController()
        self.batalha_controller = BatalhaController()
        self.quiz_controller._QuizController__cursoController = self.curso_controller

    def limpar_terminal(self):
        # Limpa o terminal dependendo do sistema operacional
        os.system('cls' if os.name == 'nt' else 'clear')


    def iniciar(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nBem vindo ao RPG do Mercado de Trabalho!!\n Você quer cadastrar um personagem ou uma empresa?\n1. Cadastrar Personagem\n2. Cadastrar Empresa\n3. Sair\nEscolha uma opção: ")

            if opcao == '1':
                self.personagem_controller.cadastrar_personagem()
                self.menu_principal()

            elif opcao == '2':
                self.dungeon_controller.cadastrar_dungeon()
                self.iniciar()

            elif opcao == '3':
                 break

    def menu_principal(self):
        self.limpar_terminal()

        while True:
            opcao = input("\nMenu Principal:\n1. Gerenciar Cursos\n2. Realizar Quiz\n3. Gerenciar Personagens\n4. Gerenciar Dungeons\n5. Gerenciar Bosses\n6. Batalhar\n7. Sair\nEscolha uma opção: ")

            if opcao == '1':
                self.menu_curso()

            elif opcao == '2':
                self.quiz_controller.realizar_quiz()

            elif opcao == '3':
                self.menu_personagem()

            elif opcao == '4':
                self.menu_dungeons()

            elif opcao == '5':
                self.menu_bosses()

            elif opcao == '6':
                pass

            elif opcao == '7':
                exit()




           

    def menu_curso(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Cursos:\n1. Cadastrar Curso\n2. Alterar Curso\n3. Excluir Curso\n4. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.curso_controller.cadastrar_curso()
            elif opcao == '2':
                self.curso_controller.alterar_curso()
            elif opcao == '3':
                self.curso_controller.excluir_curso()
            elif opcao == '4':
                self.menu_principal()

    def menu_personagem(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Personagens:\n1. Cadastrar Personagem\n2. Ver Status\n3. Usar Item\n4. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.personagem_controller.cadastrar_personagem()

            elif opcao == '2':
                self.personagem_controller.mostrar_status()

            elif opcao == '3':
                self.personagem_controller.usar_item()

            elif opcao == '4':
                self.menu_principal()

    
    def menu_dungeons(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Dungeons:\n1. Cadastrar Dungeon\n2. Ver Dungeons\n3. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.dungeon_controller.cadastrar_dungeon()

            elif opcao == '2':
                self.dungeon_controller.ver_dungeons() ##Implementar ainda

            elif opcao == '3':
                self.menu_principal()


    def menu_bosses(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Bosses:\n1. Cadastrar Boss\n2. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.boss_controller.cadastrar_boss()

            elif opcao == '2':
                self.menu_principal()

