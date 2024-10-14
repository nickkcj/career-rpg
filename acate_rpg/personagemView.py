
class PersonagemView():
    def mostrar_status(self, dados_personagem):
        print(f"Nome: {dados_personagem['nome']}")
        print(f"Nível: {dados_personagem['nivel']}")
        print(f"Experiência: {dados_personagem['experiencia']}")
        print(f"HP: {dados_personagem['hp']}")
        print(f"Estamina: {dados_personagem['estamina']}")

    def pega_dados_personagem(self):
        print("----------CADASTRO PERSONAGEM---------")
        nome = input("Nome: ")
        if not isinstance(nome, str):
            raise Exception("Nome inválido")

        print("-------- CLASSES ----------")
        print("Escolha uma classe:")
        print("1 - CLT (Bom no early game)")
        print("2 - Estagiário (Médio no early, bom no late)")
        print("3 - Trainee (Fraco no early, muito forte no late)")

        opcao = int(input("Digite o número da classe: "))
        classe = "CLT" if opcao == 1 else "Estagiário" if opcao == 2 else "Trainee" if opcao == 3 else None
        if not classe:
            raise Exception("Classe não encontrada")

        return {"nome": nome, "classe": classe, "nivel": 1, "experiencia": 0}
    
    def escolher_item(self):
        print("Escolha o item para usar:")
        print("1 - Poção de HP")
        print("2 - Poção de Estamina")
        return int(input("Digite o número do item: "))

    def escolher_habilidade(self):
        print("Escolha a habilidade:")
        print("1 - hab1")
        print("2 - hab2")
        print("3 - hab3")
        #Colocar logica para que as habilidades mostradas sejam somente aquelas que a classe tem, tipo, trainee só tem
        # a primeira habilidade, enquanto o estagiario tem a primeira e a segunda, e o CLT tem a primeira, segunda e a terceira.
        return int(input("Digite o número da habilidade: "))

    def mostra_mensagem(self, msg):
        print(msg)

        