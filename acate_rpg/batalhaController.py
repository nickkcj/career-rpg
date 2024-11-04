from batalha import Batalha
from batalhaView import BatalhaView
from personagemController import PersonagemController
import time
import random
from exceptions import OperacaoNaoPermitidaException, HpJahCheioException
from bossController import BossController
import os
class BatalhaController():
    def __init__(self, batalha: Batalha):
        self.__batalha = batalha
        self.__tela = BatalhaView()
        self.__personagemController = PersonagemController()
        self.__bossController = BossController()
        self.defesas = 0

    def realizar_turno(self, acao_personagem, personagem, boss, dungeon, log):
        if acao_personagem == 1: 
            dano = self.__personagemController.atacar(personagem, boss)
            boss.atributos['hp'] = max(boss.atributos['hp'] - dano, 0)
            self.__tela.mostra_mensagem(f"{personagem.nome} atacou {boss.nome} e causou {dano} de dano!")
            log.adicionar_registro(personagem, boss, dungeon, "ataque")
            time.sleep(3)
            self.verificar_vencedor()
            self.turno_boss(personagem, boss)
            time.sleep(3)

        elif acao_personagem == 2:
            self.__personagemController.defender(personagem)
            self.__tela.mostra_mensagem(f"{personagem.nome} aumentou a defesa em {personagem.classe_personagem.atributos['defesa']}!")
            log.adicionar_registro(personagem, boss, dungeon, "defesa")
            self.defesas += 1
            time.sleep(3)
            self.turno_boss(personagem, boss)
            time.sleep(3)
        elif acao_personagem == 3:
            self.__personagemController.usar_item(personagem)
            log.adicionar_registro(personagem, boss, dungeon, "usar item")
            self.turno_boss(personagem, boss)
            time.sleep(3)

        elif acao_personagem == 4:
            self.__personagemController.usar_habilidade(personagem, boss)
            log.adicionar_registro(personagem, boss, dungeon, "usar habilidade")
            self.turno_boss(personagem, boss)
            time.sleep(3)

        else:
            raise OperacaoNaoPermitidaException("Opção inválida, tente novamente.")

    def usar_item(self, personagem):
        opcao = self.__personagemController.usar_itens_batalha(personagem)
        while True:
            try:
                if opcao == '1':
                    if personagem.hp_atual < personagem.classe_personagem.atributos['hp']:
                        personagem.hp_atual += 10
                        personagem.pocao_hp.quant -= 1
                        self.__tela.mostra_mensagem(f"O personagem {personagem.nome} se curou em 10 de vida")
                        time.sleep(2)
                        break
                    else:
                        raise HpJahCheioException("Não é possível usar a Poção de HP, o seu HP já está Cheio!")

                else:
                    personagem.classe_personagem.atributos['estamina'] += 10
                    self.__tela.mostra_mensagem(f"O personagem {personagem.nome} restaurou 10 de estamina")
                    time.sleep(2)
                    break
            except HpJahCheioException as e:
                self.__tela.mostra_mensagem(str(e))

    def turno_boss(self, personagem, boss):
        acao_boss = random.randint(1, 2)  
        if acao_boss == 1:
            dano = self.__bossController.atacar(personagem, boss)
            personagem.hp_atual -= dano
            self.__tela.mostra_mensagem(f"{boss.nome} atacou {personagem.nome} e causou {dano} de dano!")
            time.sleep(1.5)
            
        else:      
            self.__bossController.defender(boss)
            
            self.__tela.mostra_mensagem(f"{boss.nome} se defendeu! Defesa aumentada para {boss.atributos['defesa']}.")
            time.sleep(1.5)

    def verificar_vencedor(self):
        if self.__batalha.boss.atributos['hp'] <= 0:
            self.__batalha.finalizada = True
            return "vitória"
        elif self.__batalha.personagem.hp_atual <= 0:
            self.__batalha.finalizada = True
            return "derrota"
        return

    def iniciar_batalha(self, personagem, boss, dungeon, setor, log):
        self.__batalha.personagem = personagem
        self.__batalha.boss = boss
        self.__batalha.finalizada = False
        while not self.__batalha.finalizada:
            self.__tela.exibir_tela_batalha(personagem, boss)
            acao_personagem = self.__tela.tela_opcoes()
            while True:
                try:
                    self.realizar_turno(acao_personagem, self.__batalha.personagem, boss, dungeon, log)
                    break

                except OperacaoNaoPermitidaException:
                    self.__tela.mostra_mensagem("Opção inválida, tente novamente!")
                    time.sleep(2)
                    os.system('cls' if os.name == 'nt' else 'clear')

            resultado = self.verificar_vencedor()
            if resultado == "vitória":
                self.__tela.mostra_resultado("Você venceu!")
                time.sleep(2)
                personagem.bosses_derrotados.append(boss)
                if boss.nome == dungeon.boss_final.nome:
                    dungeon.conquistada = True
                    personagem.dungeons_conquistadas.append(dungeon)
                    self.__tela.mostra_mensagem(f"Voce conquistou a {dungeon.nome}!")
                    time.sleep(1)
                    self.__personagemController.ganhar_experiencia(personagem, dungeon.boss_final.dificuldade * 100)
                    personagem.classe_personagem.atributos['defesa'] -= (self.defesas * 7.5)
                elif boss.nome == setor.boss.nome:
                    setor.conquistado = True
                    personagem.bosses_derrotados.append(boss)
                    self.__tela.mostra_mensagem(f"Voce conquistou o setor {setor.nome} da {dungeon.nome}!")
                    personagem.hp_atual = min(personagem.hp_atual + 20, personagem.classe_personagem.atributos["hp"])
                    time.sleep(1)
                    self.__personagemController.ganhar_experiencia(personagem, boss.dificuldade * 100)
                    personagem.classe_personagem.atributos['defesa'] -= (self.defesas * 7.5)
                    setor.conquistado = True

            elif resultado == "derrota":
                self.__tela.mostra_resultado("Você foi derrotado!")
                personagem.classe_personagem.atributos['defesa'] -= (self.defesas * 7.5)
                personagem.hp_atual = (personagem.classe_personagem.atributos['hp']/2)
                time.sleep(2)

