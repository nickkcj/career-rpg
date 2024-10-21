import os
import random
class QuizView():
    
    def mostra_mensagem(self, mensagem):
        print(mensagem)

    def limpar_terminal(self):
        # Limpa o terminal dependendo do sistema operacional
        os.system('cls' if os.name == 'nt' else 'clear')

    def comeca_quiz(self, setor):
        self.limpar_terminal()
        print(f"Bem-vindo ao quiz de RH ! Responda as perguntas abaixo:\n")
        
        
        pontos = 0
        perguntas = []
        while len(perguntas) != 5:
            numero = random.randint(1,20)
            if numero not in perguntas:
                perguntas.append(numero)

        
        for i in range(0, 5): 
            pergunta = setor[str(perguntas[i])]["pergunta"]
            a = setor[str(perguntas[i])]["a"]
            b = setor[str(perguntas[i])]["b"]
            c = setor[str(perguntas[i])]["c"]
            resposta_correta = setor[str(perguntas[i])]["resposta"]
            
            
            print(f"{(perguntas[i])}. {pergunta}")
            print(f"a) {a}")
            print(f"b) {b}")
            print(f"c) {c}")
            
            
            resposta_usuario = input("Digite a sua resposta (a, b ou c): ").lower()
            
            
            if resposta_usuario == resposta_correta:
                print("Resposta correta!\n")
                pontos += 1  # Incrementar a pontuação
            else:
                print(f"Resposta incorreta. A resposta correta era '{resposta_correta}'.\n")

        
        if pontos == 5:
            print("Parabéns, você gabaritou o quiz!")



    