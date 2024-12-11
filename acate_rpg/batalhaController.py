from batalha import Batalha
from batalhaView import BatalhaView
from personagemController import PersonagemController
from classePersonagemController import ClassePersonagemController
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
        self.__classepersonagemController = ClassePersonagemController()
        self.defesas = 0

    def realizar_turno(self, acao_personagem, personagem, boss, dungeon, log, window):
        if acao_personagem == "Atacar": 
            dano = personagem.classe_personagem.atacar(boss)
            boss.atributos['hp'] = max(boss.atributos['hp'] - dano, 0)
            imagem_ataque = "assets/images/ataque.jpg"
            window["-IMG-"].update(filename=imagem_ataque, size=(800,600))
            self.__tela.mostra_mensagem(f"{personagem.nome} atacou {boss.nome} e causou {dano} de dano!")
            log.adicionar_registro(personagem, boss, dungeon, "ataque")
            self.atualizar_status(window, personagem, boss)
            self.verificar_vencedor()
            self.turno_boss(personagem, boss, window)
        
        elif acao_personagem == "Defender":
            self.__classepersonagemController.defender(personagem)
            personagem_defesa = "assets/images/personagem_defesa.jpg"
            window["-IMG-"].update(filename=personagem_defesa, size=(800,600))            
            self.__tela.mostra_mensagem(f"{personagem.nome} aumentou a defesa em {personagem.classe_personagem.atributos['defesa']}!")
            log.adicionar_registro(personagem, boss, dungeon, "defesa")
            self.defesas += 1
            self.turno_boss(personagem, boss, window)
        elif acao_personagem == "Usar Item":
            self.__personagemController.usar_item(personagem)
            log.adicionar_registro(personagem, boss, dungeon, "usar item")
            self.turno_boss(personagem, boss, window)

        elif acao_personagem == "Usar Habilidade":
            self.__personagemController.usar_habilidade(personagem, boss)
            log.adicionar_registro(personagem, boss, dungeon, "usar habilidade")
            self.turno_boss(personagem, boss, window)

        else:
            raise OperacaoNaoPermitidaException("Opção inválida, tente novamente.")

        self.__personagemController.atualizar_personagem(personagem)

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

    def turno_boss(self, personagem, boss, window):
        acao_boss = random.randint(1, 5)  
        if acao_boss in (1, 2, 3, 4):
            dano = self.__bossController.atacar(boss, personagem)
            personagem.hp_atual -= dano
            boss_ataque = "assets/images/boss_ataque.jpg"
            window["-IMG-"].update(filename=boss_ataque, size=(800,600))
            self.__tela.mostra_mensagem(f"{boss.nome} atacou {personagem.nome} e causou {dano} de dano!")
            time.sleep(1)
            self.atualizar_status(window,personagem,boss)
            batalha = "assets/images/personagem_boss.jpg"
            window["-IMG-"].update(filename=batalha, size=(800,600))
            
        else:      
            self.__bossController.defender(boss)
            boss_defesa = "assets/images/boss_defesa.jpg"
            window["-IMG-"].update(filename=boss_defesa, size=(800,600))
            self.__tela.mostra_mensagem(f"{boss.nome} se defendeu! Defesa aumentada para {boss.atributos['defesa']}.")
            self.atualizar_status(window,personagem,boss)
            time.sleep(1)
            batalha = "assets/images/personagem_boss.jpg"
            window["-IMG-"].update(filename=batalha, size=(800,600))

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
        window = self.__tela.exibir_tela_batalha(personagem,boss)
        while not self.__batalha.finalizada:
            event, _ = window.read()
            self.realizar_turno(event, self.__batalha.personagem, boss, dungeon, log, window)

            resultado = self.verificar_vencedor()
            if resultado == "vitória":
                vitoria = "assets/images/vitoria.jpg"
                window["-IMG-"].update(filename=vitoria, size=(800,600))
                self.__tela.mostra_resultado("Você venceu!")
                window.close()
                time.sleep(1)
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
                    break

            elif resultado == "derrota":
                self.__tela.mostra_resultado("Você foi derrotado!")
                personagem.classe_personagem.atributos['defesa'] -= (self.defesas * 7.5)
                personagem.hp_atual = (personagem.classe_personagem.atributos['hp']/2)
                break
                

        self.__personagemController.atualizar_personagem(personagem)
        window.close()

    def atualizar_status(self, window, personagem, boss):
        window["-PERSONAGEM_HP-"].update(f"HP: {personagem.hp_atual}/{personagem.classe_personagem.atributos['hp']}")
        window["-BOSS_HP-"].update(F"HP: {boss.atributos['hp']}")