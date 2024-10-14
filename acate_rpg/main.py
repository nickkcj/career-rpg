# teste_personagem.py
from personagemController import PersonagemController

def main():
    personagem_controller = PersonagemController()

    personagem_controller.cadastrar_personagem()

    nome_personagem = input("Digite o nome do personagem que foi cadastrado: ")

    personagem = personagem_controller.pega_personagem_por_nome(nome_personagem)

    if personagem:
        personagem_controller.mostrar_status(personagem)
    else:
        print(f"Erro: Personagem '{nome_personagem}' não encontrado.")

if __name__ == "__main__":
    main()


