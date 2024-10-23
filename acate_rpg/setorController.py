from setorView import SetorView
from setor import Setor

class SetorController():
    def __init__(self):
        self.__setorView = SetorView()


    
    from setorView import SetorView
from setor import Setor

class SetorController:
    def __init__(self):
        self.__setorView = SetorView()

    def adicionar_setor(self, numero):
        setores_validos = ["RH", "T.I", "Vendas", "Financeiro", "Marketing"]
        setor = None

        while not setor:
            try:
                
                dados_setor = self.__setorView.pega_dados_setor(numero)
                
                
                if dados_setor["nome"] not in setores_validos:
                    
                    mensagem = f"Setor inválido: {dados_setor['nome']}. Escolha entre {', '.join(setores_validos)}."
                    raise ValueError(mensagem)
                
                
                setor = Setor(dados_setor["nome"], dados_setor["dificuldade"])

            except ValueError as e:
                
                print("******************************************")
                print(f"{e}")
                print("******************************************")

        return setor

    


    def calcular_media_dificuldades(self, setores):
        dificuldade = 0
        dificuldade = sum(int(setor.dificuldade) for setor in setores)
        return dificuldade/ len(setores)
