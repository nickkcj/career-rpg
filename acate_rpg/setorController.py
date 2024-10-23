from setorView import SetorView
from setor import Setor

class SetorController():
    def __init__(self):
        self.__setorView = SetorView()


    
    def adicionar_setor(self, numero):
        dados_setor = self.__setorView.pega_dados_setor(numero)
        setor = Setor(dados_setor["nome"], dados_setor["dificuldade"])
        return setor
    


    def calcular_media_dificuldades(self, setores):
        dificuldade = 0
        dificuldade = sum(int(setor.dificuldade) for setor in setores)
        return dificuldade/ len(setores)
