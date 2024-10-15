import os
class PersonagemView():

    def mostrar_status(self, dados_personagem):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("-------- STATUS ----------")
        print(f"Nome: {dados_personagem['nome']}")
        print(f"Nível: {dados_personagem['nivel']}")
        print(f"Experiência: {dados_personagem['experiencia']}")
        print(f"Ataque: {dados_personagem['ataque']}")
        print(f"Defesa: {dados_personagem['defesa']}")
        print(f"HP: {dados_personagem['hp']}")
        print(f"Estamina: {dados_personagem['estamina']}")
        print(f"Pontos disponíveis para distribuir: {dados_personagem['pontos_disponiveis']}")
        print(f"Poções de HP: {dados_personagem['pocoes_hp']}")
        print(f"Poções de Estamina: {dados_personagem['pocoes_est']}")

    def escolher_atributo(self):
        os.system('cls' if os.name == 'nt' else 'clear')
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
    
    def escolher_item(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Escolha o item para usar:")
        print("1 - Poção de HP")
        print("2 - Poção de Estamina")
        return int(input("Digite o número do item: "))

    def escolher_habilidade(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Escolha a habilidade:")
        print("1 - hab1")
        print("2 - hab2")
        print("3 - hab3")
        #Colocar logica para que as habilidades mostradas sejam somente aquelas que a classe tem, tipo, trainee só tem
        # a primeira habilidade, enquanto o estagiario tem a primeira e a segunda, e o CLT tem a primeira, segunda e a terceira.
        return int(input("Digite o número da habilidade: "))

    def mostra_mensagem(self, msg):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("****************************************")
        print(msg)
        print("****************************************")

        