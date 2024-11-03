from batalha import Batalha
from batalhaView import BatalhaView
from personagemController import PersonagemController
import time
import random

class BatalhaController():
    def __init__(self, batalha: Batalha):
        self.__batalha = batalha
        self.__tela = BatalhaView()
        self.__personagemController = PersonagemController()

    def realizar_turno(self, acao_personagem, personagem, boss):

        if acao_personagem == 1: 
            dano = self.atacar(personagem, boss)
            boss.atributos['hp'] -= dano
            self.__tela.mostra_mensagem(f"{personagem.nome} atacou {boss.nome} e causou {dano}!")
            time.sleep(3)
            self.turno_boss(personagem, boss)
            time.sleep(3)
            
        elif acao_personagem == 2:
            personagem.defender()
            self.__tela.mostra_mensagem(f"{personagem.nome} se defendeu!")
        elif acao_personagem == 3:
            pass
        elif acao_personagem == 4:
            personagem.usar_habilidade(boss)
            self.__tela.mostra_mensagem(f"{personagem.nome} usou uma habilidade!")

        else:
            pass

    
    def atacar(self, personagem, boss):
        dano = max(personagem.classe_personagem.atributos['ataque'] - boss.atributos['defesa'], 1)
        return dano


    def turno_boss(self, personagem, boss):
        self.boss_defesa_original = boss.atributos['defesa']
        acao_boss = random.randint(1, 2)  
        if acao_boss == 1:
            self.boss_defesa_original = None
            dano = max(boss.atributos['ataque'] - personagem.classe_personagem.atributos['defesa'], 1)
            personagem.classe_personagem.atributos['hp'] -= dano
            self.__tela.mostra_mensagem(f"{boss.nome} atacou {personagem.nome} e causou {dano} de dano!")
            
            boss.atributos['defesa'] = self.boss_defesa_original if self.boss_defesa_original else boss.atributos['defesa']
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
                self.__personagemController.ganhar_experiencia(personagem, boss.dificuldade * 100)
                dungeon.conquistada = True
                personagem.dungeons_conquistadas.append(dungeon)
                print(personagem.dungeons_conquistadas)
                time.sleep(2)

            elif resultado == "derrota":
                self.__tela.mostra_resultado("Você foi derrotado!")


    


                