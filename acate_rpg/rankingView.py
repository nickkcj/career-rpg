import PySimpleGUI as sg

class RankingView:

    def pega_nome_personagem(self):
        layout = [
            [sg.Text("Você deseja ver o ranking de um personagem específico?")],
            [sg.InputText("", key="opcao", size=(30, 1))],
            [sg.Button("Confirmar", key="confirmar", font=("Helvetica", 14))]
        ]

        window = sg.Window("Ranking Específico", layout, finalize=True)

        while True:
            event, values = window.read()
            if event == sg.WINDOW_CLOSED:
                window.close()
                break
            elif event == "confirmar":
                nome = values["opcao"].strip()
                window.close()
                return nome

                

    def exibir_ranking_nivel(self, personagens_ordenados):
        layout = [
            [sg.Text("-------- RANKING POR NÍVEL --------", font=("Helvetica", 20), justification="center")],
            [sg.Listbox(
                values=[f"{i + 1}. {personagem.nome} - Nível: {personagem.nivel}" for i, personagem in enumerate(personagens_ordenados)],
                size=(50, len(personagens_ordenados)),
                font=("Helvetica", 14),
                key="LISTA"
            )],
            [sg.Button("Voltar", key="voltar", font=("Helvetica", 14))]
        ]

        window = sg.Window("Ranking por Nível", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "voltar"):
                window.close()
                break

    def exibir_ranking_dungeons(self, personagens_ordenados):
        layout = [
            [sg.Text("-------- RANKING POR DUNGEONS CONQUISTADAS --------", font=("Helvetica", 20), justification="center")],
            [sg.Listbox(
                values=[f"{i + 1}. {personagem.nome} - Dungeons Conquistadas: {len(personagem.dungeons_conquistadas)}" for i, personagem in enumerate(personagens_ordenados)],
                size=(50, len(personagens_ordenados)),
                font=("Helvetica", 14),
                key="LISTA"
            )],
            [sg.Button("Voltar", key="voltar", font=("Helvetica", 14))]
        ]

        window = sg.Window("Ranking por Dungeons", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "voltar"):
                window.close()
                return None

    def exibir_ranking_cursos(self, personagens_ordenados):
        layout = [
            [sg.Text("-------- RANKING POR CURSOS CONQUISTADOS --------", font=("Helvetica", 20), justification="center")],
            [sg.Listbox(
                values=[f"{i + 1}. {personagem.nome} - Cursos Conquistados: {personagem.cursos_conquistados}" for i, personagem in enumerate(personagens_ordenados)],
                size=(50, len(personagens_ordenados)),
                font=("Helvetica", 14),
                key="LISTA"
            )],
            [sg.Button("Voltar", key="voltar", font=("Helvetica", 14))]
        ]

        window = sg.Window("Ranking por Cursos", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "voltar"):
                window.close()
                break

    def exibir_dungeons_personagem(self, personagem):
        layout = [
            [sg.Text(f"Dungeons conquistadas por {personagem.nome}:", font=("Helvetica", 16))] if personagem.dungeons_conquistadas else
            [sg.Text(f"{personagem.nome} não conquistou nenhuma dungeon.", font=("Helvetica", 16))],
            [sg.Listbox(
                values=[dungeon['nome'] for dungeon in personagem.dungeons_conquistadas],
                size=(50, len(personagem.dungeons_conquistadas)) if personagem.dungeons_conquistadas else (50, 1),
                font=("Helvetica", 14),
                key="LISTA"
            )] if personagem.dungeons_conquistadas else [sg.Text("")],
            [sg.Button("Voltar", key="voltar", font=("Helvetica", 14))]
        ]

        window = sg.Window("Dungeons do Personagem", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "voltar"):
                window.close()
                break

    def mostrar_mensagem(self, mensagem):
        layout = [
            [sg.Text("***************************", font=("Helvetica", 16), justification="center")],
            [sg.Text(mensagem, font=("Helvetica", 14), justification="center")],
            [sg.Text("***************************", font=("Helvetica", 16), justification="center")],
            [sg.Button("OK", key="ok", font=("Helvetica", 14))]
        ]

        window = sg.Window("Mensagem", layout, finalize=True)

        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "ok"):
                window.close()
                break
