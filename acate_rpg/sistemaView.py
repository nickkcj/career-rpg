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
        self.window.close()

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





    def menu_inicial(self):
        sg.theme("DarkGreen4")

        layout = [
            [psg.Text("Bem-vindo ao RPG do Mercado de Trabalho!!", 
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

        self.window = psg.Window("Menu Inicial", layout, size=(1000, 800), element_justification='center', finalize=True, resizable=True)
        self.window.maximize()

        while True:
            event, _ = self.window.read()

            if event in ("0", sg.WINDOW_CLOSED):
                self.window.close()
                exit()  

            self.window.close()  
            return event
  
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
                break
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

            if event in (sg.WINDOW_CLOSED, "0"):
                sg.popup("Fechando o jogo...")
                self.window.close()
                break

            
            else:
                self.window.close()
                return event
        
        self.window.close()
                

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

        while True:
            event, _ = self.window.read()
            if event in ('-EXIT-', sg.WINDOW_CLOSED):
                self.window.close()
                return None
                
            
            else:
                return event
            

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
            if event in ('4', sg.WINDOW_CLOSED):  
                self.window.close()
                break
            self.window.close()
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

        self.window = sg.Window(
            "Personagens Cadastrados",
            layout,
            element_justification="center",
            size=(1200, 800),
            finalize=True,
            resizable=True,
        )

        self.window.maximize()


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
            [sg.Text("--------- MEU PERSONAGEM ---------", font=("Helvetica", 16), justification='center')],
            [sg.Button("1 - Mostrar Status", key='1')],
            [sg.Button("2 - Aumentar Atributo", key='2')],
            [sg.Button("3 - Usar Item", key='3')],
            [sg.Button("4 - Ver Habilidades", key='4')],
            [sg.Button("5 - Ganhar Experiência (TESTE)", key='5')],
            [sg.Button("6 - Voltar ao Menu Principal", key='6')],
            [sg.Button("0 - Voltar ao Menu Jogador", key='0')],
            [sg.Button("Sair", key='-EXIT-')]
        ]

        window = sg.Window("Meu Personagem", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in ('-EXIT-', sg.WINDOW_CLOSED):
                window.close()
                return None
                
            else:
                window.close()
                return event

    def mostrar_status(self, status):
        status_str = "\n".join([f"{key.capitalize()}: {value}" for key, value in status.items()])

        layout = [
            [sg.Text("-------- STATUS --------", font=("Helvetica", 16), justification='center')],
            [sg.Multiline(status_str, size=(40, 10), disabled=True, autoscroll=True)],
            [sg.Button("Voltar", key='-BACK-')]
        ]

        window = sg.Window("Status do Personagem", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in ('-BACK-', sg.WINDOW_CLOSED):
                break
        window.close()

    def mostrar_habilidades(self, habilidades):
        habilidades_str = "\n".join([f"{h['nome']} - {h['efeito']} ({h['tipo']})" for h in habilidades])

        layout = [
            [sg.Text("--------- HABILIDADES DO PERSONAGEM ---------", font=("Helvetica", 16), justification='center')],
            [sg.Multiline(habilidades_str, size=(50, 10), disabled=True, autoscroll=True)],
            [sg.Button("Voltar", key='-BACK-')]
        ]

        window = sg.Window("Habilidades do Personagem", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in ('-BACK-', sg.WINDOW_CLOSED):
                window.close()
                break
        window.close()

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

