from abc import ABC

class BaseSistemaException(Exception, ABC):
    def __init__(self, mensagem, solucao="Tente novamente ou consulte o administrador do sistema"):
        super().__init__(mensagem)
        self.mensagem = mensagem
        self.solucao = solucao

    def __str__(self):
        return f"{self.mensagem} Solução: {self.solucao}"


class CadastroInvalidoException(BaseSistemaException):
    def __init__(self, entidade, campo, solucao="Verifique os valores e tente novamente"):
        mensagem = f"Erro no cadastro de {entidade}: campo '{campo}' está inválido."
        super().__init__(mensagem, solucao)


class ItemIndisponivelException(BaseSistemaException):
    def __init__(self, item, solucao="Verifique o inventário ou tente outro item"):
        mensagem = f"Item '{item}' não está disponível ou quantidade é insuficiente."
        super().__init__(mensagem, solucao)


class OperacaoNaoPermitidaException(BaseSistemaException):
    def __init__(self, operacao, solucao="Verifique os pré-requisitos e tente novamente"):
        mensagem = f"A operação '{operacao}' não é permitida neste contexto."
        super().__init__(mensagem, solucao)


class CarregamentoDadosException(BaseSistemaException):
    def __init__(self, arquivo, solucao="Verifique o arquivo e tente novamente"):
        mensagem = f"Erro ao carregar dados do arquivo '{arquivo}'."
        super().__init__(mensagem, solucao)


class SalvamentoDadosException(BaseSistemaException):
    def __init__(self, arquivo, solucao="Verifique o espaço em disco e as permissões"):
        mensagem = f"Erro ao salvar dados no arquivo '{arquivo}'."
        super().__init__(mensagem, solucao)