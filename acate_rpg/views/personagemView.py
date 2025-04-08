import os
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
        # Layout com banners e lista de personagens centralizada
        layout = [
            [
                psg.Image("assets/images/banner1.png", size=(200, 600), pad=(0, 0)),  # Banner esquerdo
                psg.Column(
                    [
                        [psg.Text("------- LISTA DE PERSONAGENS -------", font=("Arial", 18), justification='center', expand_x=True)],
                        [psg.Text("Escolha um personagem para jogar:", font=("Arial", 14), justification='center', expand_x=True)],
                        [
                            psg.Listbox(
                                values=dados_personagens,
                                size=(50, 12),  # Tamanho levemente aumentado
                                key="personagem_lista",
                                font=("Arial", 14),  # Fonte aumentada
                                enable_events=True,
                                select_mode=psg.LISTBOX_SELECT_MODE_SINGLE,
                            )
                        ],
                        [psg.Button("Cancelar", size=(12, 1), pad=(5, 20))],  # Botão ajustado
                    ],
                    element_justification="center",  # Centralização horizontal do conteúdo da coluna
                    pad=(0, 0),  # Sem espaçamento extra
                ),
                psg.Image("assets/images/banner1.png", size=(200, 600), pad=(0, 0)),  # Banner direito
            ]
        ]

        # Criar a janela com centralização vertical e horizontal
        window = psg.Window(
            "Lista de Personagens",
            layout,
            finalize=True,
            resizable=True,
            element_justification="center",  # Centralização horizontal
            size=(800, 600),  # Tamanho mínimo para evitar distorção
        )
        window.maximize()  # Maximizar a janela ao abrir
        

        while True:
            event, values = window.read()

            if event == psg.WIN_CLOSED or event == "Cancelar":
                window.close()
                return None  # Se o usuário cancelar ou fechar a janela

            if event == "personagem_lista" and values["personagem_lista"]:
                # Detectar duplo clique para selecionar
                event, values = window.read()  # Verifica o segundo clique
                if event == "personagem_lista" and values["personagem_lista"]:
                    window.close()
                    return values["personagem_lista"][0]  # Retornar o personagem selecionado

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
            
    def pega_novos_dados_personagem(self, personagem):
        layout = [
            [psg.Text(f"Alterar Dados de {personagem.nome}", font=("Helvetica", 16))],
            [psg.Text("Nome:", size=(15, 1)), psg.InputText(default_text=personagem.nome, key="nome")],
            [psg.Text("Nível:", size=(15, 1)), psg.InputText(default_text=personagem.nivel, key="nivel")],
            [psg.Text("Experiência Total:", size=(15, 1)), psg.InputText(default_text=personagem.experiencia_total, key="experiencia_total")],
            [psg.Text("Pontos Disponíveis:", size=(15, 1)), psg.InputText(default_text=personagem.pontos_disponiveis, key="pontos_disponiveis")],
            [psg.Text("Classe:", size=(15, 1)), psg.Combo(
            ["Trainee","Estagiario", "CLT"], default_value=personagem.classe_personagem.nome_classe, key="classe")],
            [psg.Text("Cursos Conquistados:", size=(15, 1)), psg.InputText(default_text=personagem.cursos_conquistados, key="cursos_conquistados")],
            [psg.Button("Salvar"), psg.Button("Cancelar")]
        ]

        window = psg.Window("Alterar Dados do Personagem", layout)
        event, values = window.read()
        window.close()

        if event == "Salvar":

            return {
                "nome": values["nome"],
                "nivel": int(values["nivel"]),
                "experiencia_total": int(values["experiencia_total"]),
                "pontos_disponiveis": int(values["pontos_disponiveis"]),
                "classe": values["classe"],
                "cursos_conquistados": int(values["cursos_conquistados"]),
            }
        return None
        
    def selecionar_personagem_para_excluir(self, personagens):
        layout = [
            [psg.Text("Selecione o personagem que deseja excluir:", font=("Helvetica", 16))],
            [psg.Listbox(
                values=[f"{p.nome} - Nível: {p.nivel} - Classe: {p.classe_personagem.nome_classe}" for p in personagens],
                size=(50, 10),
                key="personagem_selecionado",
                enable_events=True
            )],
            [psg.Button("Excluir"), psg.Button("Cancelar")]
        ]

        window = psg.Window("Excluir Personagem", layout)

        personagem_selecionado = None  # Variável para armazenar a seleção do personagem
        while True:
            event, values = window.read()

            if event == psg.WINDOW_CLOSED or event == "Cancelar":
                break  # Fecha a janela ou cancela a ação

            if event == "Excluir":
                if values["personagem_selecionado"]:  # Verifica se um item foi selecionado na lista
                    # Obtém o personagem selecionado
                    idx = personagens.index(next(p for p in personagens if f"{p.nome}" in values["personagem_selecionado"][0]))
                    personagem_selecionado = personagens[idx]
                    break  # Sai do loop após a seleção

        window.close()
        return personagem_selecionado

    def confirmar_exclusao(self, nome_personagem):
        confirmacao = psg.popup_yes_no(
            f"Você realmente deseja excluir o personagem '{nome_personagem}'?",
            title="Confirmação de Exclusão",
        )
        return confirmacao == "Yes"

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

    
