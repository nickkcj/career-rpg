
from gamelogger import LogJogadas
from gameloggerView import LogView
from gameloggerDAO import GameloggerDAO


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
        registros = [
            registro for registro in self.__registros
            if registro.personagem.nome == nome_personagem
        ]
        if not registros:
            self.__logView.mostrar_mensagem("Nenhum registro disponível para este personagem!")
            return
        self.__logView.listar_registros(registros)

    def excluir_registro(self):
        registro_selecionado = self.__logView.excluir_registro(self.__registros)
        if registro_selecionado is not None:
            self.__registro_dao.remove(registro_selecionado)
            self.__registros = list(self.__registro_dao.get_all())

    def alterar_registro(self):
        dados, index = self.__logView.alterar_registro(self.__registros)
        if dados is not None:
            novo_registro = LogJogadas(
                dados["personagem"], dados["boss"], dados["dungeon"], dados["movimento"]
            )

            # Atualizar apenas se o novo personagem existe
            if any(registro.personagem == dados["personagem"] for registro in self.__registros):
                self.__registros[index] = novo_registro
                self.__registro_dao.update(novo_registro)
                self.__registros = list(self.__registro_dao.get_all())
            else:
                self.__logView.mostrar_mensagem(
                    f"Personagem {dados['personagem']} não encontrado! Registro será removido."
                )
                del self.__registros[index]
                self.__registro_dao.remove(self.__registros[index].personagem)
            
        
