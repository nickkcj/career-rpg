from datetime import datetime
class LogJogadas:
    def __init__(self, personagem, boss, dungeon, acao):
        self.__personagem = personagem
        self.__boss = boss
        self.__dungeon = dungeon 
        self.__acao = acao
        self.__data = datetime.now()
    
    @property
    def personagem(self):
        return self.__personagem
    
    @personagem.setter
    def personagem(self, personagem):
        self.__personagem = personagem


    @property
    def boss(self):
        return self.__boss
    
    @boss.setter
    def boss(self, boss):
        self.__boss = boss
    
    @property
    def dungeon(self):
        return self.__dungeon
    
    @dungeon.setter
    def dungeon(self, dungeon):
        self.__dungeon = dungeon
    
    @property
    def acao(self):
        return self.__acao
    
    @acao.setter
    def acao(self, acao):
        self.__acao = acao
    
    @property
    def data(self):
        return self.__data
    
    