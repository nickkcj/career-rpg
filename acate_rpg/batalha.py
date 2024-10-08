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
        