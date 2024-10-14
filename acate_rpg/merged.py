class Atributo:
    def __init__(self, ataque=0, defesa=0, hp=0, estamina=0):
        self.__atributos = {
            'ataque': ataque,
            'defesa': defesa,
            'hp': hp,
            'estamina': estamina
        }

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, novos_atributos):
        if isinstance(novos_atributos, dict):
            self.__atributos.update(novos_atributos)
        else:
            return 'errou'

from atributo import Atributo
from atributoView import AtributoView

class AtributoController():
    def __init__(self):
        self.__tela_atributos = AtributoView()

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos: Atributo):
        self.__atributos = atributos

    def mostrar_atributos(self):
        dados = {
            "ataque": self.atributos["ataque"],
            "defesa": self.atributos["defesa"],
            "hp": self.atributos["hp"],
            "estamina": self.atributos["estamina"]
        }
        self.__tela_atributos.mostrar_atributo(dados)
    
    def alterar_atributo(self):
        match (self.__tela_atributos.selecionar_atributo()):
            case 1:
                opcao


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


from personagem import Personagem
from boss import Boss

class Batalha():
    def __init__(self, personagem, boss, batalha_final, finalizada=False, turno=0):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem
        else:
            return
        if isinstance(boss, Boss):
            self.__boss = boss
        else:
            return
        self.__batalha_final = batalha_final
        self.__finalizada = finalizada
        self.__turno = turno
        


    @property
    def personagem(self):
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    @property
    def boss(self):
        return self.__boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self.__boss = boss

    @property
    def batalha_final(self):
        return self.__batalha_final

    @batalha_final.setter
    def batalha_final(self, batalha_final):
        self.__batalha_final = batalha_final

    @property
    def finalizada(self):
        return self.__finalizada

    @finalizada.setter
    def finalizada(self, finalizada):
        self.__finalizada = finalizada

    @property
    def turno(self):
        return self.__turno

    @turno.setter
    def turno(self, turno):
        self.__turno = turno

from batalha import Batalha
from batalhaView import BatalhaView

class BatalhaController(Boss, Personagem):
    def __init__(self, batalha: Batalha):
        self.__batalha = batalha
        self.__tela = BatalhaView()

    def realizar_turno(self, acao_personagem):
        personagem = self.__batalha.personagem
        boss = self.__batalha.boss

        if acao_personagem == 1:
            personagem.atacar(boss)
            self.__tela.mostra_mensagem(f"{personagem.nome} atacou {boss.nome}!")
        elif acao_personagem == 2:
            personagem.defender()
            self.__tela.mostra_mensagem(f"{personagem.nome} se defendeu!")
        elif acao_personagem == 3:
            tipo_item = self.__tela.escolher_item()
            if tipo_item:
                personagem.usar_item(tipo_item)
        elif acao_personagem == 4:
            personagem.usar_habilidade(boss)
            self.__tela.mostra_mensagem(f"{personagem.nome} usou uma habilidade!")

        if not self.__batalha.finalizada:
            boss.realizar_acao(personagem)

        self.__batalha.turno += 1

    def verificar_vencedor(self):
        if self.__batalha.boss.atributos['hp'] <= 0:
            self.__batalha.finalizada = True
            return "vitória"
        elif self.__batalha.personagem.atributos['hp'].valor <= 0:
            self.__batalha.finalizada = True
            return "derrota"
        return

    def iniciar_batalha(self):
        while not self.__batalha.finalizada:
            acao_personagem = self.__view.tela_opcoes()
            self.realizar_turno(acao_personagem)

            resultado = self.verificar_vencedor()
            if resultado == "vitória":
                self.__view.mostra_resultado("Você venceu!")
            elif resultado == "derrota":
                self.__view.mostra_resultado("Você foi derrotado!")

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
    
    def escolher_item(self):
        print("Escolha o item para usar:")
        print("1 - Poção de HP")
        print("2 - Poção de Estamina")
        escolha = int(input("Digite o número do item: "))
        if escolha == 1:
            return "HP"
        elif escolha == 2:
            return "Estamina"
        else:
            return
        
    def escolher_habilidade(self):
        #colocar a logica do personagem escolher a habilidade
        pass

    def mostra_resultado(self, mensagem):
        print(mensagem)

    def mostra_mensagem(self, msg):
        print(msg)

        from atributo import Atributo

class Boss:
    def __init__(self, nome, dificuldade, nivel_requerido, ataque, defesa, hp, estamina, diretor=False):
        super().__init__(ataque, defesa, hp, estamina)
        self.__nome = nome
        self.__dificuldade = dificuldade
        self.__nivel_requerido = nivel_requerido
        self.__diretor = diretor
        self.atributos = {
            'ataque': ataque,
            'defesa': defesa,
            'hp': hp,
            'estamina': estamina
        }


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def nivel_requerido(self):
        return self.__nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, nivel_requerido):
        self.__nivel_requerido = nivel_requerido

    @property
    def diretor(self):
        return self.__diretor

    @diretor.setter
    def diretor(self, diretor):
        self.__diretor = diretor

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos: Atributo):
        self.__atributos = atributos

        from boss import Boss
