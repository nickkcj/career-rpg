import PySimpleGUI as sg
import time
class DungeonView:
    def pega_dados_dungeon(self):
        layout = [
            [sg.Text("------DADOS DA EMPRESA------", font=("Helvetica", 20))],
            [sg.Text("Digite o nome da empresa:"), sg.InputText(key="NOME")],
            [sg.Text("Digite o nível requerido da empresa:"),
            sg.Combo([str(i) for i in range(1, 11)], key="NIVEL_REQUERIDO", default_value="1")],
            [sg.Text("Quanto de XP essa empresa vale?"),
            sg.Combo([str(i) for i in range(1, 1000, 100)], key="XP_GANHO", default_value="1")],
            [sg.Text("Digite o número de setores desta empresa:"),
            sg.Combo([str(i) for i in range(1, 11)], key="N_SETOR", default_value="1")],
            [sg.Button("Confirmar", size=(10, 2)), sg.Button("Cancelar", size=(10, 2))]
        ]

        window = sg.Window("Cadastro de Dungeon", layout, modal=True)
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return 
            if event == "Confirmar":
                try:
                    nivel_requerido_str = values["NIVEL_REQUERIDO"]
                    xp_ganho_str = values["XP_GANHO"]
                    n_setores_str = values["N_SETOR"]

                    if not nivel_requerido_str.isdigit() or not xp_ganho_str.isdigit() or not n_setores_str.isdigit():
                        sg.popup_error("Por favor, insira apenas números inteiros válidos nos campos.")
                        continue

                    nivel_requerido = int(nivel_requerido_str)
                    xp_ganho = int(xp_ganho_str)
                    n_setores = int(n_setores_str)
  
                    window.close()
                    return {
                        "nome": values["NOME"],
                        "nivel_requerido": nivel_requerido,
                        "xp_ganho": xp_ganho,
                        "n_setores": n_setores,
                    }

                except ValueError:
                    sg.popup_error("Por favor, insira valores válidos. Os campos 'Nível Requerido', 'XP Ganho' e 'Número de Setores' devem ser números inteiros.")

            
        
    def pega_nome_boss_final(self):
        layout = [
            [sg.Text("Digite o nome do Boss Final da Dungeon:")],
            [sg.InputText(key="BOSS_FINAL")],
            [sg.Button("Confirmar", size=(10, 2)), sg.Button("Cancelar", size=(10, 2))]
        ]

        window = sg.Window("Nome do Boss Final", layout, modal=True, element_justification='center')
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Confirmar":
                sg.popup("Dungeon cadastrada com sucesso!")
                window.close()
                return values["BOSS_FINAL"]
            

    def pega_nome_dungeon(self):
        layout = [
            [sg.Text("Digite o nome da empresa que deseja selecionar:")],
            [sg.InputText(key="DUNGEON_NAME")],
            [sg.Button("Confirmar", size=(10, 2)), sg.Button("Cancelar", size=(10, 2))]
        ]

        window = sg.Window("Seleção de Dungeon", layout, modal=True, size=(400,200))
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Confirmar":
                window.close()
                return values["DUNGEON_NAME"]

    def pega_atributo_alteracao(self):
        layout = [
            [sg.Text("Digite o nome do atributo a ser alterado ou 'todos' para alterar tudo:")],
            [sg.InputText(key="ATRIBUTO")],
            [sg.Button("Confirmar", size=(10, 2)), sg.Button("Cancelar", size=(10, 2))]
        ]

        window = sg.Window("Alteração de Atributo", layout, modal=True)
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Confirmar":
                return values["ATRIBUTO"]

    def confirma_exclusao(self, dungeon_nome):
        layout = [
            [sg.Text(f"Tem certeza que deseja excluir a empresa '{dungeon_nome}'? (s/n):")],
            [sg.Button("Sim", size=(10, 2)), sg.Button("Não", size=(10, 2))]
        ]
        window = sg.Window("Confirmar Exclusão", layout, modal=True)
        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Não"):
                window.close()
                return False
            if event == "Sim":
                window.close()
                return True

    def mostra_mensagem(self, msg):
        sg.popup(msg, title="Mensagem")

    def mensagem_basica(self, msg):
        sg.popup(msg, title="Aviso")

    def mostra_dungeons_enum(self, dungeons):
        
        dungeons_formatadas = [
            f"{idx + 1}. Nome: {dungeon['nome']}, Nível Requerido: {dungeon['nivel_requerido']}"
            for idx, dungeon in enumerate(dungeons)
        ]

        
        layout = [
            [sg.Text("Selecione uma Dungeon:")],
            [
                sg.Listbox(
                    values=dungeons_formatadas,
                    size=(40, 10),
                    key="DUNGEONS_LIST",
                    select_mode=sg.LISTBOX_SELECT_MODE_SINGLE
                )
            ],
            [sg.Button("Confirmar", key="confirmar", size=(10, 2)), sg.Button("Cancelar", key="cancelar", size=(10, 2))]
        ]

        
        window = sg.Window("Lista de Dungeons", layout, modal=True, finalize=True)

        while True:
            event, values = window.read()

            if event in ("cancelar", sg.WINDOW_CLOSED):
                window.close()
                return None

            if event == "confirmar":
                
                if values["DUNGEONS_LIST"]:
                    opcao_selecionada = int(values["DUNGEONS_LIST"][0].split(".")[0]) - 1
                    window.close()
                    return opcao_selecionada
                else:
                    sg.popup("Por favor, selecione uma dungeon.")

        
    def mostra_dungeon(self, dungeons):
        layout = [
            [sg.Text("--- TODAS AS DUNGEONS ---", font=("Helvetica", 20))],
        ]

        for dungeon in dungeons:
            dungeon_layout = [
                [sg.Text(f"--- DUNGEON: {dungeon['nome']} ---", font=("Helvetica", 16))],
                [sg.Text(f"Nível Requerido: {dungeon['nivel_requerido']}")],
                [sg.Text(f"XP Ganho: {dungeon['xp_ganho']}")],
                [sg.Text(f"Dificuldade: {dungeon['dificuldade']}")],
                [sg.Text("Setores:")],
            ]

            
            for setor in dungeon["setores"]:
                dungeon_layout.append([
                    sg.Text(f" - Setor: {setor['nome']} (Dificuldade: {setor['dificuldade']})\n"
                            f"   Diretor: {setor['boss']['nome']} - Dificuldade: {setor['boss']['dificuldade']} - "
                            f"Nível: {setor['boss']['nivel_requerido']}")
                ])

            
            dungeon_layout.append([
                sg.Text(f"Diretor Geral: {dungeon['boss_final']['nome']} - Dificuldade: {dungeon['boss_final']['dificuldade']} - "
                        f"Nível: {dungeon['boss_final']['nivel_requerido']}")
            ])
            dungeon_layout.append([sg.HorizontalSeparator()])
            layout.extend(dungeon_layout)

        layout.append([sg.Button("Voltar", size=(10, 2))])

       
        window = sg.Window(
            "Lista de Dungeons",
            [[sg.Column(layout, scrollable=True, vertical_scroll_only=True, size=(800, 500))]],
            modal=True,
            finalize=True
        )

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Voltar"):
                window.close()
                break


    
    def capturar_entrada(self, tipo):
        layout = [
            [sg.Text(tipo)],
            [sg.InputText(key="entrada")],
            [sg.Button("Confirmar"), sg.Button("Cancelar")]
        ]
        window = sg.Window("Entrada de Dados", layout, finalize=True)

        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            elif event == "Confirmar":
                window.close()
                entrada = values["entrada"]
                return entrada

