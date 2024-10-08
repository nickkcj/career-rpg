from atributo import Atributo
from atributoView import AtributoView

class AtributoController():
    def __init__(self):
        self.__tela_atributos = AtributoView()

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos: Atributo):
        self.__atributos = atributos

    def mostrar_atributos(self):
        dados = {
            "ataque": self.atributos["ataque"],
            "defesa": self.atributos["defesa"],
            "hp": self.atributos["hp"],
            "estamina": self.atributos["estamina"]
        }
        self.__tela_atributos.mostrar_atributo(dados)
    
    def alterar_atributo(self):
        match (self.__tela_atributos.selecionar_atributo()):
            case 1:
                opcao


