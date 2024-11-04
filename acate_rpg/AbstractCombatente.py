from abc import ABC, abstractmethod

class Combatente(ABC):
    @abstractmethod
    def atacar(self, usuario, alvo):
        pass

    @abstractmethod
    def defender(self, usuario):
        pass