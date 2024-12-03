import os
import time
import PySimpleGUI as sg
class SistemaView:
    def __init__(self):
        self.window = None

    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def open(self):
        button, values = self.window.Read()
        return button, values
    
    def close(self):
        self.window.Close()

    def menu_inicial(self):
        sg.theme("DarkGreen5")  

        layout = [
            [sg.Text("Bem-vindo ao RPG do Mercado de Trabalho!!", 
                    justification='center', 
                    font=("Georgia", 36))],
            [sg.Image(filename="assets/images/background.jpg", size=(1000, 500), pad=(0, 20))],  # Aumentei o espaçamento entre o título e a imagem
            [sg.Button("Gerenciar Personagens", key="1", size=(15, 2), font=("Segoe UI", 16),pad=(2,20)),  
            sg.Button("Gerenciar\nDungeons", key="2", size=(15, 2), font=("Segoe UI", 16),pad=(2,20)), 
            sg.Button("Ver o Ranking", key="3", size=(15, 2), font=("Segoe UI", 16), pad=(2,20))],
            [sg.Button("Sair", key="0", size=(8, 1), font=("Segoe UI", 16))]  # Aumentei o espaçamento do botão "Sair"
        ] 

        self.window = sg.Window("Menu Inicial", layout, size=(1000, 800), element_justification='center', finalize=True, resizable=True)
        self.window.maximize()
        while True:
            event, _ = self.open()
            self.window.maximize()

            if event in ("0", sg.WINDOW_CLOSED):
                exit()
            
            return event

            

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
        layout = [
            [sg.Image("assets/images/personagem.jpg", size=(700, 450), pad=(0,30))],
            [sg.Text("--------- MENU JOGADOR ---------", font=("Helvetica", 16), justification="center")],
            [sg.Text("Olá Jogador, o que você quer fazer?", font=("Helvetica", 23), justification="center", pad=(0,10))],
            [sg.Button("Cadastrar Personagem", key="1", size=(50, 2), font=("Helvetica", 15), pad=(0,4))],
            [sg.Button("Selecionar Personagem", key="2", size=(50, 2), font=("Helvetica", 15), pad=(0,4))],
            [sg.Button("Sair", key="0", size=(50, 2), font=("Helvetica", 15), pad=(0,4))]
        ]

        
        self.window = sg.Window(
            "Menu Jogador", layout, element_justification="center", size=(1000, 800), finalize=True
        )
        
        self.window.maximize()

        while True:
            event, _ = self.window.read()

            if event in (sg.WINDOW_CLOSED, "0"):
                sg.popup("Fechando o jogo...")
                break

            
            else:
                return event
                

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
        if not personagens:
            sg.popup("Nenhum personagem cadastrado!", title="Aviso")
            return

        banner_path = "assets/images/banner1.png"  

        layout = [
        [
            sg.Column(
                [[sg.Image(banner_path, size=(157, 800))]],  # Banner esquerdo
                pad=(0, 30),
                element_justification="center",
                vertical_alignment="center",
                size=(157, 800),
            ),
            sg.Column(
                [
                    [sg.Text("--------- PERSONAGENS CADASTRADOS ---------", font=("Helvetica", 20), justification="center", pad=(0, 20))],
                    [sg.Text("Selecione um personagem:", font=("Helvetica", 14), justification="left", pad=(0, 10))],
                    [
                        sg.Listbox(
                            values=[
                                f"{idx} - {personagem.nome} - Nível: {personagem.nivel} - Classe: {personagem.classe_personagem.nome_classe}"
                                for idx, personagem in enumerate(personagens, start=1)
                            ],
                            size=(50, 20),
                            key="personagem_selecionado",
                            font=("Helvetica", 14),
                            enable_events=True,
                            select_mode=sg.LISTBOX_SELECT_MODE_SINGLE,
                        )
                    ],
                    [
                        sg.Button("Confirmar", size=(15, 1), font=("Helvetica", 14)),
                        sg.Button("Cancelar", size=(15, 1), font=("Helvetica", 14)),
                    ],
                ],
                element_justification="center",
                vertical_alignment="center",
                pad=(20, 0),
            ),
            sg.Column(
                [[sg.Image(banner_path, size=(157, 800))]],  # Banner direito
                pad=(0, 30),
                element_justification="center",
                vertical_alignment="center",
                size=(157, 800),
            ),
        ]
    ]

        window = sg.Window(
            "Personagens Cadastrados",
            layout,
            element_justification="center",
            size=(1200, 800),
            finalize=True,
            resizable=True,
        )


        while True:
            event, values = self.window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                sg.popup("Operação cancelada!", title="Aviso")
                self.window.close()
                return None

            if event == "Confirmar":
                personagem_selecionado = values["personagem_selecionado"]

                if not personagem_selecionado:
                    sg.popup("Por favor, selecione um personagem!", title="Erro")
                else:
                    idx_selecionado = int(personagem_selecionado[0].split(" - ")[0]) - 1
                    self.window.close()
                    return personagens[idx_selecionado]



    def pegar_personagem_selecionado(self):
        return input("Digite o número do personagem que deseja selecionar: ").strip()
    
    def pegar_opcao(self):
        return input("Escolha uma opção: ").strip()

    def pega_dados_personagem(self):
        layout = [
            [sg.Text("---------- CADASTRO DE PERSONAGEM ---------", font=("Helvetica", 20), justification="center", pad=(0, 20))],
            [sg.Text("Nome:", font=("Helvetica", 14), justification="left", pad=(0, 10))],
            [sg.InputText(key="nome", size=(30, 1), font=("Helvetica", 14))],
            [sg.Text("Escolha uma classe:", font=("Helvetica", 14), justification="left", pad=(0, 10))],
            [sg.Combo(
                ["CLT (Bom no early game)", "Estagiário (Médio no early, bom no late)", "Trainee (Fraco no early, muito forte no late)"],
                key="classe", 
                readonly=True, 
                size=(40, 1),
                font=("Helvetica", 14)
            )],
            [sg.Button("Confirmar", size=(15, 1), font=("Helvetica", 14)), sg.Button("Cancelar", size=(15, 1), font=("Helvetica", 14))]
        ]

        self.window = sg.Window(
            "Cadastro de Personagem", 
            layout, 
            element_justification="center", 
            size=(600, 400), 
            finalize=True
        )

        while True:
            event, values = self.window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                sg.popup("Cadastro cancelado!")
                self.window.close()
                return None

            if event == "Confirmar":
                nome = values["nome"].strip()
                classe = values["classe"]

                if not nome:
                    sg.popup("Por favor, insira um nome válido!", title="Erro")
                elif not classe:
                    sg.popup("Por favor, escolha uma classe!", title="Erro")
                else:
                    classe_nome = classe.split(" ")[0]
                    sg.popup("Personagem cadastrado com sucesso!")
                    self.window.close()
                    return {
                        "nome": nome,
                        "classe": classe_nome,
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
