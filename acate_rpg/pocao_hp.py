from pocao  import Pocao

class PocaoHP(Pocao):
    def __init__(self, quant):
        super().__init__("Poção de HP", 10)
        self._quant = quant


    @property
    def quant(self):
        return self._quant

    @quant.setter
    def quant(self, quant):
        self._quant = quant