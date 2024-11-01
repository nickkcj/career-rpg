class Setor:
    def __init__(self, nome, dificuldade, boss):
        self.__nome = nome
        self.__dificuldade = dificuldade
        self.__boss = boss

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
    def boss(self):
        return self.__boss
    
    @boss.setter
    def boss(self, boss):
        self.__boss = boss
