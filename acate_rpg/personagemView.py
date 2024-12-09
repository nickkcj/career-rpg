import os
import time
import PySimpleGUI as psg
class PersonagemView():

    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pega_dados_personagem(self):
    # Layout para a janela de cadastro
        layout = [
            [psg.Text("---------- CADASTRO DE PERSONAGEM ----------", font=("Helvetica", 16), justification="center")],
            [psg.Text("Digite o nome do personagem:", font=("Helvetica", 12))],
            [psg.InputText(key="nome")],
            [psg.Text("Escolha uma classe:", font=("Helvetica", 12))],
            [psg.Radio("CLT (Bom no early game)", "classe", key="CLT")],
            [psg.Radio("Estagiário (Médio no early, bom no late)", "classe", key="Estagiario")],
            [psg.Radio("Trainee (Fraco no early, muito forte no late)", "classe", key="Trainee")],
            [psg.Button("Confirmar", key="CONFIRMAR"), psg.Button("Cancelar", key="CANCELAR")]
        ]

        # Criação da janela
        janela = psg.Window("Cadastro de Personagem", layout, modal=True)

        while True:
            evento, valores = janela.read()

            if evento == psg.WINDOW_CLOSED or evento == "CANCELAR":
                janela.close()
                return None  # Cadastro cancelado

            if evento == "CONFIRMAR":
                nome = valores.get("nome", "").strip()
                classe = None

                # Determina qual classe foi escolhida
                if valores.get("CLT"):
                    classe = "CLT"
                elif valores.get("Estagiario"):
                    classe = "Estagiario"
                elif valores.get("Trainee"):
                    classe = "Trainee"

                # Validações
                if not nome:
                    psg.popup_error("Nome inválido! Por favor, insira um nome válido.", title="Erro")
                    continue
                if not classe:
                    psg.popup_error("Por favor, selecione uma classe para o personagem.", title="Erro")
                    continue

                # Dados validados
                janela.close()
                return {
                    "nome": nome,
                    "classe": classe,
                    "nivel": 1,
                    "experiencia_total": 0
                }

    def mostrar_personagens(self, dados_personagens):
        # Layout para exibir os personagens
        layout = [
            [psg.Text("------- LISTA DE PERSONAGENS -------", font=("Arial", 14), justification='center')],
            [psg.Text("Escolha um personagem para jogar:", font=("Arial", 12))],
        ]

        # Criando os botões em grupos de 3 por linha
        botoes_por_linha = []
        for i, personagem in enumerate(dados_personagens):
            botoes_por_linha.append(psg.Button(personagem, key=str(i)))
            if (i + 1) % 3 == 0 or i == len(dados_personagens) - 1:  # Quando completar 3 botões ou for o último
                layout.append(botoes_por_linha)  # Adiciona os 3 botões como uma linha
                botoes_por_linha = []  # Reseta a lista para o próximo grupo de botões

        # Adicionando o botão de cancelar
        layout.append([psg.Button("Cancelar")])

        window = psg.Window("Lista de Personagens", layout, finalize=True)

        while True:
            event, _ = window.read()
            
            if event == psg.WIN_CLOSED or event == "Cancelar":
                window.close()
                return None  # Se o usuário cancelar ou fechar a janela

            if event.isdigit():
                # Retornar o nome do personagem selecionado
                window.close()
                return dados_personagens[int(event)]

    def mostrar_status(self, dados_personagem):
        psg.ChangeLookAndFeel('DarkGreen4')
        layout = [
            [psg.Text("-------- STATUS ----------", font=("Arial", 14, "bold"))],
            [psg.Text(f"Nome: {dados_personagem['nome']}")],
            [psg.Text(f"Classe: {dados_personagem['classe']}")],
            [psg.Text(f"Nível: {dados_personagem['nivel']}")],
            [psg.Text(f"Experiência total: {dados_personagem['experiencia_total']}")],
            [psg.Text(f"Experiência para próximo nível: {dados_personagem['experiencia_para_proximo_nivel']}")],
            [psg.Text(f"Pontos disponíveis para distribuir: {dados_personagem['pontos_disponiveis']}")],
            [psg.Text(f"Ataque: {dados_personagem['ataque']}")],
            [psg.Text(f"Defesa: {dados_personagem['defesa']}")],
            [psg.Text(f"HP Máximo: {dados_personagem['hp']}")],
            [psg.Text(f"HP Atual: {dados_personagem['hp_atual']}")],
            [psg.Text(f"Estamina: {dados_personagem['estamina']}")],
            [psg.Text(f"Poções de HP: {dados_personagem['pocoes_hp']}")],
            [psg.Text(f"Poções de Estamina: {dados_personagem['pocoes_est']}")],
            [psg.Text("")],
            [psg.Text("-------- PROGRESSO ----------", font=("Arial", 14, "bold"))],
            [psg.Text(f"Cursos Conquistados: {dados_personagem['cursos_conquistados']}")],
            [psg.Text("Empresas conquistadas:")],
            [psg.Listbox(
                values=[dungeon['nome'] for dungeon in dados_personagem['dungeons_conquistadas']],
                size=(40, 5),
                no_scrollbar=len(dados_personagem['dungeons_conquistadas']) <= 5,
                key="EMPRESAS_CONQUISTADAS"
            )],
            [psg.Text("Histórico de vagas:")],
            [psg.Listbox(
                values=[boss['nome'] for boss in dados_personagem['bosses_derrotados']],
                size=(40, 5),
                no_scrollbar=len(dados_personagem['bosses_derrotados']) <= 5,
                key="HISTORICO_DE_VAGAS"
            )],
            [psg.Button("Fechar", key="FECHAR")]
        ]

        janela = psg.Window("Status do Personagem", layout, modal=True)

        while True:
            evento, _ = janela.read()
            if evento in (psg.WINDOW_CLOSED, "FECHAR"):
                janela.close()
                return
            

        

    def escolher_atributo_e_quantidade(self):
        layout_atributos = [
            [psg.Text("-------- UPAR ATRIBUTOS ----------")],
            [psg.Text("Escolha um atributo para aumentar:")],
            [psg.Button("Ataque", key="ataque")],
            [psg.Button("Defesa", key="defesa")],
            [psg.Button("HP", key="hp")],
            [psg.Button("Estamina", key="estamina")],
            [psg.Button("Cancelar", key="CANCELAR")]
        ]

        janela_atributos = psg.Window("Upar Atributos", layout_atributos, modal=True)

        while True:
            evento, _ = janela_atributos.read()

            if evento in (psg.WINDOW_CLOSED, "CANCELAR"):
                janela_atributos.close()
                return None, None

            if evento in ["ataque", "defesa", "hp", "estamina"]:
                atributo_escolhido = evento
                janela_atributos.close()
                break

        layout_pontos = [
            [psg.Text("-------- UPAR ATRIBUTOS ----------")],
            [psg.Text(f"Você escolheu: {atributo_escolhido}")],
            [psg.Text("Quantos pontos deseja aplicar?")],
            [psg.InputText(key="quantidade", do_not_clear=False)],
            [psg.Button("Confirmar", key="CONFIRMAR"), psg.Button("Cancelar", key="CANCELAR")]
        ]

        janela_pontos = psg.Window("Definir Pontos", layout_pontos, modal=True)

        while True:
            evento, valores = janela_pontos.read()

            if evento in (psg.WINDOW_CLOSED, "CANCELAR"):
                janela_pontos.close()
                return None, None

            if evento == "CONFIRMAR":
                try:
                    pontos = int(valores["quantidade"])
                    if pontos > 0:
                        janela_pontos.close()
                        return atributo_escolhido, pontos
                    else:
                        psg.popup_error("Por favor, insira um número maior que 0.")
                except ValueError:
                    psg.popup_error("Por favor, insira um número válido.")
    
    def escolher_item(self, itens_personagem):
        opcoes = []
        if itens_personagem["pocoes_hp"] > 0:
            opcoes.append([psg.Button("Poção de HP", key="HP")])
        if itens_personagem["pocoes_est"] > 0:
            opcoes.append([psg.Button("Poção de Estamina", key="EST")])
        
        layout = [
            [psg.Text("--- Inventário ---", font=("Arial", 14, "bold"))],
            *opcoes,
            [psg.Button("Cancelar", key="CANCELAR")]
        ]
        janela = psg.Window("Usar Item", layout, modal=True)

        evento, _ = janela.read()
        janela.close()
        return {"HP": 1, "EST": 2}.get(evento, None)

    def mostrar_habilidades(self, habilidades_por_classe):
        layout = [
            [psg.Text("--------- HABILIDADES DO PERSONAGEM ---------", font=("Arial", 14, "bold"))]
        ]

        for classe, habilidades in habilidades_por_classe.items():
            layout.append([psg.Text(f"{classe}:", font=("Arial", 12, "bold"))])
            for habilidade in habilidades:
                layout.append([psg.Text(f" - {habilidade['nome']}: {habilidade['efeito']} ({habilidade['tipo']})")])

        layout.append([psg.Button("Voltar", key="VOLTAR")])

        janela = psg.Window("Habilidades do Personagem", layout, modal=True)
        while True:
            evento, _ = janela.read()
            if evento in (psg.WINDOW_CLOSED, "VOLTAR"):
                break
        janela.close()

    

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

    
