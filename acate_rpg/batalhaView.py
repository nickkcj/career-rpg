import os
class BatalhaView:
    def tela_opcoes(self):
        print("-------- BATALHA ----------")
        print("Escolha a ação:")
        print("1 - Atacar")
        print("2 - Defender")
        print("3 - Usar Item")
        print("4 - Usar Habilidade")

        opcao = int(input("Escolha a ação: "))
        return opcao

    def escolher_habilidade(self, classe):
        if classe == 'CLT':
            print("\n")
            print("------Escolha sua habilidade!------")
            print("\n")
            print("1 - Festa da Firma, efeito: Aumenta o Ataque do personagem, tipo: buff")
            print("\n")
            print("2 - Ataque Corporativo, efeito: Dano direto ao HP do boss, tipo: dano")
            print("\n")
            opcao = input("Digite o número da habilidade: ")

        elif classe == 'Estagiario':
            print("\n")
            print("------Escolha sua habilidade!------")
            print("\n")
            print("1 - Cagada Remunerada, efeito: Aumenta o HP do personagem, tipo: buff")
            print("\n")
            print("2 - Desestabilizar Boss, efeito: Reduz a defesa do boss, tipo: debuff")
            print("\n")
            opcao = input("Digite o número da habilidade: ")

        elif classe == 'Trainee':
            print("\n")
            print("------Escolha sua habilidade!------")
            print("\n")
            print("1 - Hora Extra, efeito: Aumenta a estamina, tipo: buff")
            print("\n")
            print("2 - Desmotivar Boss, efeito: Reduz o ataque do boss, tipo: debuff")
            print("\n")
            opcao = input("Digite o número da habilidade: ")

        return opcao
        

    def mostra_resultado(self, mensagem):
        print(mensagem)

    def mostra_mensagem(self, msg):
        print("\n")
        print(msg)
        print("\n")


    def exibir_tela_batalha(self, personagem, boss):
        os.system('cls' if os.name == 'nt' else 'clear')
        largura_total = 60  
        margem_personagem = 7  
        margem_boss = 10  
        ajuste_direita = 5  

        
        espacos_entre_nomes = largura_total - margem_personagem - margem_boss - len(personagem.nome) - len(boss.nome) - len(" VS ")

        print("=" * largura_total)
        print(f"{' ' * margem_personagem}{personagem.nome}{' ' * (espacos_entre_nomes // 2)}VS{' ' * (espacos_entre_nomes // 2)}{boss.nome}")
        print("-" * largura_total)

        
        espacos_boss = margem_personagem + len(personagem.nome) + (espacos_entre_nomes // 2) + len(" VS ") + ajuste_direita

        
        print(f"{' ' * margem_personagem}{'HP:':<10}{str(personagem.hp_atual) + ' / ' + str(personagem.classe_personagem.atributos['hp']):<10}{' ' * (espacos_boss - margem_personagem - 20)}{'HP:':<10}{boss.atributos['hp']}")
        print(f"{' ' * margem_personagem}{'Ataque:':<10}{personagem.classe_personagem.atributos['ataque']:<10}{' ' * (espacos_boss - margem_personagem - 20)}{'Ataque:':<10}{boss.atributos['ataque']}")
        print(f"{' ' * margem_personagem}{'Defesa:':<10}{personagem.classe_personagem.atributos['defesa']:<10}{' ' * (espacos_boss - margem_personagem - 20)}{'Defesa:':<10}{boss.atributos['defesa']}")
        print(f"{' ' * margem_personagem}{'Estamina:':<10}{personagem.classe_personagem.atributos['estamina']:<10}{' ' * (espacos_boss - margem_personagem - 20)}{'Estamina:':<10}{boss.atributos['estamina']}")
        print("=" * largura_total)







