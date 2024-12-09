import time
import os
import PySimpleGUI as sg
class CursoView():
    def pega_dados_curso(self):
        
        janela_largura = 600
        janela_altura = 400

        # Definir a proporção para o aumento dos elementos
        proporcao_largura = janela_largura / 800
        proporcao_altura = janela_altura / 600
        proporcao_texto = proporcao_largura

        # Tamanho proporcional dos widgets
        campo_largura = int(janela_largura * 0.8)
        tamanho_fonte = int(16 * proporcao_texto)

        # Valores para os combos
        niveis = list(range(1, 12))  # Níveis de 1 a 11
        dificuldades = list(range(1, 12))  # Dificuldades de 1 a 11
        xp_ganhos = list(range(100, 1101, 100))  # XP de 100 em 100 até 1000

        layout = [
            [sg.Text("Digite os dados do curso", font=("Helvetica", tamanho_fonte), justification="center", size=(40, 1))],
            [sg.Text("Nome do curso:", size=(int(20 * proporcao_largura), 1)), sg.InputText(key="nome", size=(campo_largura, 1))],
            [sg.Text("Nível requerido:", size=(int(20 * proporcao_largura), 1)), sg.Combo(niveis, key="nivel_requerido", size=(campo_largura, 1), readonly=True)],
            [sg.Text("XP ganho:", size=(int(20 * proporcao_largura), 1)), sg.Combo(xp_ganhos, key="xp_ganho", size=(campo_largura, 1), readonly=True)],
            [sg.Text("Setor:", size=(int(20 * proporcao_largura), 1)), sg.Combo(["RH", "T.I", "Vendas", "Financeiro", "Marketing"], key="setor", size=(campo_largura, 1), readonly=True)],
            [sg.Text("Dificuldade:", size=(int(20 * proporcao_largura), 1)), sg.Combo(dificuldades, key="dificuldade", size=(campo_largura, 1), readonly=True)],
            [sg.Button("Confirmar", size=(int(10 * proporcao_largura), 1)), sg.Button("Cancelar", size=(int(10 * proporcao_largura), 1))]
        ]

        window = sg.Window("Cadastro de Curso", layout, modal=True, size=(janela_largura, janela_altura//2), resizable=True)

        dados = {}
        while True:
            event, values = window.read()

            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                break

            if event == "Confirmar":
                try:
                    # Validação dos campos obrigatórios
                    if not values["nome"]:
                        sg.popup_error("O nome do curso é obrigatório!")
                        continue

                    if not values["nivel_requerido"]:
                        sg.popup_error("Você deve selecionar um nível requerido!")
                        continue

                    if not values["xp_ganho"]:
                        sg.popup_error("Você deve selecionar o XP ganho!")
                        continue

                    if not values["setor"]:
                        sg.popup_error("Você deve selecionar um setor!")
                        continue

                    if not values["dificuldade"]:
                        sg.popup_error("Você deve selecionar a dificuldade!")
                        continue

                    
                    dados = {
                        "nome": values["nome"],
                        "nivel_requerido": int(values["nivel_requerido"]),
                        "xp_ganho": int(values["xp_ganho"]),
                        "setor": values["setor"],
                        "dificuldade": int(values["dificuldade"]),
                        "realizado": False
                    }
                    break

                except ValueError:
                    sg.popup_error("Por favor, preencha todos os campos corretamente!")
                    continue

        window.close()
        return dados




    def mostra_mensagem(self, mensagem):
        layout = [
            [sg.Text('****************************************')],
            [sg.Text(mensagem)],
            [sg.Text('****************************************')],
            [sg.Button('OK')]
        ]
        window = sg.Window('Mensagem', layout)
        event, values = window.read()
        window.close()

    def mostra_cursos(self, cursos_dicionario, alteracao=None):
        cursos_info = []
        for curso in cursos_dicionario:
            cursos_info.append(
                f"Nome: {curso['nome']}\n"
                f"Nível Requerido: {curso['nivel_requerido']}\n"
                f"XP Ganhado: {curso['xp_ganho']}\n"
                f"Setor: {curso['setor']}\n"
                f"Dificuldade: {curso['dificuldade']}\n"
                f"Realizado: {curso['realizado']}\n"
                "-----------------------------\n"
            )

        # Layout da esquerda com a lista de cursos
        cursos_layout = [
            [sg.Text('---- LISTA DE CURSOS ----', font=("Helvetica", 20), justification='center', expand_x=True, pad=(0,25))],
            [sg.Multiline('\n'.join(cursos_info), size=(60, 20), key='-CURSOS-', disabled=True, font=("Helvetica", 16), pad=(10, 10))],
            [sg.Button('Fechar', size=(15, 2), pad=(10, 20))]
        ]

        # Layout da direita com a imagem ajustada
        imagem_layout = [
            [sg.Image(filename="assets/images/cursos.jpg", size=(800, 600), pad=(10, 200))]
        ]

        # Layout principal com os elementos lado a lado e centralizados
        layout = [
            [sg.Push(),
            sg.Column(cursos_layout, element_justification='center', vertical_alignment='center'),
            sg.VSeparator(),
            sg.Column(imagem_layout, element_justification='center', vertical_alignment='center'),
            sg.Push()]
        ]

        # Janela principal centralizada
        window = sg.Window(
            'Cursos Disponíveis',
            layout,
            size=(1200, 800),  # Tamanho total da tela
            element_justification='center',
            resizable=True,
            finalize=True
        )
        window.maximize()
        time.sleep(0.5)  # Maximiza para garantir centralização
        if alteracao == True:
            return
        
        
        else:
            event, values = window.read()
            window.close()







    def seleciona_curso(self):
        layout = [
            [sg.Text('Digite o nome do curso:')],
            [sg.InputText(key='-CURSO-', size=(30, 1))],
            [sg.Button('Selecionar'), sg.Button('Cancelar')]
        ]

        window = sg.Window('Seleção de Curso', layout)
        event, values = window.read()
        window.close()

        if event == 'Selecionar':
            return values['-CURSO-']
        return None
    
