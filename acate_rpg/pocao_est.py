from pocao  import Pocao

class PocaoEstamina(Pocao):
    def __init__(self, quant):
        super().__init__("Poção de Estamina", 5)
        self.__quant = quant


    @property
    def quant(self):
        return self.__quant

    @quant.setter
    def quant(self, quant):
        self.__quant = quant

        