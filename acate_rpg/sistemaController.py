
import json
import time
from sistema import Sistema
from sistemaView import SistemaView
from personagemController import PersonagemController
from cursoController import CursoController
from quizController import QuizController


class SistemaControllerr:
    def __init__(self):
        self.__sistema = Sistema()
        self.__sistemaView = SistemaView()
        self.__personagemController = PersonagemController(self)
        self.__cursoController = CursoController(self)
        self.__quizController = QuizController(self)
        self.__arquivo_personagens = "personagens.json"
        self.carregar_personagens()


    @property
    def cursoController(self):
        return self.__cursoController
    
    @property
    def quizController(self):
        return self.__quizController

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

    def executar(self):
        while True:
            self.__sistemaView.mostrar_menu()
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
                break
            else:
                self.__sistemaView.mostrar_mensagem("Opção inválida. Tente novamente.")
                time.sleep(2)

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
            opcao = input("Escolha uma opção: ").strip()

            if opcao == '1':
                self.mostrar_status(personagem)
            elif opcao == '2':
                self.__personagemController.upar_atributos(personagem)
            elif opcao == '3':
                self.__personagemController.usar_item(personagem)
            elif opcao == '4':
                self.__personagemController.upar_nivel(personagem)
            elif opcao == '0':
                break
            else:
                self.__sistemaView.mostrar_mensagem("Opção inválida. Tente novamente.")
                time.sleep(2)
