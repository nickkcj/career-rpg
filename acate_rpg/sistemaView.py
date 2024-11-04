import os
import time
class SistemaView:
    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menu_inicial(self):
        self.limpar_terminal()
        print("##########################################")
        print("Bem vindo ao RPG do Mercado de Trabalho!!")
        print("##########################################")
        print("")
        print("Você quer ser um personagem, uma empresa, ou só quer ver o Ranking?")
        print("1 - Personagem")
        print("2 - Empresa")
        print("3 - Ranking")
        print("0 - Nah, sair")
        print("")

    def menu_principal_empresa(self):
        self.limpar_terminal()
        print("----------MENU PRINCIPAL---------")
        print("Bem vindo ao RPG do Mercado de Trabalho!!")
        print("1. Gerenciar Cursos")
        print("2. Gerenciar Empresas")
        print("3. Gerenciar Bosses")
        print("0. Sair")
        print("")

    def menu_empresa(self):
        self.limpar_terminal()
        print("--------- MENU EMPRESA ---------")
        print("Olá Empresa, o que você quer fazer?")
        print("1. Cadastrar Empresa")
        print("2. Ver Empresas")
        print("3. Alterar Empresa")
        print("4. Excluir Empresa")
        print("5. Gerenciar Cursos")
        print("0. Voltar")

    def menu_jogador(self):
        self.limpar_terminal()
        print("--------- MENU JOGADOR ---------")
        print("Olá Jogador, o que você quer fazer?")
        print("1 - Cadastrar Personagem")
        print("2 - Selecionar Personagem")
        print("0 - Sair")

    def menu_principal_personagem(self, nome_personagem):
        self.limpar_terminal()
        print("--------- MENU PRINCIPAL ---------")
        print(f"Olá {nome_personagem}, Bem vindo(a) ao RPG do Mercado de Trabalho!!")
        print("1 - Meu Personagem")
        print("2 - Batalha")
        print("3 - Cursos")
        print("4 - Gerenciar Log de Jogadas")
        print("0 - Voltar ao Menu Personagem")


    def menu_log(self):
        print("--------- MENU LOG ---------")
        print("1 - Ver Logs de Jogada")
        print("2 - Alterar Logs de Jogada")
        print("3 - Remover Logs de Jogada")
        print("4 - Voltar")
        


    def menu_ranking(self):
        self.limpar_terminal()
        print("\n------ MENU DE RANKING ------")
        print("1 - Ranking por Nível")
        print("2 - Ranking por Dungeons Conquistadas")
        print("3 - Ranking por Cursos Concluídos")
        print("0 - Voltar")

    def mostrar_personagens(self, personagens):
        self.limpar_terminal()
        if not personagens:
            print("##############################")
            print(" Nenhum personagem cadastrado!")
            print("##############################")
            time.sleep(2)
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
        self.limpar_terminal()
        print("----------CADASTRO PERSONAGEM---------")
        
        while True:
            nome = input("Nome: ").strip()
            if nome:
                break
            print("Nome inválido! Por favor, insira um nome válido.")

        while True:
            try:
                print("-------- CLASSES ----------")
                print("Escolha uma classe:")
                print("1 - CLT (Bom no early game)")
                print("2 - Estagiário (Médio no early, bom no late)")
                print("3 - Trainee (Fraco no early, muito forte no late)")

                opcao = int(input("Digite o número da classe: "))
                if opcao == 1:
                    classe = "CLT"
                elif opcao == 2:
                    classe = "Estagiario"
                elif opcao == 3:
                    classe = "Trainee"
                else:
                    print("Opção inválida! Escolha entre 1, 2, ou 3.")
                    continue
                break
            except ValueError:
                print("Entrada inválida! Digite um número para selecionar a classe.")

        return {
            "nome": nome,
            "classe": classe,
            "nivel": 1,
            "experiencia_total": 0
        }

    def mostrar_opcoes_personagem(self):
        print("\n--------- MEU PERSONAGEM ---------")
        print("1 - Mostrar Status")
        print("2 - Aumentar Atributo")
        print("3 - Usar Item")
        print("4 - Ver Habilidades")
        print("5 - Ganhar Experiência (TESTE)")
        print("6 - Voltar ao Menu Principal")
        print("0 - Voltar ao Menu Jogador")

    def mostrar_status(self, status):
        print("-------- STATUS ----------")
        for key, value in status.items():
            print(f"{key.capitalize()}: {value}")

    def mostrar_habilidades(self, habilidades):
        self.limpar_terminal()
        print("--------- HABILIDADES DO PERSONAGEM ---------")
        for habilidade in habilidades:
            print(f"{habilidade['nome']} - {habilidade['efeito']} ({habilidade['tipo']})")
        input("\nPressione Enter para voltar ao menu.")

    def mostrar_mensagem(self, msg):
        self.limpar_terminal()
        print("\n")
        print("****************************************")
        print(msg)
        print("****************************************")
        time.sleep(1)