from bossView import BossView

class BossController:
    def __init__(self):
        self.__boss = None
        self.__boss_view = BossView()

    def cadastrar_boss(self):
        dados_boss = self.__boss_view.pega_dados_boss()
        boss = Boss(**dados_boss)
        self.__boss_view.mostra_mensagem(f"Boss {self.__boss.nome} cadastrado com sucesso!")

    def mostrar_atributos(self):
        if self.__boss:
            atributos = self.__boss.mostrar_atributos()
            self.__boss_view.mostra_atributos(atributos)
        else:
            self.__boss_view.mostra_mensagem("Nenhum boss cadastrado.")


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

        from atributo import Atributo

class ClassePersonagem(Atributo):
    def __init__(self, nome_classe, evolucao, ataque=0, defesa=0, hp=0, estamina=0):
        super().__init__(ataque, defesa, hp, estamina)
        self.__nome_classe = nome_classe
        self.__evolucao = evolucao
        self.__atributos = {
            'ataque': ataque,
            'defesa': defesa,
            'hp': hp,
            'estamina': estamina
        }


    @property
    def nome_classe(self):
        return self.__nome_classe

    @nome_classe.setter
    def nome_classe(self, nome_classe):
        self.__nome_classe = nome_classe

    @property
    def evolucao(self):
        return self.__evolucao

    @evolucao.setter
    def evolucao(self, evolucao):
        self.__evolucao = evolucao

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos: Atributo):
        self.__atributos = atributos

    def habilidades_clt(self, atributos):
        pass #Habilidades focadas em estabilidade no mercado e progressão estável."

    def habilidades_estagiario(self, nome_classe, atributos, evolucao):
        pass #Habilidades focadas em aprendizado rápido e flexibilidade."

    def habilidades_trainee(self, nome_classe, atributos, evolucao):
        pass #Habilidades focadas em crescimento acelerado e promoções rápidas."

    def incrementar_atributo(self, atributo, valor):
        if atributo in self.atributos:
            self.atributos[atributo] += valor
        else:
            return f"Atributo '{atributo}' não encontrado."
        
        from quiz import Quiz

class Curso(Quiz):
    def __init__(self, nome, nivel_requerido, xp_ganho, setor, dificuldade, realizado=False, acertos: Quiz=0):
        self._nome = nome
        self._nivel_requerido = nivel_requerido
        self._xp_ganho = xp_ganho
        self._setor = setor
        self._dificuldade = dificuldade
        self._realizado = realizado
        self._acertos = acertos


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nivel_requerido(self):
        return self._nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, nivel_requerido):
        self._nivel_requerido = nivel_requerido

    @property
    def xp_ganho(self):
        return self._xp_ganho

    @xp_ganho.setter
    def xp_ganho(self, xp_ganho):
        self._xp_ganho = xp_ganho

    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, setor):
        self._setor = setor

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self._dificuldade = dificuldade

    @property
    def realizado(self):
        return self._realizado

    @realizado.setter
    def realizado(self, realizado):
        self._realizado = realizado

    @property
    def acertos(self):
        return self._acertos

    @acertos.setter
    def acertos(self, acertos):
        self._acertos = acertos

    def realizar_quiz(self, gabarito):
        pass

    from setor import Setor

class Dungeon(Setor):
    def __init__(self, nome, nivel_requerido, xp_ganho, dificuldade, conquistada=False):
        self._nome = nome
        self._nivel_requerido = nivel_requerido
        self._xp_ganho = xp_ganho
        self._dificuldade = dificuldade
        self._conquistada = conquistada


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def nivel_requerido(self):
        return self._nivel_requerido

    @nivel_requerido.setter
    def nivel_requerido(self, nivel_requerido):
        self._nivel_requerido = nivel_requerido

    @property
    def xp_ganho(self):
        return self._xp_ganho

    @xp_ganho.setter
    def xp_ganho(self, xp_ganho):
        self._xp_ganho = xp_ganho

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self._dificuldade = dificuldade

    @property
    def conquistada(self):
        return self._conquistada

    @conquistada.setter
    def conquistada(self, conquistada):
        self._conquistada = conquistada

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

from personagem import Personagem
from dungeon import Dungeon
from curso import Curso


