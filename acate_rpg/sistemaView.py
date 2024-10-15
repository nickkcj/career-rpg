
class SistemaView:
    def mostrar_menu(self):
        print("--------- MENU ---------")
        print("1 - Cadastrar Personagem")
        print("2 - Selecionar Personagem")
        print("0 - Sair")

    def mostrar_personagens(self, personagens):
        if not personagens:
            print("##############################")
            print(" Nenhum personagem cadastrado!")
            print("##############################")
            return
        print("--------- PERSONAGENS CADASTRADOS ---------")
        print("Selecione um personagem:")
        for idx, personagem in enumerate(personagens, start=1):
            print(f"{idx} - {personagem.nome} - Nível: {personagem.nivel} - Classe: {personagem.classe_personagem.nome_classe}")

    def pegar_personagem_selecionado(self):
        return input("Digite o número do personagem que deseja selecionar: ").strip()
    
    def pegar_opcao(self):
        return input("Escolha uma opção: ").strip()

    def pega_dados_personagem(self):
        print("----------CADASTRO PERSONAGEM---------")
        nome = input("Nome: ")
        if not isinstance(nome, str):
            raise Exception("Nome inválido")

        while True:
            print("-------- CLASSES ----------")
            print("Escolha uma classe:")
            print("1 - CLT (Bom no early game)")
            print("2 - Estagiário (Médio no early, bom no late)")
            print("3 - Trainee (Fraco no early, muito forte no late)")

            opcao = int(input("Digite o número da classe: "))

            if opcao == 1:
                classe = "CLT"
            elif opcao == 2:
                classe = "Estagiário"
            elif opcao == 3:
                classe = "Trainee"
            else:
                print("Classe inválida! Tente novamente.")
                continue

            break

        return {"nome": nome, 
                "classe": classe, 
                "nivel": 1, 
                "experiencia": 0
                }

    def mostrar_opcoes_personagem(self):
        print("\n--------- OPÇÕES DO PERSONAGEM ---------")
        print("1 - Mostrar Status")
        print("2 - Aumentar Atributo")
        print("3 - Usar Item")
        print("0 - Voltar ao menu principal")

    def mostrar_status(self, status):
        print("-------- STATUS ----------")
        for key, value in status.items():
            print(f"{key.capitalize()}: {value}")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)