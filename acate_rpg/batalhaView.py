import PySimpleGUI as sg

class BatalhaView:

    def tela_opcoes(self):
        layout = [
            [sg.Text("-------- BATALHA ----------")],
            [sg.Text("Escolha a ação:")],
            [sg.Button("Atacar"), sg.Button("Defender"), sg.Button("Usar Item"), sg.Button("Usar Habilidade")],
        ]
        window = sg.Window("Escolha a Ação", layout, return_keyboard_events=True)

        event, _ = window.read()
        window.close()

        if event == "Atacar":
            return 1
        elif event == "Defender":
            return 2
        elif event == "Usar Item":
            return 3
        elif event == "Usar Habilidade":
            return 4

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
        largura_total = 60  
        margem_personagem = 7  
        margem_boss = 10  
        ajuste_direita = 5  

        espacos_entre_nomes = largura_total - margem_personagem - margem_boss - len(personagem.nome) - len(boss.nome) - len(" VS ")

        layout = [
            [sg.Text("=" * largura_total)],
            [sg.Text(f"{' ' * margem_personagem}{personagem.nome}{' ' * (espacos_entre_nomes // 2)}VS{' ' * (espacos_entre_nomes // 2)}{boss.nome}")],
            [sg.Text("-" * largura_total)],
            [sg.Text(f"{' ' * margem_personagem}{'HP:':<10}{str(personagem.hp_atual) + ' / ' + str(personagem.classe_personagem.atributos['hp']):<10}{' ' * (espacos_entre_nomes - margem_personagem - 20)}{'HP:':<10}{boss.atributos['hp']}")],
            [sg.Text(f"{' ' * margem_personagem}{'Ataque:':<10}{personagem.classe_personagem.atributos['ataque']:<10}{' ' * (espacos_entre_nomes - margem_personagem - 20)}{'Ataque:':<10}{boss.atributos['ataque']}")],
            [sg.Text(f"{' ' * margem_personagem}{'Defesa:':<10}{personagem.classe_personagem.atributos['defesa']:<10}{' ' * (espacos_entre_nomes - margem_personagem - 20)}{'Defesa:':<10}{boss.atributos['defesa']}")],
            [sg.Text(f"{' ' * margem_personagem}{'Estamina:':<10}{personagem.classe_personagem.atributos['estamina']:<10}{' ' * (espacos_entre_nomes - margem_personagem - 20)}{'Estamina:':<10}{boss.atributos['estamina']}")],
            [sg.Text("=" * largura_total)]  
        ]
        
        window = sg.Window("Batalha", layout)
        window.read()
        window.close()








