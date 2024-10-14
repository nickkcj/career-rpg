from personagemController import PersonagemController
from classePersonagem import ClassePersonagem
from pocao_hp import PocaoHP
from pocao_est import PocaoEstamina
from boss import Boss

personagem_controller = PersonagemController()

personagem_controller.cadastrar_personagem()

classe_personagem = ClassePersonagem("CLT", "0")
pocao_hp = PocaoHP(3)
pocao_est = PocaoEstamina(2)
boss = Boss("Boss Final", 5, 10, 10, 5, 50, 20)

personagem = personagem_controller.pega_personagem_por_nome("Nome do Personagem")
personagem.__classe_personagem = classe_personagem
personagem.__pocao_hp = pocao_hp
personagem.__pocao_est = pocao_est

personagem_controller.mostrar_status(personagem)

personagem_controller.atacar(boss, personagem)

personagem_controller.usar_item(personagem)

personagem_controller.usar_habilidade(personagem, boss)

