import PySimpleGUI as sg
import time
class SetorView:
    
    def pega_dados_setor(self, numero):
        layout = [
            [sg.Text(f"-------- DADOS DO SETOR {numero} --------", font=("Helvetica", 16), justification="center")],
            [sg.Text("Digite o nome do setor (RH, T.I, Vendas, Financeiro ou Marketing):", font=("Helvetica", 14))],
            [sg.InputText(key="nome", font=("Helvetica", 12))],
            [sg.Text("Qual a dificuldade do setor (1-10):", font=("Helvetica", 14))],
            [sg.Spin([i for i in range(1, 11)], initial_value=1, key="dificuldade", font=("Helvetica", 12))],
            [sg.Button("Confirmar", key="confirmar", font=("Helvetica", 12))],
        ]

        window = sg.Window(f"Setor {numero}", layout, finalize=True, element_justification='center')

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                return None
            elif event == "confirmar":
                nome = values["nome"]
                dificuldade = values["dificuldade"]
                window.close()
                return {"nome": nome, "dificuldade": int(dificuldade)}

    def pega_nome_setor(self, numero):
        layout = [
            [sg.Text(f"-------- DADOS DO SETOR {numero} --------", font=("Helvetica", 16))],
            [sg.Text("Selecione o nome do setor:", font=("Helvetica", 14), pad=(0,5))],
            [sg.Combo(
                ["RH", "T.I", "Vendas", "Financeiro", "Marketing"], 
                key="SETOR", 
                font=("Helvetica", 12), 
                readonly=True,
                pad=(0,20)   
            )],
            [sg.Button("Confirmar", key="CONFIRMAR", font=("Helvetica", 12), size=(20,1))],
        ]

        window = sg.Window(f"Setor {numero}", layout, modal=True, size=(400,200), element_justification='center')
        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                return None  # Ou você pode retornar algo indicando cancelamento

            if event == "CONFIRMAR":
                setor = values.get("SETOR")
                if setor:
                    window.close()
                    return setor  # Retorna o nome do setor selecionado
                else:
                    sg.popup_error("Por favor, selecione um setor.")


    def pega_dificuldade_setor(self):
        layout = [
            [sg.Text("Qual a dificuldade do setor (1-10):", font=("Helvetica", 14))],
            [sg.Spin([i for i in range(1, 11)], initial_value=1, key="dificuldade", font=("Helvetica", 12), size=(20,3))],
            [sg.Button("Confirmar", key="confirmar", font=("Helvetica", 12))],
        ]

        window = sg.Window("Dificuldade do Setor", layout, finalize=True, element_justification='center')

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                return None
            elif event == "confirmar":
                dificuldade = values["dificuldade"]
                window.close()
                return int(dificuldade)

    def pega_opcao_setor(self):
        layout = [
            [sg.Text("Selecione o número do setor:", font=("Helvetica", 14))],
            [sg.InputText(key="opcao", font=("Helvetica", 12))],
            [sg.Button("Confirmar", key="confirmar", font=("Helvetica", 12))],
        ]

        window = sg.Window("Opção do Setor", layout, finalize=True)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                return None
            elif event == "confirmar":
                opcao = values["opcao"]
                window.close()
                return opcao

    def pega_opcao_boss(self):
        layout = [
            [sg.Text("Selecione o número de qual processo seletivo quer aplicar:", font=("Helvetica", 14))],
            [sg.InputText(key="opcao", font=("Helvetica", 12))],
            [sg.Button("Confirmar", key="confirmar", font=("Helvetica", 12))],
        ]

        window = sg.Window("Opção do Boss", layout, finalize=True)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                return None
            elif event == "confirmar":
                opcao = values["opcao"]
                window.close()
                return opcao

