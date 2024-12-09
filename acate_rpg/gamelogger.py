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

    @property
    def boss(self):
        return self.__boss
    
    @property
    def dungeon(self):
        return self.__dungeon
    
    @property
    def acao(self):
        return self.__acao
    
    @property
    def data(self):
        return self.__data
    
    