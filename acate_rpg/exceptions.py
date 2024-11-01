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


class XpGanhoInvalidoError(CadastroInvalidoException):
    def __init__(self, solucao="O XP ganho deve ser um número inteiro."):
        super().__init__("Curso", "xp_ganho", solucao)


class NivelRequeridoInvalidoError(CadastroInvalidoException):
    def __init__(self, solucao="O nível requerido deve ser um número entre 1 e 10."):
        super().__init__("Curso", "nivel_requerido", solucao)


class SetorInvalidoError(CadastroInvalidoException):
    def __init__(self, solucao="O setor deve ser RH, T.I, Vendas, Marketing ou Financeiro."):
        super().__init__("Curso", "setor", solucao)


class DificuldadeInvalidaError(CadastroInvalidoException):
    def __init__(self, solucao="A dificuldade deve ser um número inteiro entre 1 e 10."):
        super().__init__("Curso", "dificuldade", solucao)


class CriacaoBossException(BaseSistemaException):
    def __init__(self, mensagem="Erro ao criar o boss"):
        super().__init__(mensagem, "Verifique as configurações e tente novamente")


class CriacaoSetorException(BaseSistemaException):
    def __init__(self, mensagem="Erro ao criar o setor"):
        super().__init__(mensagem, "Verifique as configurações do setor e tente novamente")
