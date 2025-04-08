from entidadejogavel import EntidadeJogavel

class ClassePersonagem(EntidadeJogavel):
    def __init__(self, nome_classe, evolucao=0, ataque=1, defesa=1, hp=100, estamina=20):
        super().__init__(ataque, defesa, hp, estamina)
        self.__nome_classe = nome_classe
        self.__evolucao = evolucao


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


    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa * 2
        dano = max(dano, 1)
        return round(dano)
    
    def defender(self):
        self.defesa += 5




        