import PySimpleGUI as sg

class LogView:
    def listar_registros(self, registros):
        layout = [
            [sg.Text("Registros", font=("Helvetica", 20))],
            [
                sg.Multiline(
                    "\n".join(
                        [
                            f"Registro {i}:\n  Personagem: {registro.personagem.nome} (Nível {registro.personagem.nivel})\n  Boss: {registro.boss.nome} (Dificuldade {registro.boss.dificuldade})\n  Dungeon: {registro.dungeon.nome}\n  Movimento: {registro.acao}\n  Data: {registro.data}\n"
                            for i, registro in enumerate(registros, 1)
                        ]
                    ),
                    size=(80, 20),
                    disabled=True,
                    key="REGISTROS",
                )
            ],
            [sg.Button("Voltar", size=(10, 2))]
        ]

        window = sg.Window("Listar Registros", layout, modal=True, finalize=True)
        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "Voltar"):
                break
        window.close()

    def excluir_registro(self, registros):
        layout = [
            [sg.Text("Excluir Registro", font=("Helvetica", 20))],
            [sg.Text("Digite o índice do registro a ser excluído:")],
            [sg.Input(size=(20, 1), key="INDEX")],
            [sg.Button("Excluir", size=(10, 2)), sg.Button("Cancelar", size=(10, 2))]
        ]

        window = sg.Window("Excluir Registro", layout, modal=True, finalize=True)
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None
            if event == "Excluir":
                try:
                    index = int(values["INDEX"]) - 1
                    if 0 <= index < len(registros):
                        window.close()
                        return index
                    sg.popup_error("Índice inválido.")
                except ValueError:
                    sg.popup_error("Por favor, insira um número válido.")

    def alterar_registro(self, registros):
        layout = [
            [sg.Text("Alterar Registro", font=("Helvetica", 20))],
            [sg.Text("Digite o índice do registro a ser alterado:")],
            [sg.Input(size=(20, 1), key="INDEX")],
            [sg.Button("Selecionar", size=(10, 2)), sg.Button("Cancelar", size=(10, 2))]
        ]

        window = sg.Window("Alterar Registro", layout, modal=True, finalize=True)
        while True:
            event, values = window.read()
            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                window.close()
                return None, None
            if event == "Selecionar":
                try:
                    index = int(values["INDEX"]) - 1
                    if 0 <= index < len(registros):
                        window.close()
                        registro = registros[index]
                        dados_layout = [
                            [sg.Text(f"Alterar Registro {index + 1}", font=("Helvetica", 20))],
                            [sg.Text("Nome do personagem:"), sg.Input(registro.personagem.nome, key="PERSONAGEM")],
                            [sg.Text("Nível do personagem:"), sg.Input(registro.personagem.nivel, key="NIVEL")],
                            [sg.Text("Nome do boss:"), sg.Input(registro.boss.nome, key="BOSS")],
                            [sg.Text("Dificuldade do boss:"), sg.Input(registro.boss.dificuldade, key="DIFICULDADE")],
                            [sg.Text("Nome da dungeon:"), sg.Input(registro.dungeon.nome, key="DUNGEON")],
                            [sg.Text("Movimento realizado:"), sg.Input(registro.acao, key="MOVIMENTO")],
                            [sg.Button("Salvar", size=(10, 2)), sg.Button("Cancelar", size=(10, 2))]
                        ]

                        dados_window = sg.Window("Alterar Registro", dados_layout, modal=True, finalize=True)
                        while True:
                            event, dados_values = dados_window.read()
                            if event in (sg.WINDOW_CLOSED, "Cancelar"):
                                dados_window.close()
                                return None, None
                            if event == "Salvar":
                                dados_window.close()
                                return {
                                    "personagem": dados_values["PERSONAGEM"],
                                    "nivel": int(dados_values["NIVEL"]),
                                    "boss": dados_values["BOSS"],
                                    "dificuldade": int(dados_values["DIFICULDADE"]),
                                    "dungeon": dados_values["DUNGEON"],
                                    "movimento": dados_values["MOVIMENTO"]
                                }, index
                except ValueError:
                    sg.popup_error("Por favor, insira um número válido.")

    def mostrar_mensagem(self, mensagem):
        sg.popup(mensagem, title="Mensagem")