class Menu(Personagem, Dungeon, Curso):
    def __init__(self, personagem: Personagem, dungeon: Dungeon, curso: Curso):
        self.__personagem = personagem
        self.__dungeon = dungeon
        self.__curso = curso


    @property
    def personagem(self):
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    @property
    def dungeon(self):
        return self.__dungeon

    @dungeon.setter
    def dungeon(self, dungeon: Dungeon):
        if isinstance(dungeon, Dungeon):
            self.__dungeon = dungeon

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso: Curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    def listar_status(self):
        pass

    def listar_cursos(self):
        pass

    def listar_dungeons(self):
        pass

    from classePersonagem import ClassePersonagem
from pocao_hp import PocaoHP
from pocao_est import PocaoEstamina

class Personagem():
    def __init__(self, nome, nivel, experiencia, pocao_hp: PocaoHP, pocao_est: PocaoEstamina, classe_personagem: ClassePersonagem):
        self.__nome = nome
        self.__nivel = nivel
        self.__experiencia = experiencia
        if isinstance(pocao_hp, PocaoHP):
            self.__pocao_hp = pocao_hp
        if isinstance(pocao_est, PocaoEstamina):
            self.__pocao_est = pocao_est
        if isinstance(classe_personagem, ClassePersonagem):
            self.__classe_personagem = classe_personagem


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def nivel(self):
        return self.__nivel

    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel

    @property
    def experiencia(self):
        return self.__experiencia

    @experiencia.setter
    def experiencia(self, experiencia):
        self.__experiencia = experiencia

    @property
    def pocao_hp(self):
        return self.__pocao_hp

    @pocao_hp.setter
    def pocao_hp(self, pocao_hp):
        self.__pocao_hp = pocao_hp

    @property
    def pocao_est(self):
        return self.__pocao_est

    @pocao_est.setter
    def pocao_est(self, pocao_est):
        self.__pocao_est = pocao_est

    @property
    def classe_personagem(self):
        return self.__classe_personagem

    @classe_personagem.setter
    def classe_personagem(self, classe_personagem):
        self.__classe_personagem = classe_personagem

from personagemView import PersonagemView
from personagem import Personagem

class PersonagemController():
    def __init__(self):
        self.__personagens = []
        self.__personagemView = PersonagemView()


    def pega_personagem_por_nome(self, nome: str):
        for personagem in self.__personagens:
            if (personagem.nome == nome):
                return personagem
            return None

    def cadastrar_personagem(self):
        dados_personagem = self.__personagemView.pega_dados_personagem()
        personagem_existente = self.pega_personagem_por_nome(dados_personagem["nome"])
        if personagem_existente is None:
            classe = dados_personagem["classe"]
            personagem = Personagem(dados_personagem["nome"], dados_personagem["nivel"], dados_personagem["experiencia"], None, None, dados_personagem["classe"])
            self.__personagens.append(personagem)
            self.__personagemView.mostra_mensagem(f"Personagem {dados_personagem['nome']} cadastrado com sucesso!")
        else:
            self.__personagemView.mostra_mensagem(f"O personagem {dados_personagem['nome']} já existe!")

    def mostrar_status(self, personagem: Personagem):
        dados_personagem = {
            'nome': personagem.nome,
            'nivel': personagem.nivel,
            'experiencia': personagem.experiencia,
            'hp': personagem.classe_personagem.atributos['hp'],
            'estamina': personagem.classe_personagem.atributos['estamina']
        }
        self.__personagemView.mostrar_status(dados_personagem)

    def atacar(self, personagem: Personagem, boss: Boss):
        dano = self.classePersonagem.atributos['ataque'] - boss.atributos['defesa']
        dano = max(dano, 1)
        boss.atributos['hp'] -= dano
        self.__personagemView.mostra_mensagem(f"{personagem.nome} atacou {boss.nome} e causou {dano} de dano!")

    def defender(self):
        #colocar a logica que dobraria o atributo 'defender' durante 1 turno
        pass

    def usar_item(self, personagem: Personagem):
        tipo_item = self.__personagemView.escolher_item()
        if tipo_item == 1 and personagem.pocao_hp and personagem.pocao_hp.quant > 0:
            personagem.classe_personagem.atributos['hp'] += personagem.pocao_hp.valor
            personagem.pocao_hp.quant -= 1
            self.__personagemView.mostra_mensagem(f"{personagem.nome} usou Poção de HP!")
        elif tipo_item == 2 and personagem.pocao_est and personagem.pocao_est.quant > 0:
            personagem.classe_personagem.atributos['estamina'] += personagem.pocao_est.valor
            personagem.pocao_est.quant -= 1
            self.__personagemView.mostra_mensagem(f"{personagem.nome} usou Poção de Estamina!")
        else:
            self.__personagemView.mostra_mensagem(f"{self.nome} não tem Poção de {tipo_item} disponível!")

    def usar_habilidade(self, classe_personagem: Personagem, boss: Boss):
        #colocar a logica em que o jogador escolhe qual habilidade ele quer usar,
        #podendo escolher entre 3 habilidades, que tem efeitos diferentes no inimigo.
        pass

    
