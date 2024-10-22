from setorView import SetorView
from setor import Setor

class SetorController():
    def __init__(self):
        self.__setorView = SetorView()


    
    def adicionar_setor(self):
        dados_setor = self.__setorView.pega_dados_setor()
        setor = Setor(dados_setor["nome"], dados_setor["dificuldade"])
        return setor
    


    def calcular_media_dificuldades(self):
        dificuldade = 0
        dificuldade += [setor["dificuldade"] for setor in self.setores.values()]
