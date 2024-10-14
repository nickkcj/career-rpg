
class BossView:
    def pega_dados_boss(self):
        print("----------CADASTRO BOSS---------")
        nome = input("Nome: ")
        dificuldade = int(input("Dificuldade: "))
        nivel_requerido = int(input("Nível Requerido: "))
        diretor = input("É o diretor? (S/N): ")
        diretor = False if diretor == "N" else True if diretor == "S" else None
        ataque = dificuldade * 2
        defesa = (dificuldade * 2) + 5
        hp = (dificuldade**2) + 25
        estamina = dificuldade * 2

        
        return {
            'nome': nome,
            'dificuldade': dificuldade,
            'nivel_requerido': nivel_requerido,
            'ataque': ataque,
            'defesa': defesa,
            'hp': hp,
            'estamina': estamina,
            'diretor': diretor
        }

    def mostra_atributos(self, atributos):
        print(atributos)

    def mostra_mensagem(self, msg):
        print(msg)

        