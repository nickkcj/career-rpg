from boss import Boss
import time


class BossController:
    def criar_boss(self, nome, dificuldade, nivel_requerido, ataque, defesa, hp, estamina):
        ataque = dificuldade * 2
        defesa = dificuldade * 1.5
        hp = dificuldade * 10
        estamina = dificuldade * 5
        #print(f"Criando boss: {nome}, Dificuldade: {dificuldade}, Nível Requerido: {nivel_requerido}")
        #time.sleep(1)
        return Boss(nome=nome, dificuldade=dificuldade, nivel_requerido=nivel_requerido, ataque=ataque, defesa=defesa, hp=hp, estamina=estamina)

    def criar_boss_final(self, nome, dificuldade, nivel_requerido):
        ataque = dificuldade * 4
        defesa = dificuldade * 3
        hp = dificuldade * 20 
        estamina = dificuldade * 10
        #print(f"Criando boss final: {nome}, Dificuldade: {dificuldade}, Nível Requerido: {nivel_requerido}")
        #time.sleep(1)
        return Boss(nome=nome, dificuldade=dificuldade, nivel_requerido=nivel_requerido, ataque=ataque, defesa=defesa, hp=hp, estamina=estamina)
    
    def to_dict(self, boss):
        return {
            "nome": boss.nome,
            "dificuldade": boss.dificuldade,
            "nivel_requerido": boss.nivel_requerido,
            "atributos": {
                "ataque": boss.atributos['ataque'],
                "defesa": boss.atributos['defesa'],
                "hp": boss.atributos['hp'],
                "estamina": boss.atributos['estamina'],
            }
        }

    def criar_boss_de_dicionario(self, boss_data):
        return Boss(nome=boss_data["nome"], dificuldade=boss_data["dificuldade"], nivel_requerido=boss_data["nivel_requerido"], atributos=boss_data["atributos"])
