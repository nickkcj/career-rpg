
import json
import time
import os
from sistema import Sistema
from sistemaView import SistemaView
from personagemController import PersonagemController
from cursoController import CursoController
from quizController import QuizController
from bossController import BossController
from dungeonController import DungeonController
from batalhaController import BatalhaController
from setorController import SetorController


class SistemaControllerr:
    def __init__(self):
        self.__sistema = Sistema()
        self.__sistemaView = SistemaView()
        self.__personagemController = PersonagemController()
        self.__cursoController = CursoController()
        self.__quizController = QuizController()
        self.__bossController = BossController()
        self.__setorController = SetorController()
        self.__dungeonController = DungeonController()
        self.__batalhaController = BatalhaController(self)
        self.__quizController._QuizController__cursoController = self.__cursoController
        
        self.__arquivo_personagens = "personagens.json"
        self.carregar_personagens()


    @property
    def cursoController(self):
        return self.__cursoController
    
    @property
    def quizController(self):
        return self.__quizController
    
    @property
    def bossController(self):
        return self.__bossController
    
    @property
    def setorController(self):
        return self.__setorController
    
    @property
    def dungeonController(self):
        return self.__dungeonController
    
    @property
    def batalhaController(self):
        return self.__batalhaController
    
    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def salvar_personagens(self):
        personagens_salvar = []
        for personagem in self.__personagemController.personagens:
            personagens_salvar.append({
                'nome': personagem.nome,
                'nivel': personagem.nivel,
                'experiencia': personagem.experiencia,
                'classe': personagem.classe_personagem.nome_classe,
                'pontos_disponiveis': personagem.pontos_disponiveis,
                'pocoes_hp': personagem.pocao_hp.quant,
                'pocoes_est': personagem.pocao_est.quant,
                'atributos': personagem.classe_personagem.atributos
            })

        with open(self.__arquivo_personagens, 'w') as arquivo:
            json.dump(personagens_salvar, arquivo, indent=4)
        self.__sistemaView.mostrar_mensagem("Personagens salvos com sucesso!")
        time.sleep(2)

    def carregar_personagens(self):
        try:
            with open(self.__arquivo_personagens, 'r') as arquivo:
                personagens_carregados = json.load(arquivo)
                for dados_personagem in personagens_carregados:
                    personagem = self.__personagemController.cadastrar_personagem(
                        nome=dados_personagem['nome'],
                        nivel=dados_personagem['nivel'],
                        experiencia=dados_personagem['experiencia'],
                        nome_classe=dados_personagem['classe']
                    )
                    personagem.pocao_hp.quant = dados_personagem['pocoes_hp']
                    personagem.pocao_est.quant = dados_personagem['pocoes_est']
                    personagem.pontos_disponiveis = dados_personagem['pontos_disponiveis']
                    personagem.classe_personagem.atributos.update(dados_personagem['atributos'])
                self.__sistemaView.mostrar_mensagem(f"{len(personagens_carregados)} personagens carregados com sucesso!")
                time.sleep(2)
        except FileNotFoundError:
            self.__sistemaView.mostrar_mensagem("Nenhum arquivo de personagens encontrado. Iniciando sistema sem personagens.")
            time.sleep(2)

    def iniciar(self):
        self.limpar_terminal()
        while True:
            self.__sistemaView.menu_inicial()
            opcao = self.__sistemaView.pegar_opcao()

            if opcao == '1':
                self.menu_personagem()

            elif opcao == '2':
                self.__dungeonController.cadastrar_dungeon()
                self.iniciar()

            elif opcao == '3':
                self.salvar_personagens()
                self.__sistemaView.mostrar_mensagem("Saindo do sistema...")
                time.sleep(1)
                break

    def menu_principal(self):
        self.limpar_terminal()
        while True:
            self.__sistemaView.menu_principal()
            opcao = self.__sistemaView.pegar_opcao()

            if opcao == '1':
                self.menu_curso()

            elif opcao == '2':
                self.quizController.realizar_quiz()

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

    def menu_personagem(self):
        self.limpar_terminal()
        while True:
            self.__sistemaView.menu_personagem()
            opcao = self.__sistemaView.pegar_opcao()

            if opcao == '1':
                self.cadastrar_personagem()
            elif opcao == '2':
                personagem = self.selecionar_personagem()
                if personagem:
                    self.mostrar_status(personagem)
                    self.opcoes_personagem(personagem)
            elif opcao == '0':
                self.salvar_personagens()
                self.__sistemaView.mostrar_mensagem("Saindo do sistema...")
                time.sleep(1)
                break
            else:
                self.__sistemaView.mostrar_mensagem("Opção inválida. Tente novamente.")
                time.sleep(1)

    def cadastrar_personagem(self):
        dados_personagem = None
        while dados_personagem is None:
            try:
                dados_personagem = self.__sistemaView.pega_dados_personagem()
                if not dados_personagem['classe']:
                    raise ValueError("Classe inválida!")
                for personagem in self.__sistema.listar_personagens():
                    if personagem.nome == dados_personagem["nome"]:
                        raise ValueError(f"O personagem {dados_personagem['nome']} já existe!")
            except ValueError as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                dados_personagem = None

        personagem = self.__personagemController.cadastrar_personagem(
            nome=dados_personagem["nome"],
            nivel=dados_personagem["nivel"],
            experiencia=dados_personagem["experiencia"],
            nome_classe=dados_personagem["classe"]
        )
        self.__sistema.adicionar_personagem(personagem)
        self.__sistemaView.mostrar_mensagem(f"Personagem {dados_personagem['nome']} da classe {dados_personagem['classe']} cadastrado com sucesso!")

    def selecionar_personagem(self):
        personagens = self.__personagemController.personagens
        self.__sistemaView.mostrar_personagens(personagens)

        escolha = self.__sistemaView.pegar_personagem_selecionado()
        if escolha.isdigit() and 1 <= int(escolha) <= len(personagens):
            personagem = personagens[int(escolha) - 1]
            return personagem
        else:
            self.__sistemaView.mostrar_mensagem("Escolha inválida.")
            time.sleep(2)
            return None

    def mostrar_status(self, personagem):
        self.__personagemController.mostrar_status(personagem)


    def opcoes_personagem(self, personagem):
        while True:
            self.__sistemaView.mostrar_opcoes_personagem()
            opcao = self.__sistemaView.pegar_opcao()

            if opcao == '1':
                self.mostrar_status(personagem)
            elif opcao == '2':
                self.__personagemController.upar_atributos(personagem)
            elif opcao == '3':
                self.__personagemController.usar_item(personagem)
            elif opcao == '4':
                self.__personagemController.upar_nivel(personagem)
            elif opcao == '5':
                self.menu_principal()
            elif opcao == '0':
                break
            else:
                self.__sistemaView.mostrar_mensagem("Opção inválida. Tente novamente.")
                time.sleep(2)

    def menu_curso(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Cursos:\n1. Cadastrar Curso\n2. Alterar Curso\n3. Excluir Curso\n4. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.__cursoController.cadastrar_curso()
            elif opcao == '2':
                self.__cursoController.alterar_curso()
            elif opcao == '3':
                self.__cursoController.excluir_curso()
            elif opcao == '4':
                self.menu_principal()

    def menu_bosses(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Bosses:\n1. Cadastrar Boss\n2. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.__bossController.cadastrar_boss()

            elif opcao == '2':
                self.menu_principal()

    def menu_dungeons(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Dungeons:\n1. Cadastrar Dungeon\n2. Ver Dungeons\n3. Voltar\nEscolha uma opção: ")

            if opcao == '1':
                self.__dungeonController.cadastrar_dungeon()

            elif opcao == '2':
                self.__dungeonController.mostrar_dungeons()  

            elif opcao == '3':
                self.menu_principal()

