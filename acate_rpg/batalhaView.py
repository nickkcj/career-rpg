import PySimpleGUI as sg
import time
class BatalhaView:

    def escolher_habilidade(self, classe):
        if classe == 'CLT':
            layout = [
                [sg.Text("------Escolha sua habilidade!------")],
                [sg.Button("Festa da Firma", key='1'), sg.Button("Ataque Corporativo", key='2')]
            ]
        elif classe == 'Estagiario':
            layout = [
                [sg.Text("------Escolha sua habilidade!------")],
                [sg.Button("Cagada Remunerada", key='1'), sg.Button("Desestabilizar Boss", key='2')]
            ]
        elif classe == 'Trainee':
            layout = [
                [sg.Text("------Escolha sua habilidade!------")],
                [sg.Button("Hora Extra", key='1'), sg.Button("Desmotivar Boss", key='2')]
            ]

        window = sg.Window(f"Escolha a habilidade para {classe}", layout)
        event, _ = window.read()
        window.close()

        return event

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


    def exibir_tela_batalha(self, dados_batalha):
        
        img_personagem_boss_path = "assets/images/personagem_boss.jpg"  

        
        personagem_nome = dados_batalha["personagem"]["nome"]
        personagem_hp_atual = dados_batalha["personagem"]["hp_atual"]
        personagem_hp_total = dados_batalha["personagem"]["hp_total"]

        boss_nome = dados_batalha["boss"]["nome"]
        boss_hp = dados_batalha["boss"]["hp"]

        
        layout = [
            [sg.Text("BATALHA", justification="center", font=("Arial", 25), size=(30, 1))],
            [sg.Image(filename=img_personagem_boss_path, key="-IMG-", size=(800, 600))],
            [sg.Column([
                [sg.Text(f"{personagem_nome}", justification="center", font=("Arial", 20), size=(20, 1))],
                [sg.Text(f"HP: {personagem_hp_atual}/{personagem_hp_total}", justification="center", font=("Arial", 20), key="-PERSONAGEM_HP-")],
            ], element_justification="center"),
            sg.Column([
                [sg.Text(f"{boss_nome}", justification="center", font=("Arial", 20), size=(20, 1))],
                [sg.Text(f"HP: {boss_hp}", justification="center", font=("Arial", 20), key="-BOSS_HP-")],
            ], element_justification="center")],
            [sg.Button("Atacar", size=(20, 2)), sg.Button("Defender", size=(20, 2)), sg.Button("Usar Item", size=(20, 2)), sg.Button("Usar Habilidade", size=(20, 2))],
        ]

       
        window = sg.Window("Batalha", layout, finalize=True, element_justification='center')
        window.maximize()
        return window












