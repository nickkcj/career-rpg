import os
import time
import PySimpleGUI as psg

class RankingView:
    def __init__(self):
        self.window = None

    def limpar_tela(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def exibir_ranking_nivel(self, personagens_ordenados):
        layout = [
            [psg.Text("-------- RANKING POR NÍVEL --------", font=("Helvetica", 20), justification="center")],
            [psg.Listbox(
                values=[f"{idx+1}. {personagem.nome} - Nível: {personagem.nivel}" for idx, personagem in enumerate(personagens_ordenados)],
                size=(50, 10),
                key="personagem_selecionado",
                font=("Helvetica", 14),
                enable_events=True,
                select_mode=psg.LISTBOX_SELECT_MODE_SINGLE,
            )],
            [psg.Button("Ver Status", key="ver_status", font=("Helvetica", 14)), psg.Button("Voltar", key="voltar", font=("Helvetica", 14))]
        ]

        window = psg.Window("Ranking de Nível", layout, size=(600, 400), finalize=True)

        while True:
            event, values = window.read()

            if event in ("voltar", psg.WINDOW_CLOSED):
                window.close()
                return

            if event == "ver_status":
                if values["personagem_selecionado"]:
                    idx = int(values["personagem_selecionado"][0].split(".")[0]) - 1
                    personagem = personagens_ordenados[idx]
                    self.exibir_status_personagem(personagem)

    def exibir_ranking_dungeons(self, personagens_ordenados):
        layout = [
            [psg.Text("-------- RANKING POR DUNGEONS CONQUISTADAS --------", font=("Helvetica", 20), justification="center")],
            [psg.Listbox(
                values=[f"{idx+1}. {personagem.nome} - Dungeons: {len(personagem.dungeons_conquistadas)}" for idx, personagem in enumerate(personagens_ordenados)],
                size=(50, 10),
                key="personagem_selecionado",
                font=("Helvetica", 14),
                enable_events=True,
                select_mode=psg.LISTBOX_SELECT_MODE_SINGLE,
            )],
            [psg.Button("Ver Status", key="ver_status", font=("Helvetica", 14)), psg.Button("Voltar", key="voltar", font=("Helvetica", 14))]
        ]

        window = psg.Window("Ranking de Dungeons", layout, size=(600, 400), finalize=True)

        while True:
            event, values = window.read()

            if event in ("voltar", psg.WINDOW_CLOSED):
                window.close()
                return

            if event == "ver_status":
                if values["personagem_selecionado"]:
                    idx = int(values["personagem_selecionado"][0].split(".")[0]) - 1
                    personagem = personagens_ordenados[idx]
                    self.exibir_status_personagem(personagem)

    def exibir_ranking_cursos(self, personagens_ordenados):
        layout = [
            [psg.Text("-------- RANKING POR CURSOS CONQUISTADOS --------", font=("Helvetica", 20), justification="center")],
            [psg.Listbox(
                values=[f"{idx+1}. {personagem.nome} - Cursos: {personagem.cursos_conquistados}" for idx, personagem in enumerate(personagens_ordenados)],
                size=(50, 10),
                key="personagem_selecionado",
                font=("Helvetica", 14),
                enable_events=True,
                select_mode=psg.LISTBOX_SELECT_MODE_SINGLE,
            )],
            [psg.Button("Ver Status", key="ver_status", font=("Helvetica", 14)), psg.Button("Voltar", key="voltar", font=("Helvetica", 14))]
        ]

        window = psg.Window("Ranking de Cursos", layout, size=(600, 400), finalize=True)

        while True:
            event, values = window.read()

            if event in ("voltar", psg.WINDOW_CLOSED):
                window.close()
                return

            if event == "ver_status":
                if values["personagem_selecionado"]:
                    idx = int(values["personagem_selecionado"][0].split(".")[0]) - 1
                    personagem = personagens_ordenados[idx]
                    self.exibir_status_personagem(personagem)

    def exibir_status_personagem(self, personagem):
        layout = [
            [psg.Text(f"Status de {personagem.nome}", font=("Helvetica", 18), justification="center")],
            [psg.Text(f"Nome: {personagem.nome}", font=("Helvetica", 14))],
            [psg.Text(f"Nível: {personagem.nivel}", font=("Helvetica", 14))],
            [psg.Text(f"Classe: {personagem.classe_personagem.nome_classe}", font=("Helvetica", 14))],
            [psg.Text(f"Experiência: {personagem.experiencia_total}", font=("Helvetica", 14))],
            [psg.Text(f"HP: {personagem.classe_personagem.atributos['hp']}", font=("Helvetica", 14))],
            [psg.Text(f"Estamina: {personagem.classe_personagem.atributos['estamina']}", font=("Helvetica", 14))],
            [psg.Text(f"Ataque: {personagem.classe_personagem.atributos['ataque']}", font=("Helvetica", 14))],
            [psg.Text(f"Defesa: {personagem.classe_personagem.atributos['defesa']}", font=("Helvetica", 14))],
            [psg.Text(f"Cursos Conquistados: {personagem.cursos_conquistados}", font=("Helvetica", 14))],
            [psg.Text("Dungeons Conquistadas:", font=("Helvetica", 14))],
            [psg.Listbox(
                values=[f"{dungeon['nome']}" for dungeon in personagem.dungeons_conquistadas],
                size=(30, 10),
                font=("Helvetica", 12),
                select_mode=psg.LISTBOX_SELECT_MODE_SINGLE,
            )],
            [psg.Button("Fechar", key="fechar", font=("Helvetica", 14))]
        ]

        window = psg.Window(f"Status de {personagem.nome}", layout, finalize=True)

        while True:
            event, _ = window.read()

            if event in ("fechar", psg.WINDOW_CLOSED):
                window.close()
                break

    def mostrar_mensagem(self, mensagem):
        psg.popup(mensagem, title="Mensagem")

       