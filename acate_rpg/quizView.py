import random
import PySimpleGUI as sg

class QuizView:
    def mostra_mensagem(self, mensagem):
        sg.popup(mensagem, title="Mensagem", font=("Helvetica", 14))

    def comeca_quiz(self, dificuldade, setor, quiz):
        layout = [[sg.Text(f"Bem-vindo ao quiz de {setor}!", font=("Helvetica", 16), justification="center")],
                  [sg.Text("É necessário gabaritar para ganhar experiência!", font=("Helvetica", 14))],
                  [sg.Button("Iniciar", font=("Helvetica", 14), key="iniciar")]]
        
        window = sg.Window("Quiz", layout, finalize=True)
        while True:
            event, _ = window.read()
            if event in (sg.WINDOW_CLOSED, "iniciar"):
                window.close()
                break

        # Inicializar variáveis do quiz
        pontos = 0
        perguntas = []
        while len(perguntas) != int(dificuldade):
            numero = random.randint(1, 20)
            if numero not in perguntas:
                perguntas.append(numero)

        # Loop pelas perguntas do quiz
        for i in range(len(perguntas)):
            pergunta = quiz[str(perguntas[i])]["pergunta"]
            a = quiz[str(perguntas[i])]["a"]
            b = quiz[str(perguntas[i])]["b"]
            c = quiz[str(perguntas[i])]["c"]
            resposta_correta = quiz[str(perguntas[i])]["resposta"]

            layout_pergunta = [
                [sg.Text(f"Pergunta {i+1}/{len(perguntas)}: {pergunta}", font=("Helvetica", 14))],
                [sg.Radio(f"a) {a}", "RESPOSTA", key="a", font=("Helvetica", 12))],
                [sg.Radio(f"b) {b}", "RESPOSTA", key="b", font=("Helvetica", 12))],
                [sg.Radio(f"c) {c}", "RESPOSTA", key="c", font=("Helvetica", 12))],
                [sg.Button("Responder", key="responder", font=("Helvetica", 14))]
            ]

            window_pergunta = sg.Window(f"Quiz de {setor}", layout_pergunta, finalize=True)

            while True:
                event, values = window_pergunta.read()
                if event == sg.WINDOW_CLOSED:
                    window_pergunta.close()
                    return False  # Abandona o quiz

                if event == "responder":
                    resposta_usuario = [key for key, val in values.items() if val]
                    if not resposta_usuario:
                        self.mostra_mensagem("Opção inválida, selecione uma resposta.")
                    else:
                        resposta_usuario = resposta_usuario[0]  # Pega a resposta selecionada
                        if resposta_usuario == resposta_correta:
                            self.mostra_mensagem("Resposta correta!")
                            pontos += 1
                        else:
                            self.mostra_mensagem(f"Resposta incorreta. A resposta correta era '{resposta_correta}'.")
                        window_pergunta.close()
                        break

        # Resultado final
        if pontos == len(perguntas):
            self.mostra_mensagem("Parabéns, você gabaritou o quiz!")
            return True
        else:
            self.mostra_mensagem("Infelizmente você não foi aprovado no curso :(")
            return False



        



    