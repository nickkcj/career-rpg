import time
import os
import PySimpleGUI as psg
class CursoView():
    def pega_dados_curso(self):
        psg.ChangeLookAndFeel("DarkGreen4")
        
        janela_largura = 600
        janela_altura = 400

        # Definir a proporção para o aumento dos elementos
        proporcao_largura = janela_largura / 800
        proporcao_altura = janela_altura / 600
        proporcao_texto = proporcao_largura

        # Tamanho proporcional dos widgets
        campo_largura = int(janela_largura * 0.8)
        campo_altura = 1
        tamanho_fonte = int(16 * proporcao_texto)

        layout = [
            [psg.Text("Digite os dados do curso", font=("Helvetica", tamanho_fonte), justification="center", size=(40, 1))],
            [psg.Text("Nome do curso:", size=(int(20 * proporcao_largura), 1)), psg.InputText(key="nome", size=(campo_largura, campo_altura))],
            [psg.Text("Nível requerido:", size=(int(20 * proporcao_largura), 1)), psg.InputText(key="nivel_requerido", size=(campo_largura, campo_altura))],
            [psg.Text("XP ganho:", size=(int(20 * proporcao_largura), 1)), psg.InputText(key="xp_ganho", size=(campo_largura, campo_altura))],
            [psg.Text("Setor:", size=(int(20 * proporcao_largura), 1)), psg.InputCombo(["RH", "T.I", "Vendas", "Financeiro", "Marketing"], key="setor", size=(campo_largura, campo_altura), readonly=True)],
            [psg.Text("Dificuldade:", size=(int(20 * proporcao_largura), 1)), psg.InputText(key="dificuldade", size=(campo_largura, campo_altura))],
            [psg.Button("Confirmar", size=(int(10 * proporcao_largura), 1)), psg.Button("Cancelar", size=(int(10 * proporcao_largura), 1))]
        ]

        # Criação da janela com o tamanho desejado
        window = psg.Window("Cadastro de Curso", layout, modal=True, size=(janela_largura, janela_altura), resizable=True)  


        dados = {}
        while True:
            event, values = window.read()

        
            if event in (psg.WINDOW_CLOSED, "Cancelar"):
                break

            if event == "Confirmar":
                try:
                    
                    if not values["nome"]:
                        psg.popup_error("O nome do curso é obrigatório!")
                        continue

                    nivel_requerido = int(values["nivel_requerido"])
                    if nivel_requerido < 1 or nivel_requerido > 10:
                        psg.popup_error("O nível requerido deve ser entre 1 e 10!")
                        continue

                    xp_ganho = int(values["xp_ganho"])
                    if xp_ganho <= 0:
                        psg.popup_error("O XP ganho deve ser maior que 0!")
                        continue

                    if not values["setor"]:
                        psg.popup_error("Você deve selecionar um setor!")
                        continue

                    dificuldade = int(values["dificuldade"])
                    if dificuldade < 1 or dificuldade > 10:
                        psg.popup_error("A dificuldade deve ser entre 1 e 10!")
                        continue

                    
                    dados = {
                        "nome": values["nome"],
                        "nivel_requerido": nivel_requerido,
                        "xp_ganho": xp_ganho,
                        "setor": values["setor"],
                        "dificuldade": dificuldade,
                        "realizado": False
                    }
                    break

                except ValueError:
                    psg.popup_error("Por favor, preencha todos os campos corretamente!")
                    continue

        window.close()
        return dados



    def mostra_mensagem(self,mensagem):
        print("\n")
        print("****************************************")
        print(mensagem)
        print("****************************************")
        time.sleep(1)


    def mostra_cursos(self, cursos_dicionario):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n----LISTA DE CURSOS---- \n")
        for curso in cursos_dicionario:
            print(
                f"Nome: {curso['nome']}, Nível Requerido: {curso['nivel_requerido']}, "
                f"XP Ganhado: {curso['xp_ganho']}, Setor: {curso['setor']}, "
                f"Dificuldade: {curso['dificuldade']}, Realizado: {curso['realizado']}"
            )
            print("\n")



    def seleciona_curso(self):
        print("\n")
        nome = input("Qual o nome do curso que você quer selecionar?: ")
        return nome
    
