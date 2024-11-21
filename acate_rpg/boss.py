from entidadejogavel import EntidadeJogavel
class Boss(EntidadeJogavel):
    def __init__(self, nome, dificuldade, nivel_requerido, ataque=0, defesa=0, hp=0, estamina=0):
        super().__init__(ataque, defesa, hp, estamina)
        self.__nome = nome
        self.__dificuldade = dificuldade
        self.__nivel_requerido = nivel_requerido
        self.__atributos = {
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
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos: EntidadeJogavel):
        self.__atributos = atributos

    
    def atacar(self, alvo):
        dano = self.__atributos["ataque"] * 1.5 - alvo.classe_personagem.defesa
        dano = max(dano, 1)
        return dano
    
    def defender(self):
        self.__atributos["defesa"] += 5

    def receber_dano(self, dano):
        self.__atributos["hp"] =- dano

        