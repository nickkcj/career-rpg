
from gamelogger import LogJogadas
from gameloggerView import LogView


class LogController():
    def __init__(self):
          self.__registros = []
          self.__logView = LogView()

    @property
    def registros(self):
        return self.__registros
         
    def adicionar_registro(self, personagem, boss, dungeon, acao):
        registro = LogJogadas(personagem, boss, dungeon, acao)
        self.__registros.append(registro)
    
    def listar_registros(self):
        self.__logView.listar_registros(self.__registros)
        
    def excluir_registro(self):
        self.__logView.excluir_registro(self.__registros)

    def alterar_registro(self):
        dados, index = self.__logView.alterar_registro(self.__registros)  
        novo_registro = LogJogadas(dados["personagem"], dados["boss"], dados["dungeon"], dados["movimento"])
        self.__registros[index] = novo_registro
            
        
