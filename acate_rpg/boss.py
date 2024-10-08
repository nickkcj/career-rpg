import random

class Boss:
    def __init__(self, nome, dificuldade, nivel_requerido, ataque=0, defesa=0, hp=0, estamina=0, diretor=False):
        super().__init__(ataque, defesa, hp, estamina)
        self.__nome = nome
        self.__dificuldade = dificuldade
        self.__nivel_requerido = nivel_requerido
        self.__diretor = False


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

    def mostrar_atributos(self):
        return f"Ataque: {self.atributos['ataque']}, Defesa: {self.atributos['defesa']}, HP: {self.atributos['hp']}, Estamina: {self.atributos['estamina']}"
    
    def realizar_acao(self, personagem):
        acao = random.choice(['atacar', 'defender', 'usar_habilidade'])
        if acao == 'atacar':
            self.atacar()
        elif acao == 'defender':
            self.defender()
        elif acao == 'usar_habilidade':
            self.usar_habilidade()

    def atacar(self, personagem):
        dano = self.atributos['ataque'] - personagem.classe_personagem.atributos['defesa']
        dano = max(dano, 1)
        personagem.classe_personagem.atributos['hp'] -= dano
        print(f"{self.nome} atacou {personagem.nome} e causou {dano} de dano!")

    def defender(self):
        #logica para aumentar a defesa em somente um turno
        print(f"{self.nome} se defendeu, aumentando sua defesa temporariamente.")
        pass

    def usar_habilidade(self, personagem):
        #habilidade do boss
        print(f"{self.nome} usou uma habilidade especial em {personagem.nome}!")
        pass