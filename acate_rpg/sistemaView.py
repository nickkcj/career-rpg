import os
import time
import PySimpleGUI as sg
class SistemaView:
    def __init__(self):
        self.window = None
        sg.theme("DarkBlue3")

    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def open(self):
        button, values = self.window.Read()
        return button, values
    
    def close(self):
        self.window.close()

    def menu_inicial(self):
        sg.theme("DarkGreen4")

        layout = [
            [sg.Text("Bem-vindo ao RPG do Mercado de Trabalho!!", 
                    justification='center', 
                    font=("Georgia", 36), 
                    expand_x=True)],
            [sg.Column([[sg.Image(filename="assets/images/background.jpg", size=(1000, 500))]], 
                    justification='center', expand_x=True, element_justification='center')],
            [sg.Column([
                [sg.Button("Gerenciar Personagens", key="1", size=(20, 2), font=("Segoe UI", 16)),
                sg.Button("Gerenciar Dungeons", key="2", size=(20, 2), font=("Segoe UI", 16))],
                [sg.Button("Ver o Ranking", key="3", size=(20, 2), font=("Segoe UI", 16)),
                sg.Button("Sair", key="0", size=(20, 2), font=("Segoe UI", 16))]
            ], justification='center', element_justification='center', pad=(0, 20))]
        ]

        self.window = sg.Window("Menu Inicial", layout, size=(1000, 800), element_justification='center', finalize=True, resizable=True)
        self.window.maximize()

        evento, _ = self.window.read()
        self.window.close()  # Feche a janela antes de retornar
        return evento

        
  
    def menu_principal_empresa(self):
        layout = [
            [sg.Text("----------MENU PRINCIPAL---------", font=("Helvetica", 30), justification="center", expand_x=True)],
            [sg.Text("Bem-vindo ao RPG do Mercado de Trabalho!!", font=("Helvetica", 20), justification="center", expand_x=True)],
            [sg.Button("Gerenciar Cursos", size=(20, 2), key='1')],
            [sg.Button("Gerenciar Empresas", size=(20, 2), key='2')],
            [sg.Button("Gerenciar Bosses", size=(20, 2), key='3')],
            [sg.Button("Sair", size=(20, 2), key='0')]
        ]
        self.window = sg.Window("Menu Principal", layout, size=(1000, 800), element_justification="center", finalize=True, resizable=True)

        while True:
            event, _ = self.window.read()
            if event in ('0', sg.WINDOW_CLOSED):
                self.window.close()
                exit()
            self.window.close()
            return event

    def menu_empresa(self):
        layout = [
            [sg.VPush()],
            [
                sg.Push(),
                sg.Image(
                    source="assets/images/dungeon.jpg", 
                    size=(650, 650),  
                    key="IMAGE"
                ),
                sg.Column(
                    [
                        [sg.Text("--------- MENU DUNGEON ---------", font=("Helvetica", 30), justification="center", expand_x=True)],
                        [sg.Text("Olá Mr.Dungeon, o que você quer fazer?", font=("Helvetica", 20), justification="center", expand_x=True, pad=(0, 20))],
                        [sg.Button("Cadastrar Dungeon", size=(55, 3), key='1', pad=(0, 10), font=("Helvetica", 13))],
                        [sg.Button("Ver Dungeons", size=(55, 3), key='2', pad=(0, 10), font=("Helvetica", 13))],
                        [sg.Button("Alterar Dungeon", size=(55, 3), key='3', pad=(0, 10), font=("Helvetica", 13))],
                        [sg.Button("Excluir Dungeon", size=(55, 3), key='4', pad=(0, 10), font=("Helvetica", 13))],
                        [sg.Button("Gerenciar Cursos", size=(55, 3), key='5', pad=(0, 10), font=("Helvetica", 13))],
                        [sg.Button("Voltar", size=(55, 3), key='0', pad=(0, 10), font=("Helvetica", 13))]
                    ],
                    element_justification="center",
                    vertical_alignment="center",
                    pad=(20, 20)
                ),
                sg.Push()
            ],
            [sg.VPush()]
        ]

        self.window = sg.Window(
            "Menu Dungeons",
            layout,
            size=(1000, 800),
            element_justification="center",
            finalize=True,
            resizable=True
        )

        self.window.maximize()

        while True:
            event, _ = self.window.read()
            if event in (None, sg.WINDOW_CLOSED):
                self.window.close()
                break

            self.window.close()
            return event



    def menu_jogador(self):
        screen_width, screen_height = sg.Window.get_screen_size()
        layout = [
            [sg.Image("assets/images/personagem.jpg", size=(500, 320), pad=(0, 23))],
            [sg.Text("--------- MENU JOGADOR ---------", font=("Helvetica", 16), justification="center", pad=(0, 5))],
            [sg.Text("Olá Jogador, o que você quer fazer?", font=("Helvetica", 23), justification="center", pad=(0, 20))],
            [sg.Column(
                [
                    [sg.Button("Cadastrar Personagem", key="1", size=(40, 1), font=("Helvetica", 15), pad=(0, 10))],
                    [sg.Button("Selecionar Personagem", key="2", size=(40, 1), font=("Helvetica", 15), pad=(0, 10))],
                    [sg.Button("Alterar Dados de Personagem", key="3", size=(40, 1), font=("Helvetica", 15), pad=(0, 10))],
                    [sg.Button("Excluir Personagem", key="4", size=(40, 1), font=("Helvetica", 15), pad=(0, 10))],
                    [sg.Button("Voltar", key="0", size=(40, 1), font=("Helvetica", 15), pad=(0, 10))]
                ],
                element_justification="center",
                vertical_alignment="center",
                expand_y=True,
            )]
        ]

        self.window = sg.Window(
            "Menu Jogador", layout, element_justification="center", size=(screen_width // 2, screen_height // 2), finalize=True, resizable=True
        )
        
        self.window.maximize()

        evento, _ = self.window.read()
        self.window.close()  # Feche a janela antes de retornar
        if evento is None:
            return "0"
        return evento
                

    def menu_principal_personagem(self, nome_personagem):
        layout = [
            [sg.Text(f"Olá {nome_personagem}, Bem-vindo(a) ao RPG do Mercado de Trabalho!",
                    size=(40, 2), font=("Helvetica", 25), justification='center', expand_x=True)],
            [sg.Column([[sg.Image('assets/images/status.jpg', size=(600, 500))]], 
                    justification='center', expand_x=True, element_justification='center', pad=(0, 0))],
            [sg.Column([
                [sg.Button("Meu Personagem", key='1', size=(25, 4), pad=(5, 10)), 
                sg.Button("Batalha", key='2', size=(25, 4), pad=(5, 10)), 
                sg.Button("Cursos", key='3', size=(25, 4), pad=(5, 10))],
                [sg.Button("Gerenciar Log de Jogadas", key='4', size=(25, 4), pad=(5, 10)), 
                sg.Button("Voltar ao Menu Personagem", key='0', size=(25, 4), pad=(5, 10)), 
                sg.Button("Sair", key='-EXIT-', size=(25, 4), pad=(5, 10))]
            ], justification='center', element_justification='center', pad=(0, 20))]
        ]

        self.window = sg.Window("Menu Principal", layout, size=(1000, 850), element_justification='center', finalize=True, resizable=True)
        self.window.maximize()
        evento, _ = self.window.read()
        self.window.close()
        return evento
                

    def menu_log(self):
        layout = [
            [sg.Text("--------- MENU LOG ---------", font=("Helvetica", 20), justification="center")],
            [sg.Button("Ver Logs de Jogada", size=(30, 2), key='1', font=("Helvetica", 14))],
            [sg.Button("Alterar Logs de Jogada", size=(30, 2), key='2', font=("Helvetica", 14))],
            [sg.Button("Remover Logs de Jogada", size=(30, 2), key='3', font=("Helvetica", 14))],
            [sg.Button("Voltar", size=(30, 2), key='4', font=("Helvetica", 14))]
        ]

        self.window = sg.Window(
            "Menu Log",
            layout,
            element_justification="center",
            finalize=True
        )

        while True:
            event, _ = self.window.read()
            if event == sg.WINDOW_CLOSED:  
                self.window.close()
                break
            self.window.close()
            return event

    def menu_cursos(self):
        # Layout ajustado com elementos maiores
        layout = [
            [sg.VPush()],  # Espaço para empurrar verticalmente
            [sg.Text("Menu de Cursos", justification="center", font=("Helvetica", 30), pad=(0, 10), expand_x=True)],  # Fonte maior
            [sg.Image(filename="assets/images/menu_curso.jpg", size=(900, 500), pad=(0, 30))],  # Imagem maior
            
            # Botões em duas colunas com tamanhos maiores
            [sg.Push(), sg.Button("Lista de Cursos", key="1", size=(24, 4), font=("Helvetica", 16)), 
            sg.Button("Cadastrar Curso", key="2", size=(24, 4), font=("Helvetica", 16)), sg.Push()],
            [sg.Push(), sg.Button("Alterar Curso", key="3", size=(24, 4), font=("Helvetica", 16)), 
            sg.Button("Excluir Curso", key="4", size=(24, 4), font=("Helvetica", 16)), sg.Push()],
            
            # Botão "Voltar" centralizado, maior e destacado
            [sg.Push(), sg.Button("Voltar", key="5", size=(24, 4), font=("Helvetica", 16), button_color=("white", "firebrick"), pad=(0, 40)), sg.Push()],
            [sg.VPush()],  # Espaço adicional abaixo para centralização
        ]

        # Janela com título e configuração
        window = sg.Window(
            "Menu de Cursos", 
            layout, 
            return_keyboard_events=True, 
            finalize=True, 
            element_justification='center',  # Centraliza horizontalmente
            resizable=True
        )
        window.maximize()
        event, _ = window.read()
        window.close()

        return event

    def menu_ranking(self):
        layout = [
            [sg.Text("------ MENU DE RANKING ------", font=("Helvetica", 20), justification="center")],
            [sg.Button("Ranking por Nível", size=(30, 2), key='1', font=("Helvetica", 14))],
            [sg.Button("Ranking por Dungeons Conquistadas", size=(30, 2), key='2', font=("Helvetica", 14))],
            [sg.Button("Ranking por Cursos Concluídos", size=(30, 2), key='3', font=("Helvetica", 14))],
            [sg.Button("Voltar", size=(30, 2), key='0', font=("Helvetica", 14))]
        ]

        self.window = sg.Window(
            "Menu Ranking",
            layout,
            element_justification="center",
            finalize=True
        )

        while True:
            event, _ = self.window.read()
            if event in ('0', sg.WINDOW_CLOSED):  
                self.window.close()
                return event
            self.window.close()
            return event

    def mostrar_opcoes_personagem(self):
        layout = [
            [sg.Text("--------- MEU PERSONAGEM ---------", font=("Helvetica", 16), justification='center')],
            [sg.Button("1 - Mostrar Status", key='1')],
            [sg.Button("2 - Aumentar Atributo", key='2')],
            [sg.Button("3 - Usar Item", key='3')],
            [sg.Button("4 - Ver Habilidades", key='4')],
            [sg.Button("5 - Ganhar Experiência (TESTE)", key='5')],
            [sg.Button("6 - Voltar ao Menu Principal", key='6')],
            [sg.Button("0 - Voltar ao Menu Jogador", key='0')],
            [sg.Button("Sair", key='6')]
        ]

        window = sg.Window("Meu Personagem", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in ('-EXIT-', sg.WINDOW_CLOSED):
                window.close()
                exit()
                
            else:
                window.close()
                return event

    def mostrar_mensagem(self, msg):
        layout = [
            [sg.Text("**************************************************", text_color="white", background_color="blue", font=("Helvetica", 12), justification="center")],
            [sg.Text(msg, text_color="yellow", background_color="blue", font=("Helvetica", 14, "bold"), justification="center")],
            [sg.Text("**************************************************", text_color="white", background_color="blue", font=("Helvetica", 12), justification="center")],
            [sg.Button("OK", key="OK", size=(10, 1), button_color=("white", "green"))]
        ]

        janela = sg.Window("Mensagem", layout, modal=True, background_color="blue", element_justification="center")

        while True:
            evento, _ = janela.read()
            if evento in (sg.WINDOW_CLOSED, "OK"):
                break

        janela.close()

