from models.gamelogger import LogJogadas
from gameloggerView import LogView
from dao.gameloggerDAO import GameloggerDAO
import time

class LogController():
    def __init__(self):
        self.__registro_dao = GameloggerDAO()
        self.__registros = list(self.__registro_dao.get_all())
        self.__logView = LogView()

    @property
    def registros(self):
        return list(self.__registro_dao.get_all())
         
    def adicionar_registro(self, personagem, boss, dungeon, acao):
        registro = LogJogadas(personagem, boss, dungeon, acao)
        self.__registro_dao.add(registro)
        self.__registros = list(self.__registro_dao.get_all())
    
    def listar_registros(self, nome_personagem):
        self.__registros = list(self.__registro_dao.get_all())
        

        self.__registros.remove(self.__registros[0])
        registros_filtrados = [
            registro for registro in self.__registros
            if registro.personagem.nome == nome_personagem
        ]
        if not registros_filtrados:
            self.__logView.mostrar_mensagem("Nenhum registro disponível para este personagem!")
            return

        
        
        self.__logView.listar_registros({
            "registros": [
                {
                    "personagem": registro.personagem,
                    "boss": registro.boss if registro.boss else None,
                    "dungeon": registro.dungeon if registro.dungeon else None,
                    "acao": registro.acao,
                    "data": registro.data
                }
                for registro in registros_filtrados
            ]
        })


    def excluir_registro(self, nome):
        # Obter todos os registros
        self.__registros = list(self.__registro_dao.get_all())
        
        self.__registros.remove(self.__registros[0])
        
        registros_dict = {
            "registros": [
                {
                    "personagem": registro.personagem.nome,
                    "boss": registro.boss.nome if registro.boss else None,
                    "dungeon": registro.dungeon.nome if registro.dungeon else None,
                    "acao": registro.acao,
                    "data": registro.data
                    
                }
                for registro in self.__registros
                if registro.personagem.nome == nome
            ]
        }

        # Passa o dicionário para a View para selecionar o registro a excluir
        registro_selecionado = self.__logView.excluir_registro(registros_dict)
        
        
        if registro_selecionado is not None:
            nome_registro = registro_selecionado['personagem']
            data_registro = registro_selecionado['data'].timestamp()
            self.__registros = [registro for registro in self.__registros if registro.data.timestamp() == data_registro]
            
            chave = f"{nome_registro}_{data_registro}"
            
            self.__registro_dao.remove(chave)
            

            # Exibe uma mensagem de sucesso
            self.__logView.mostrar_mensagem(f"Registro do personagem {nome} excluído com sucesso!")




    def alterar_registro(self, nome):
        # Obter todos os registros
        self.__registros = list(self.__registro_dao.get_all())
        self.__registros.remove(self.__registros[0])
        
        registros_dict = {
            "registros": [
                {
                    "personagem": registro.personagem,
                    "boss": registro.boss if registro.boss else None,
                    "dungeon": registro.dungeon if registro.dungeon else None,
                    "acao": registro.acao,
                    "data": registro.data
                }
                for registro in self.__registros
                if registro.personagem.nome == nome
            ]
        }

        

        # Passa o dicionário para a View para selecionar o registro a alterar
        dados_alterados, index = self.__logView.alterar_registro(registros_dict)
        registros2 = [registro for registro in self.__registros if registro.personagem.nome == nome]
        registro_selecionado = registros2[index]
        nome_registro = registro_selecionado.personagem.nome
        
        if dados_alterados["personagem"]:
            registro_selecionado.personagem.nome = dados_alterados["personagem"]
        if dados_alterados["boss"]:
            registro_selecionado.boss.nome = dados_alterados["boss"]
        if dados_alterados["dungeon"]:
            registro_selecionado.dungeon.nome = dados_alterados["dungeon"]
        if dados_alterados["movimento"]:
            registro_selecionado.acao = dados_alterados["movimento"]

    
        
            chave = f"{nome_registro}_{dados_alterados['data'].timestamp()}"
            
            
            
            self.__registro_dao.update_key(chave, registro_selecionado)
            
            self.__registros = list(self.__registro_dao.get_all())
            self.__logView.mostrar_mensagem(f"Registro do personagem {dados_alterados['personagem']} alterado com sucesso!")
        else:
            self.__logView.mostrar_mensagem(f"Personagem {dados_alterados['personagem']} não encontrado!")

            
        
