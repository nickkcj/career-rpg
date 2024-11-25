import os
import time
import PySimpleGUI as psg
class PersonagemView():

    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

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

    def escolher_atributo(self):
        self.limpar_terminal()
        print("-------- UPAR ATRIBUTOS ----------")
        print("Escolha o atributo para aumentar:")
        print("1 - Ataque")
        print("2 - Defesa")
        print("3 - HP")
        print("4 - Estamina")
        opcao = int(input("Digite o número do atributo: "))
        atributos = {1: "ataque", 2: "defesa", 3: "hp", 4: "estamina"}
        return atributos.get(opcao, None)
    
    def pega_quantidade_pontos(self):
        print("-------- UPAR ATRIBUTOS ----------")
        pontos = int(input("Quantos pontos deseja aplicar? "))
        return pontos
    
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

        evento = janela.read()

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
        print("--------- HABILIDADES DO PERSONAGEM ---------")

        for classe, habilidades in habilidades_por_classe.items():
            print(f"\n{classe}:")
            for habilidade in habilidades:
                print(f" - {habilidade['nome']} - {habilidade['efeito']} ({habilidade['tipo']})")
        
        input("\nPressione Enter para voltar ao menu.")

    def mostrar_mensagem(self, msg):
        self.limpar_terminal()
        print("****************************************")
        print(msg)
        print("****************************************")
        time.sleep(1)

        