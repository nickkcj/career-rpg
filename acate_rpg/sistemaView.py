import os
import time
import PySimpleGUI as psg
class SistemaView:
    def __init__(self):
        self.window = None
        psg.theme("DarkBlue3")

    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def open(self):
        button, values = self.window.Read()
        return button, values
    
    def close(self):
        self.window.Close()

    def menu_inicial(self):
        psg.theme("DarkGreen5")  

        layout = [
            [psg.Text("Bem-vindo ao RPG do Mercado de Trabalho!!", 
                    justification='center', 
                    font=("Georgia", 36))],
            [psg.Image(filename="assets/images/background.jpg", size=(1000, 500), pad=(0, 20))],  # Aumentei o espaçamento entre o título e a imagem
            [psg.Button("Gerenciar Personagens", key="1", size=(15, 2), font=("Segoe UI", 16),pad=(2,20)),  
            psg.Button("Gerenciar\nDungeons", key="2", size=(15, 2), font=("Segoe UI", 16),pad=(2,20)), 
            psg.Button("Ver o Ranking", key="3", size=(15, 2), font=("Segoe UI", 16), pad=(2,20))],
            [psg.Button("Sair", key="0", size=(8, 1), font=("Segoe UI", 16))]  # Aumentei o espaçamento do botão "Sair"
        ] 

        self.window = psg.Window("Menu Inicial", layout, size=(1000, 800), element_justification='center', finalize=True, resizable=True)
        self.window.maximize()
        while True:
            event, _ = self.open()
            self.window.maximize()

            if event in ("0", psg.WINDOW_CLOSED):
                exit()
            
            return event

            

    def menu_principal_empresa(self):
        layout = [
            [psg.Text("--------- MENU PRINCIPAL DA EMPRESA ---------", font=("Helvetica", 20), justification="center")],
            [psg.Button("Gerenciar Cursos", key="1", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Gerenciar Empresas", key="2", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Gerenciar Bosses", key="3", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Sair", key="0", size=(30, 2), font=("Helvetica", 14))]
        ]

        self.window = psg.Window("Menu Principal Empresa", layout, finalize=True)
        while True:
            event, _ = self.window.read()
            if event in ("0", psg.WINDOW_CLOSED):
                self.window.close()
                return "0"
            return event

    def menu_empresa(self):
        layout = [
            [psg.Text("--------- MENU EMPRESA ---------", font=("Helvetica", 20), justification="center")],
            [psg.Button("Cadastrar Empresa", key="1", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Ver Empresas", key="2", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Alterar Empresa", key="3", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Excluir Empresa", key="4", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Gerenciar Cursos", key="5", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Voltar", key="0", size=(30, 2), font=("Helvetica", 14))]
        ]

        self.window = psg.Window("Menu Empresa", layout, finalize=True)
        while True:
            event, _ = self.window.read()
            if event in ("0", psg.WINDOW_CLOSED):
                self.window.close()
                return "0"
            return event

    def menu_jogador(self):
        layout = [
            [psg.Image("assets/images/personagem.jpg", size=(700, 450), pad=(0,30))],
            [psg.Text("--------- MENU JOGADOR ---------", font=("Helvetica", 16), justification="center")],
            [psg.Text("Olá Jogador, o que você quer fazer?", font=("Helvetica", 23), justification="center", pad=(0,10))],
            [psg.Button("Cadastrar Personagem", key="1", size=(50, 2), font=("Helvetica", 15), pad=(0,4))],
            [psg.Button("Selecionar Personagem", key="2", size=(50, 2), font=("Helvetica", 15), pad=(0,4))],
            [psg.Button("Sair", key="0", size=(50, 2), font=("Helvetica", 15), pad=(0,4))]
        ]

        
        self.window = psg.Window(
            "Menu Jogador", layout, element_justification="center", size=(1000, 800), finalize=True
        )
        
        self.window.maximize()

        while True:
            event, _ = self.window.read()

            if event in (psg.WINDOW_CLOSED, "0"):
                psg.popup("Fechando o jogo...")
                break

            
            else:
                return event
                

    def menu_principal_personagem(self, nome_personagem):
        layout = [
            [psg.Text(f"MENU PRINCIPAL DO PERSONAGEM: {nome_personagem}", font=("Arial", 20), justification="center")],
            [psg.Button("Status do Personagem", key="1", size=(25, 2))],
            [psg.Button("Explorar Dungeons", key="2", size=(25, 2))],
            [psg.Button("Realizar Quiz", key="3", size=(25, 2))],
            [psg.Button("Ver Log de Jogadas", key="4", size=(25, 2))],
            [psg.Button("Voltar ao Menu do Jogador", key="0", size=(25, 2))]
        ]
        window = psg.Window("Menu Principal do Personagem", layout, modal=True)
        while True:
            event, _ = window.read()
            if event in ["0", psg.WIN_CLOSED]:
                window.close()
                return "0"
            if event in ["1", "2", "3", "4"]:
                window.close()
                return event


    def menu_log(self):
        layout = [
            [psg.Text("--------- MENU LOG ---------", font=("Helvetica", 20), justification="center")],
            [psg.Button("Ver Logs de Jogada", key="1", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Alterar Logs de Jogada", key="2", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Remover Logs de Jogada", key="3", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Voltar", key="4", size=(30, 2), font=("Helvetica", 14))]
        ]

        self.window = psg.Window("Menu Log", layout, finalize=True)
        while True:
            event, _ = self.window.read()
            if event in ("0", psg.WINDOW_CLOSED):
                self.window.close()
                return "0"
            return event
        


    def menu_ranking(self):
        layout = [
            [psg.Text("------ MENU DE RANKING ------", font=("Helvetica", 20), justification="center")],
            [psg.Button("Ranking por Nível", key="1", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Ranking por Dungeons Conquistadas", key="2", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Ranking por Cursos Concluídos", key="3", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Voltar", key="0", size=(30, 2), font=("Helvetica", 14))]
        ]

        self.window = psg.Window("Menu Ranking", layout, finalize=True)
        while True:
            event, _ = self.window.read()
            if event in ("0", psg.WINDOW_CLOSED):
                self.window.close()
                return "0"
            return event

    def mostrar_personagens(self, personagens):
        if not personagens:
            psg.popup("Nenhum personagem cadastrado!", title="Aviso")
            return

        banner_path = "assets/images/banner1.png"  

        layout = [
        [
            psg.Column(
                [[psg.Image(banner_path, size=(157, 800))]],  # Banner esquerdo
                pad=(0, 30),
                element_justification="center",
                vertical_alignment="center",
                size=(157, 800),
            ),
            psg.Column(
                [
                    [psg.Text("--------- PERSONAGENS CADASTRADOS ---------", font=("Helvetica", 20), justification="center", pad=(0, 20))],
                    [psg.Text("Selecione um personagem:", font=("Helvetica", 14), justification="left", pad=(0, 10))],
                    [
                        psg.Listbox(
                            values=[
                                f"{idx} - {personagem.nome} - Nível: {personagem.nivel} - Classe: {personagem.classe_personagem.nome_classe}"
                                for idx, personagem in enumerate(personagens, start=1)
                            ],
                            size=(50, 20),
                            key="personagem_selecionado",
                            font=("Helvetica", 14),
                            enable_events=True,
                            select_mode=psg.LISTBOX_SELECT_MODE_SINGLE,
                        )
                    ],
                    [
                        psg.Button("Confirmar", size=(15, 1), font=("Helvetica", 14)),
                        psg.Button("Cancelar", size=(15, 1), font=("Helvetica", 14)),
                    ],
                ],
                element_justification="center",
                vertical_alignment="center",
                pad=(20, 0),
            ),
            psg.Column(
                [[psg.Image(banner_path, size=(157, 800))]],  # Banner direito
                pad=(0, 30),
                element_justification="center",
                vertical_alignment="center",
                size=(157, 800),
            ),
        ]
    ]

        window = psg.Window(
            "Personagens Cadastrados",
            layout,
            element_justification="center",
            size=(1200, 800),
            finalize=True,
            resizable=True,
        )


        while True:
            event, values = self.window.read()

            if event in (psg.WINDOW_CLOSED, "Cancelar"):
                psg.popup("Operação cancelada!", title="Aviso")
                self.window.close()
                return None

            if event == "Confirmar":
                personagem_selecionado = values["personagem_selecionado"]

                if not personagem_selecionado:
                    psg.popup("Por favor, selecione um personagem!", title="Erro")
                else:
                    idx_selecionado = int(personagem_selecionado[0].split(" - ")[0]) - 1
                    self.window.close()
                    return personagens[idx_selecionado]

    def pega_dados_personagem(self):
        layout = [
            [psg.Text("---------- CADASTRO DE PERSONAGEM ---------", font=("Helvetica", 20), justification="center", pad=(0, 20))],
            [psg.Text("Nome:", font=("Helvetica", 14), justification="left", pad=(0, 10))],
            [psg.InputText(key="nome", size=(30, 1), font=("Helvetica", 14))],
            [psg.Text("Escolha uma classe:", font=("Helvetica", 14), justification="left", pad=(0, 10))],
            [psg.Combo(
                ["CLT (Bom no early game)", "Estagiário (Médio no early, bom no late)", "Trainee (Fraco no early, muito forte no late)"],
                key="classe", 
                readonly=True, 
                size=(40, 1),
                font=("Helvetica", 14)
            )],
            [psg.Button("Confirmar", size=(15, 1), font=("Helvetica", 14)), psg.Button("Cancelar", size=(15, 1), font=("Helvetica", 14))]
        ]

        self.window = psg.Window(
            "Cadastro de Personagem", 
            layout, 
            element_justification="center", 
            size=(600, 400), 
            finalize=True
        )

        while True:
            event, values = self.window.read()

            if event in (psg.WINDOW_CLOSED, "Cancelar"):
                psg.popup("Cadastro cancelado!")
                self.window.close()
                return None

            if event == "Confirmar":
                nome = values["nome"].strip()
                classe = values["classe"]

                if not nome:
                    psg.popup("Por favor, insira um nome válido!", title="Erro")
                elif not classe:
                    psg.popup("Por favor, escolha uma classe!", title="Erro")
                else:
                    classe_nome = classe.split(" ")[0]
                    psg.popup("Personagem cadastrado com sucesso!")
                    self.window.close()
                    return {
                        "nome": nome,
                        "classe": classe_nome,
                        "nivel": 1,
                        "experiencia_total": 0
                    }

    def mostrar_opcoes_personagem(self):
        layout = [
            [psg.Text("--------- MEU PERSONAGEM ---------", font=("Helvetica", 20), justification="center")],
            [psg.Button("Mostrar Status", key="1", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Aumentar Atributo", key="2", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Usar Item", key="3", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Ver Habilidades", key="4", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Ganhar Experiência (TESTE)", key="5", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Voltar ao Menu Principal", key="6", size=(30, 2), font=("Helvetica", 14))],
            [psg.Button("Voltar ao Menu Jogador", key="0", size=(30, 2), font=("Helvetica", 14))]
        ]

        self.window = psg.Window("Opções do Personagem", layout, finalize=True)
        while True:
            event, _ = self.window.read()
            if event in ("0", "6", psg.WINDOW_CLOSED):
                self.window.close()
                return event
            return event

    def mostrar_mensagem(self, msg):
        layout = [
            [psg.Text("**************************************************", text_color="white", background_color="blue", font=("Helvetica", 12), justification="center")],
            [psg.Text(msg, text_color="yellow", background_color="blue", font=("Helvetica", 14, "bold"), justification="center")],
            [psg.Text("**************************************************", text_color="white", background_color="blue", font=("Helvetica", 12), justification="center")],
            [psg.Button("OK", key="OK", size=(10, 1), button_color=("white", "green"))]
        ]

        janela = psg.Window("Mensagem", layout, modal=True, background_color="blue", element_justification="center")

        while True:
            evento, _ = janela.read()
            if evento in (psg.WINDOW_CLOSED, "OK"):
                break

        janela.close()

