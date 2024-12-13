from dao import DAO
from gamelogger import LogJogadas

#cada entidade terá uma classe dessa, implementação bem simples.
class GameloggerDAO(DAO):
    def __init__(self):
        super().__init__('registro.pkl')

    def add(self, registro: LogJogadas):
        if registro and isinstance(registro, LogJogadas):
            chave = f"{registro.personagem.nome}_{registro.data.timestamp()}"
            super().add(chave, registro)

    def update(self, registro: LogJogadas):
        if registro and isinstance(registro, LogJogadas):
            chave = f"{registro.personagem.nome}_{registro.data.timestamp()}"
            super().update(chave, registro)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
        
