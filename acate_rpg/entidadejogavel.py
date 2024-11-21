from abc import ABC, abstractmethod

class EntidadeJogavel(ABC):
    def __init__(self, ataque=0, defesa=0, hp=0, estamina=0):
        self.__atributos = {
            'ataque': ataque,
            'defesa': defesa,
            'hp': hp,
            'estamina': estamina
        }

    
    @abstractmethod
    def atacar(self, alvo):
        pass

    @abstractmethod
    def receber_dano(self, dano):
        pass

    @abstractmethod
    def defender(self):
        pass



    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, novos_atributos):
        if isinstance(novos_atributos, dict):
            self.__atributos.update(novos_atributos)
        else:
            raise ValueError("Atributos devem ser passados em um dicionário.")
        
    @property
    def ataque(self):
        return self.__atributos['ataque']

    @ataque.setter
    def ataque(self, valor):
        self.__atributos['ataque'] = valor

    @property
    def defesa(self):
        return self.__atributos['defesa']

    @defesa.setter
    def defesa(self, valor):
        self.__atributos['defesa'] = valor

    @property
    def hp(self):
        return self.__atributos['hp']

    @hp.setter
    def hp(self, valor):
        self.__atributos['hp'] = valor

    @property
    def estamina(self):
        return self.__atributos['estamina']

    @estamina.setter
    def estamina(self, valor):
        self.__atributos['estamina'] = valor