class PersonagemView():
    def mostrar_status(self, dados_personagem):
        print(f"Nome: {dados_personagem['nome']}")
        print(f"Nível: {dados_personagem['nivel']}")
        print(f"Experiência: {dados_personagem['experiencia']}")
        print(f"HP: {dados_personagem['hp']}")
        print(f"Estamina: {dados_personagem['estamina']}")

    def pega_dados_personagem(self):
        print("----------CADASTRO PERSONAGEM---------")
        nome = input("Nome: ")
        if not isinstance(nome, str):
            raise Exception("Nome inválido")

        print("-------- CLASSES ----------")
        print("Escolha uma classe:")
        print("1 - CLT (Bom no early game)")
        print("2 - Estagiário (Médio no early, bom no late)")
        print("3 - Trainee (Fraco no early, muito forte no late)")

        opcao = int(input("Digite o número da classe: "))
        classe = "CLT" if opcao == 1 else "Estagiário" if opcao == 2 else "Trainee" if opcao == 3 else None
        if not classe:
            raise Exception("Classe não encontrada")

        return {"nome": nome, "classe": classe, "nivel": 1, "experiencia": 0}
    
    def escolher_item(self):
        print("Escolha o item para usar:")
        print("1 - Poção de HP")
        print("2 - Poção de Estamina")
        return int(input("Digite o número do item: "))

    def escolher_habilidade(self):
        print("Escolha a habilidade:")
        print("1 - hab1")
        print("2 - hab2")
        print("3 - hab3")
        #Colocar logica para que as habilidades mostradas sejam somente aquelas que a classe tem, tipo, trainee só tem
        # a primeira habilidade, enquanto o estagiario tem a primeira e a segunda, e o CLT tem a primeira, segunda e a terceira.
        return int(input("Digite o número da habilidade: "))

    def mostra_mensagem(self, msg):
        print(msg)

        class Pocao:
    def __init__(self, nome, valor):
        self._nome = nome
        self._valor = valor


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

        from pocao  import Pocao

class PocaoEstamina(Pocao):
    def __init__(self, quant):
        super().__init__("Poção de Estamina", 5)
        self._quant = quant


    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, quant):
        self._quant = quant

        from pocao  import Pocao

class PocaoHP(Pocao):
    def __init__(self, quant):
        super().__init__("Poção de HP", 10)
        self._quant = quant


    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, quant):
        self._quant = quant

        class Quiz:
    def __init__(self, setor, pergunta, respostas, resposta_correta):
        self._setor = setor
        self._pergunta = pergunta
        self._respostas = respostas
        self._resposta_correta = resposta_correta
        self._selecionada = None
        self._gabaritou_miga = False


    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, setor):
        self._setor = setor

    @property
    def pergunta(self):
        return self._pergunta

    @pergunta.setter
    def pergunta(self, pergunta):
        self._pergunta = pergunta

    @property
    def respostas(self):
        return self._respostas

    @respostas.setter
    def respostas(self, respostas):
        self._respostas = respostas

    @property
    def resposta_correta(self):
        return self._resposta_correta

    @resposta_correta.setter
    def resposta_correta(self, resposta_correta):
        self._resposta_correta = resposta_correta

    @property
    def selecionada(self):
        return self._selecionada

    @selecionada.setter
    def selecionada(self, selecionada):
        self._selecionada = selecionada

    @property
    def gabaritou_miga(self):
        return self._gabaritou_miga

    @gabaritou_miga.setter
    def gabaritou_miga(self, gabaritou_miga):
        self._gabaritou_miga = gabaritou_miga

    def responder(self, resposta_selecionada):
        pass

    from personagem import Personagem

class Ranking(Personagem):
    def __init__(self, tipo, id, personagem:Personagem):
        self.__tipo = tipo
        self.__id = id
        self.__personagens = list[personagem] ## sabemos que não é assim!


    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, tipo):
        self.__tipo = tipo

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def personagens(self):
        return self.__personagens

    @personagens.setter
    def personagens(self, personagens):
        self.__personagens = personagens

    def adicionar_personagem(self, personagem):
        self.__personagens.append(personagem)

    def remover_personagem(self, personagem):
        self.__personagens.remove(personagem)

    def ranking_nivel(self):
        pass

    def ranking_dungeons(self):
        pass

    def ranking_cursos(self):
        pass

    class Setor:
    def __init__(self, nome, dificuldade):
        self._nome = nome
        self._dificuldade = dificuldade

    @property
    def nome(self):
        return self._nome
 
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def dificuldade(self):
        return self._dificuldade

    @dificuldade.setter
    def dificuldade(self, dificuldade):
        self._dificuldade = dificuldade

