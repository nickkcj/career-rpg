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

    def escolher_habilidade(self):
        #colocar a logica do personagem escolher a habilidade
        pass

    def mostra_resultado(self, mensagem):
        print(mensagem)

    def mostra_mensagem(self, msg):
        print(msg)


    def exibir_tela_batalha(personagem, boss):
        print("=" * 40)
        
        print(f"{personagem.nome:<15} VS {boss.nome:<15}")
        print("-" * 40)
        
        print(f"{'HP:':<10} {personagem.atributos['hp']:<10} {'HP:':<10} {boss.atributos['hp']}")
        print(f"{'Ataque:':<10} {personagem.atributos['ataque']:<10} {'Ataque:':<10} {boss.atributos['ataque']}")
        print(f"{'Defesa:':<10} {personagem.atributos['defesa']:<10} {'Defesa:':<10} {boss.atributos['defesa']}")
        print(f"{'Estamina:':<10} {personagem.atributos['estamina']:<10} {'Estamina:':<10} {boss.atributos['estamina']}")
        print("=" * 40)



