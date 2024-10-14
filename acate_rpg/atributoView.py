import os

class AtributoView():
    def mostrar_atributo(self, dados):
        print(f"ataque: {dados['ataque']}")
        print(f"defesa: {dados['defesa']}")
        print(f"hp: {dados['hp']}")
        print(f"estamina: {dados['estamina']}")
    
    def selecionar_atributo(self):
        print("-------- ATRIBUTOS ----------")
        print("Escolha o atributo:")
        print("1 - ataque")
        print("2 - defesa")
        print("3 - hp")
        print("4 - estamina")
        print("5 - Voltar")

        opcao = int(input("Digite o número: "))
         return opcao
    
            
    def incrementar_atributo(opcao):
        match(opcao):
            case 1:
                print("Atributo escolhido: ataque")
                print("\n")
                print("Quantos pontos aumentar?")
                num = int(input("Digite o numero: "))
                if num == 0 or not isinstance(num, int):
                    return
                else:
                    return num
            case 2:
                print("Atributo escolhido: defesa")
                print("\n")
                print("Quantos pontos aumentar?")
                num = int(input("Digite o numero: "))
                if num == 0 or not isinstance(num, int):
                    return
                else:
                    return num
            case 3:
                print("Atributo escolhido: hp")
                print("\n")
                print("Quantos pontos aumentar?")
                num = int(input("Digite o numero: "))
                if num == 0 or not isinstance(num, int):
                    return
                else:
                    return num
            case 4:
                print("Atributo escolhido: estamina")
                print("\n")
                print("Quantos pontos aumentar?")
                num = int(input("Digite o numero: "))
                if num == 0 or not isinstance(num, int):
                    return
                else:
                    return num
            case _:
                return


