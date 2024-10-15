
from sistema import Sistema
from sistemaView import SistemaView
from personagemController import PersonagemController

class SistemaController:
    def __init__(self):
        self.__sistema = Sistema()
        self.__sistemaView = SistemaView()
        self.__personagemController = PersonagemController()

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
            elif opcao == '0':
                self.__sistemaView.mostrar_mensagem("Saindo do sistema...")
                break
            else:
                self.__sistemaView.mostrar_mensagem("Opção inválida. Tente novamente.")


    def cadastrar_personagem(self):
        dados_personagem = None
        while dados_personagem is None:
            try:
                dados_personagem = self.__sistemaView.pega_dados_personagem()
                personagem_existente = self.__personagemController.pega_personagem_por_nome(dados_personagem["nome"])
                if personagem_existente is not None:
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
        personagens = self.__sistema.listar_personagens()
        self.__sistemaView.mostrar_personagens(personagens)

        escolha = self.__sistemaView.pegar_personagem_selecionado()
        if escolha.isdigit() and 1 <= int(escolha) <= len(personagens):
            personagem = personagens[int(escolha) - 1]  # Retorna a instância do personagem
            self.opcoes_personagem(personagem)
        else:
            self.__sistemaView.mostrar_mensagem("Escolha inválida.")
            return


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
            elif opcao == '0':
                break
            else:
                self.__sistemaView.mostrar_mensagem("Opção inválida. Tente novamente.")
