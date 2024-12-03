import os
import time
import PySimpleGUI as psg
class PersonagemView():

    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pega_dados_personagem(self):
        while True:
            layout_nome = [
                [psg.Text("---------- CADASTRO PERSONAGEM ---------", font=("Helvetica", 16))],
                [psg.Text("Digite o nome do personagem:", font=("Helvetica", 12))],
                [psg.InputText(key="nome")],
                [psg.Button("Confirmar", key="CONFIRMAR"), psg.Button("Cancelar", key="CANCELAR")]
            ]

            janela_nome = psg.Window("Cadastro de Personagem - Nome", layout_nome, modal=True)
            evento, valores = janela_nome.read()
            janela_nome.close()

            if evento == "CANCELAR" or evento == psg.WINDOW_CLOSED:
                return None  # Cancela o cadastro
            nome = valores.get("nome", "").strip()
            if nome:
                break
            else:
                psg.popup_error("Nome inválido! Por favor, insira um nome válido.", title="Erro")

        while True:
            # Layout da segunda janela para a escolha de classe
            layout_classe = [
                [psg.Text("---------- ESCOLHA DE CLASSE ----------", font=("Helvetica", 16))],
                [psg.Text("Escolha uma classe para o personagem:", font=("Helvetica", 12))],
                [psg.Button("CLT (Bom no early game)", key="CLT")],
                [psg.Button("Estagiário (Médio no early, bom no late)", key="Estagiario")],
                [psg.Button("Trainee (Fraco no early, muito forte no late)", key="Trainee")],
                [psg.Button("Cancelar", key="CANCELAR")]
            ]

            janela_classe = psg.Window("Cadastro de Personagem - Classe", layout_classe, modal=True)
            evento, _ = janela_classe.read()
            janela_classe.close()

            if evento == "CANCELAR" or evento == psg.WINDOW_CLOSED:
                return None  # Cancela o cadastro
            if evento in ["CLT", "Estagiario", "Trainee"]:
                classe = evento
                break
            else:
                psg.popup_error("Opção inválida! Escolha entre as opções disponíveis.", title="Erro")

        return {
            "nome": nome,
            "classe": classe,
            "nivel": 1,
            "experiencia_total": 0
        }

    def mostrar_personagens(self, dados_personagem):
        string_todos_personagens = ""
        for dado in dados_personagem:
            string_todos_personagens = string_todos_personagens + "NOME: " + dado["nome"] + ' - '
            string_todos_personagens = string_todos_personagens + "CLASSE: " + str(dado["telefone"]) + ' - '
            string_todos_personagens = string_todos_personagens + "NÍVEL: " + str(dado["cpf"]) + '\n\n'

        psg.Popup('-------- LISTA DE PERSONAGENS ----------', string_todos_personagens)

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
                break

        janela.close()

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
        layout = [
            [psg.Text("--- Inventário ---", font=("Arial", 14, "bold"))],
            [psg.Text(f"Poção HP (quantidade: {itens_personagem['pocoes_hp']})")],
            [psg.Text(f"Poção Estamina (quantidade: {itens_personagem['pocoes_est']})")],
            [psg.Button("Poção de HP", key="HP")],
            [psg.Button("Poção de Estamina", key="EST")],
            [psg.Button("Cancelar", key="CANCELAR")]
        ]

        janela = psg.Window("Usar Item", layout, modal=True)

        evento, _ = janela.read()

        if evento in (psg.WINDOW_CLOSED, "CANCELAR"):
            janela.close()
            return None
            
        if evento == "HP":
            janela.close()
            return 1
            
        if evento == "EST":
            janela.close()
            return 2

    def mostrar_habilidades(self, habilidades_por_classe):
        self.limpar_terminal()

        texto_habilidades = "--------- HABILIDADES DO PERSONAGEM ---------\n"
        for classe, habilidades in habilidades_por_classe.items():
            texto_habilidades += f"\n{classe}:\n"
            for habilidade in habilidades:
                texto_habilidades += f" - {habilidade['nome']} - {habilidade['efeito']} ({habilidade['tipo']})\n"

        layout = [
            [psg.Text(texto_habilidades, font=("Arial", 12), size=(50, 20))],
            [psg.Button("Voltar", key="VOLTAR")]
        ]

        janela = psg.Window("Habilidades do Personagem", layout, modal=True)

        while True:
            evento, _ = janela.read()

            if evento in (psg.WINDOW_CLOSED, "VOLTAR"):
                janela.close()
                break

    

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

    
