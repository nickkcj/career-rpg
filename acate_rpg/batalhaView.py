import PySimpleGUI as sg
import time
class BatalhaView:

    def escolher_habilidade(self, classe):
        if classe == 'CLT':
            layout = [
                [sg.Text("------Escolha sua habilidade!------")],
                [sg.Button("Festa da Firma"), sg.Button("Ataque Corporativo")]
            ]
        elif classe == 'Estagiario':
            layout = [
                [sg.Text("------Escolha sua habilidade!------")],
                [sg.Button("Cagada Remunerada"), sg.Button("Desestabilizar Boss")]
            ]
        elif classe == 'Trainee':
            layout = [
                [sg.Text("------Escolha sua habilidade!------")],
                [sg.Button("Hora Extra"), sg.Button("Desmotivar Boss")]
            ]

        window = sg.Window(f"Escolha a habilidade para {classe}", layout)
        event, _ = window.read()
        window.close()

        if event == "Festa da Firma" or event == "Cagada Remunerada" or event == "Hora Extra":
            return "buff"
        elif event == "Ataque Corporativo" or event == "Desestabilizar Boss" or event == "Desmotivar Boss":
            return "debuff"

    def mostra_resultado(self, mensagem):
        layout = [
            [sg.Text(mensagem)],
            [sg.Button("OK")]
        ]
        window = sg.Window("Resultado", layout)
        window.read()
        window.close()

    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg)],
            [sg.Button("OK")]
        ]
        window = sg.Window("Mensagem", layout)
        window.read()
        window.close()


    def exibir_tela_batalha(self, personagem, boss):
        # Caminhos das imagens
        img_personagem_boss_path = "assets/images/personagem_boss.jpg"  # Imagem compartilhada para personagem e boss
        

        # Layout inicial com ajuste de tamanhos
        layout = [
            [sg.Text("BATALHA", justification="center", font=("Arial", 25), size=(30, 1))],
            [sg.Image(filename=img_personagem_boss_path, key="-IMG-", size=(800, 600))],
            [sg.Column([
                [sg.Text(f"{personagem.nome}", justification="center", font=("Arial", 20), size=(20, 1))],
                [sg.Text(f"HP: {personagem.hp_atual}/{personagem.classe_personagem.atributos['hp']}", justification="center",font=("Arial", 20), key="-PERSONAGEM_HP-")],
            ], element_justification="center"),
            sg.Column([
                [sg.Text(f"{boss.nome}", justification="center", font=("Arial", 20), size=(20, 1))],
                [sg.Text(f"HP: {boss.atributos['hp']}", justification="center", font=("Arial", 20), key="-BOSS_HP-")],
            ], element_justification="center")],
            [sg.Button("Atacar", size=(20,2)), sg.Button("Defender", size=(20,2)), sg.Button("Usar Item", size=(20,2)), sg.Button("Usar Habilidade", size=(20,2))],
        ]

        # Criação da janela
        window = sg.Window("Batalha", layout, finalize=True, element_justification='center')
        window.maximize()
        return window











