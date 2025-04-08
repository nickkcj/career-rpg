import PySimpleGUI as psg
import time
class LogView:
    def listar_registros(self, dados):
        registros = dados.get("registros", [])
        if not registros:
            self.mostrar_mensagem("Nenhum registro disponível!")
            return None

        # Convertendo os registros para um formato de texto amigável para a Listbox
        registros_display = [
            f"Personagem: {registro['personagem'].nome} - Boss: {registro['boss'].nome} - Dungeon: {registro['dungeon'].nome} - Ação: {registro['acao']} - Data: {registro['data']}"
            for registro in registros
        ]
        
        layout = [
            [psg.Text("Lista de Registros", font=("Helvetica", 20), justification="center")],
            [psg.Listbox(
                values=registros_display,
                size=(80, 20),
                key="registro_selecionado",
                enable_events=False,
                font=("Helvetica", 12)
            )],
            [psg.Button("Voltar", key="voltar", size=(15, 1), font=("Helvetica", 12))]
        ]

        # Exibição da janela
        window = psg.Window("Lista de Registros", layout, modal=True, finalize=True)
        while True:
            event, _ = window.read()
            if event in (psg.WINDOW_CLOSED, "voltar"):
                window.close()
                return




    def excluir_registro(self, dados):
        registros = dados.get("registros", [])
        if not registros:
            self.mostrar_mensagem("Nenhum registro disponível para exclusão!")
            return None

        # Convertendo os registros para um formato de texto amigável para a Listbox
        # Armazenamos também o índice original para poder encontrar o objeto de registro
        registros_formatados = [
            (f"Personagem: {registro['personagem']} | Boss: {registro['boss']} | Dungeon: {registro['dungeon']} | Ação: {registro['acao']} / Data: {registro['data']}", registro)
            for registro in registros
        ]

        layout = [
            [psg.Text("Excluir Registro", font=("Helvetica", 20), justification="center")],
            [psg.Text("Selecione um registro para excluir:", font=("Helvetica", 14))],
            [psg.Listbox(
                values=[item[0] for item in registros_formatados],  # Exibe apenas a string formatada na Listbox
                size=(80, 15),
                key="registro_selecionado",
                enable_events=False,
                font=("Helvetica", 12)
            )],
            [psg.Button("Excluir", key="excluir", size=(15, 1), font=("Helvetica", 12)),
            psg.Button("Cancelar", key="cancelar", size=(15, 1), font=("Helvetica", 12))]
        ]

        window = psg.Window("Excluir Registro", layout, modal=True, finalize=True)
        while True:
            event, values = window.read()
            if event in (psg.WINDOW_CLOSED, "cancelar"):
                window.close()
                return None
            elif event == "excluir":
                selected_index = window["registro_selecionado"].get()
                if not selected_index:
                    self.mostrar_mensagem("Por favor, selecione um registro para excluir!")
                else:
                    # Encontramos o objeto de registro original com base no índice
                    selected_item = next(item for item in registros_formatados if item[0] == selected_index[0])
                    registro_selecionado = selected_item[1]  # Objeto registro
                    window.close()
                    

                    return registro_selecionado  # Retorna o objeto completo para o controlador


    def alterar_registro(self, dados):
        registros = dados.get("registros", [])
        if not registros:
            self.mostrar_mensagem("Nenhum registro disponível para alteração!")
            return None, None

        # Criar a lista formatada para exibição
        registros_formatados = [
            f"Registro {i + 1}: Personagem: {registro['personagem'].nome} | Boss: {registro['boss'].nome} | Dungeon: {registro['dungeon'].nome} | Ação: {registro['acao']} | Data: {registro['data']}"
            for i, registro in enumerate(registros)
        ]

        # Layout da interface
        layout = [
            [psg.Text("Alterar Registro", font=("Helvetica", 20), justification="center")],
            [psg.Text("Selecione um registro para alterar:", font=("Helvetica", 14))],
            [psg.Listbox(
                values=registros_formatados,
                size=(80, 15),
                key="registro_selecionado",
                enable_events=False,
                font=("Helvetica", 12)
            )],
            [psg.Text("Novo Personagem:", font=("Helvetica", 12)), psg.InputText(key="personagem")],
            [psg.Text("Novo Boss:", font=("Helvetica", 12)), psg.InputText(key="boss")],
            [psg.Text("Nova Dungeon:", font=("Helvetica", 12)), psg.InputText(key="dungeon")],
            [psg.Text("Novo Movimento:", font=("Helvetica", 12)), psg.InputText(key="movimento")],
            [psg.Button("Salvar", key="salvar", size=(15, 1), font=("Helvetica", 12)),
            psg.Button("Cancelar", key="cancelar", size=(15, 1), font=("Helvetica", 12))]
        ]

        # Janela da interface
        window = psg.Window("Alterar Registro", layout, modal=True, finalize=True)
        while True:
            event, values = window.read()
            if event in (psg.WINDOW_CLOSED, "cancelar"):
                window.close()
                return None, None
            elif event == "salvar":
                selected_index = window["registro_selecionado"].get()
                if not selected_index:
                    self.mostrar_mensagem("Por favor, selecione um registro para alterar!")
                else:
                    # Determinar o índice do registro selecionado
                    index = registros_formatados.index(selected_index[0])

                    # Capturar os novos valores
                    dados_alterados = {
                        "personagem": values["personagem"] if values["personagem"] else registros[index]["personagem"],
                        "boss": values["boss"] if values["boss"] else registros[index]["boss"],
                        "dungeon": values["dungeon"] if values["dungeon"] else registros[index]["dungeon"],
                        "movimento": values["movimento"] if values["movimento"] else registros[index]["acao"],
                        "data": registros[index]["data"]
                    }

                    self.mostrar_mensagem("Registro alterado com sucesso!")
                    window.close()
                    return dados_alterados, index



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
