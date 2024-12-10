import PySimpleGUI as psg

class LogView:
    def listar_registros(self, registros):
        if not registros:
            self.mostrar_mensagem("Nenhum registro disponível!")
            return None

        registros_formatados = [
            f"Registro {i + 1}: Personagem: {registro.personagem.nome} (Nível {registro.personagem.nivel}) | "
            f"Boss: {registro.boss.nome} (Dificuldade {registro.boss.dificuldade}) | "
            f"Dungeon: {registro.dungeon.nome} | Movimento: {registro.acao} | Data: {registro.data}"
            for i, registro in enumerate(registros)
        ]

        layout = [
            [psg.Text("Lista de Registros", font=("Helvetica", 20), justification="center")],
            [psg.Listbox(
                values=registros_formatados,
                size=(80, 20),
                key="registro_selecionado",
                enable_events=False,
                font=("Helvetica", 12)
            )],
            [psg.Button("Voltar", key="voltar", size=(15, 1), font=("Helvetica", 12))]
        ]

        window = psg.Window("Lista de Registros", layout, modal=True, finalize=True)
        while True:
            event, _ = window.read()
            if event in (psg.WINDOW_CLOSED, "voltar"):
                window.close()
                return

    def excluir_registro(self, registros):
        if not registros:
            self.mostrar_mensagem("Nenhum registro disponível para exclusão!")
            return

        registros_formatados = [
            f"Registro {i + 1}: Personagem: {registro.personagem.nome} | Boss: {registro.boss.nome} | Dungeon: {registro.dungeon.nome} | Movimento: {registro.acao}"
            for i, registro in enumerate(registros)
        ]

        layout = [
            [psg.Text("Excluir Registro", font=("Helvetica", 20), justification="center")],
            [psg.Text("Selecione um registro para excluir:", font=("Helvetica", 14))],
            [psg.Listbox(
                values=registros_formatados,
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
                return
            elif event == "excluir":
                selected_index = window["registro_selecionado"].get()
                if not selected_index:
                    self.mostrar_mensagem("Por favor, selecione um registro para excluir!")
                else:
                    index = registros_formatados.index(selected_index[0])
                    del registros[index]
                    self.mostrar_mensagem("Registro excluído com sucesso!")
                    window.close()
                    return

    def alterar_registro(self, registros):
        if not registros:
            self.mostrar_mensagem("Nenhum registro disponível para alteração!")
            return None, None

        registros_formatados = [
            f"Registro {i + 1}: Personagem: {registro.personagem.nome} | Boss: {registro.boss.nome} | Dungeon: {registro.dungeon.nome} | Movimento: {registro.acao}"
            for i, registro in enumerate(registros)
        ]

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
                    index = registros_formatados.index(selected_index[0])
                    dados = {
                        "personagem": values["personagem"],
                        "boss": values["boss"],
                        "dungeon": values["dungeon"],
                        "movimento": values["movimento"]
                    }
                    self.mostrar_mensagem("Registro alterado com sucesso!")
                    window.close()
                    return dados, index

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
