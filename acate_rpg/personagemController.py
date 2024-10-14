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

    