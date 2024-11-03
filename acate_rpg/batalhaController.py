from batalha import Batalha
from batalhaView import BatalhaView
from personagemController import PersonagemController
import time
import random
from exceptions import OperacaoNaoPermitidaException
class BatalhaController():
    def __init__(self, batalha: Batalha):
        self.__batalha = batalha
        self.__tela = BatalhaView()
        self.__personagemController = PersonagemController()

    def realizar_turno(self, acao_personagem, personagem, boss):

        if acao_personagem == 1: 
            dano = self.atacar(personagem, boss)
            boss.atributos['hp'] -= dano
            self.__tela.mostra_mensagem(f"{personagem.nome} atacou {boss.nome} e causou {dano} de dano!")
            time.sleep(3)
            self.turno_boss(personagem, boss)
            time.sleep(3)
            
        elif acao_personagem == 2:
            self.defender(personagem)
            self.__tela.mostra_mensagem(f"{personagem.nome} aumentou a defesa em {personagem.classe_personagem.atributos['defesa']}!")
            time.sleep(3)
            self.turno_boss(personagem, boss)
            time.sleep(3)
        elif acao_personagem == 3:
            self.usar_item(personagem)
            self.turno_boss(personagem, boss)
            time.sleep(3)

        elif acao_personagem == 4:
            self.usar_habilidade(personagem, boss)
            self.turno_boss(personagem, boss)
            time.sleep(3)

        else:
            raise OperacaoNaoPermitidaException("Opção inválida, tente novamente.")

    
    def atacar(self, personagem, boss):
        dano = max(personagem.classe_personagem.atributos['ataque'] - boss.atributos['defesa'], 1)
        return dano
    
    def defender(self, personagem):
        personagem.classe_personagem.atributos['defesa'] += 5

    def usar_habilidade(self, personagem, boss):
        classe = personagem.classe_personagem.nome_classe
        opcao = self.__tela.escolher_habilidade(classe)
        if personagem.classe_personagem.atributos['estamina'] >= 2:

            if classe == 'CLT' and opcao == '1':
                personagem.classe_personagem.atributos['estamina'] -= 2
                personagem.classe_personagem.atributos['ataque'] += 5
                self.__tela.mostra_mensagem(f"O personagem {personagem.nome} usou a habilidade *Festa da Firma* e aumentou seu ataque em 5 pontos!")
                time.sleep(2)

            elif classe == 'CLT' and opcao == '2':
                personagem.classe_personagem.atributos['estamina'] -= 2
                boss.atributos['hp'] -= 10
                self.__tela.mostra_mensagem(f"O personagem {personagem.nome} usou a habilidade *Ataque Corporativo* e diminuiu o HP do boss em 10 pontos!")
                time.sleep(2)

            elif classe == 'Estagiario' and opcao == '1':
                personagem.classe_personagem.atributos['estamina'] -= 2
                personagem.classe_personagem.atributos['hp'] += 10
                self.__tela.mostra_mensagem(f"O personagem {personagem.nome} usou a habilidade *Cagada Remunerada* e aumentou seu HP em 10 pontos!")
                time.sleep(2)

            elif classe == 'Estagiario' and opcao == '2':
                personagem.classe_personagem.atributos['estamina'] -= 2
                boss.atributos['defesa'] = max(boss.atributos['defesa'] - 5, 1)
                self.__tela.mostra_mensagem(f"O personagem {personagem.nome} usou a habilidade *Desestabilizar Boss* e diminuiu a defesa do boss em 7.5 pontos!")
                time.sleep(2)

            elif classe == 'Trainee' and opcao == '1':
                personagem.classe_personagem.atributos['estamina'] -= 2
                personagem.classe_personagem.atributos['estamina'] += 10
                self.__tela.mostra_mensagem(f"O personagem {personagem.nome} usou a habilidade *Hora Extra* e aumentou sua estamina em 10 pontos!")
                time.sleep(2)

            elif classe == 'Trainee' and opcao == '2':
                personagem.classe_personagem.atributos['estamina'] -= 2
                boss.atributos['ataque'] -= 7.5
                self.__tela.mostra_mensagem(f"O personagem {personagem.nome} usou a habilidade *Desmotivar Inimigo* e reduziu o ataque do boss em 7.5 pontos!")
                time.sleep(2)

            else:
                raise OperacaoNaoPermitidaException("Opção inválida, tente novamente")
            
        else:
            self.__tela.mostra_mensagem("O personagem não possui estamina o suficiente para usar uma habilidade!")

    def usar_item(self, personagem):
        opcao = self.__personagemController.usar_itens(personagem)
        if opcao == '1':
            personagem.classe_personagem.atributos['hp'] += 10
            self.__tela.mostra_mensagem(f"O personagem {personagem.nome} se curou em 10 de vida")
            time.sleep(2)

        else:
            personagem.classe_personagem.atributos['estamina'] += 10
            self.__tela.mostra_mensagem(f"O personagem {personagem.nome} restaurou 10 de estamina")
            time.sleep(2)



    def turno_boss(self, personagem, boss):
        acao_boss = random.randint(1, 2)  
        if acao_boss == 1:
            dano = max(boss.atributos['ataque'] * 2 - personagem.classe_personagem.atributos['defesa'], 1)
            personagem.classe_personagem.atributos['hp'] -= dano
            self.__tela.mostra_mensagem(f"{boss.nome} atacou {personagem.nome} e causou {dano} de dano!")
            
        else:      
            boss.atributos['defesa'] += 5
            
            self.__tela.mostra_mensagem(f"{boss.nome} se defendeu! Defesa aumentada para {boss.atributos['defesa']}.")



        

        

    def verificar_vencedor(self):
        if self.__batalha.boss.atributos['hp'] <= 0:
            self.__batalha.finalizada = True
            return "vitória"
        elif self.__batalha.personagem.classe_personagem.atributos['hp'] <= 0:
            self.__batalha.finalizada = True
            return "derrota"
        return

    def iniciar_batalha(self, personagem, boss, dungeon):
        self.__batalha.personagem = personagem
        self.__batalha.boss = boss
        self.__batalha.finalizada = False
        while not self.__batalha.finalizada:
            self.__tela.exibir_tela_batalha(personagem, boss)
            acao_personagem = self.__tela.tela_opcoes()
            self.realizar_turno(acao_personagem, self.__batalha.personagem, boss)

            resultado = self.verificar_vencedor()
            if resultado == "vitória":
                self.__tela.mostra_resultado("Você venceu!")
                time.sleep(2)
                self.__personagemController.ganhar_experiencia(personagem, boss.dificuldade * 100)
                dungeon.conquistada = True
                personagem.dungeons_conquistadas.append(dungeon)
                time.sleep(2)

            elif resultado == "derrota":
                self.__tela.mostra_resultado("Você foi derrotado!")
                time.sleep(2)


    


                