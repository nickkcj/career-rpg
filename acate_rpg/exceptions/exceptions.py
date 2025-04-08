from abc import ABC

class BaseSistemaException(Exception, ABC):
    def __init__(self, mensagem, solucao="Tente novamente ou consulte o administrador do sistema"):
        super().__init__(mensagem)
        self.mensagem = mensagem
        self.solucao = solucao

    def __str__(self):
        return f"{self.mensagem} Solução: {self.solucao}"


class CadastroInvalidoException(Exception):
    def __init__(self, entidade, campo, solucao="Verifique os valores e tente novamente"):
        mensagem = f"Erro no cadastro de {entidade}: campo '{campo}' está inválido."
        super().__init__(mensagem, solucao)


class ItemIndisponivelException(Exception):
    def __init__(self, item, solucao="Verifique o inventário ou tente outro item"):
        mensagem = f"Item '{item}' não está disponível ou quantidade é insuficiente."
        super().__init__(mensagem, solucao)


class OperacaoNaoPermitidaException(Exception):
    def __init__(self, operacao, solucao="Verifique os pré-requisitos e tente novamente"):
        mensagem = f"A operação '{operacao}' não é permitida neste contexto."
        super().__init__(mensagem, solucao)


class CarregamentoDadosException(Exception):
    def __init__(self, arquivo, mensagem):
        self.arquivo = arquivo
        self.mensagem = mensagem
        super().__init__(f"Erro ao carregar dados do arquivo {arquivo}: {mensagem}")
        input("\nPressione Enter para voltar ao menu.")


class SalvamentoDadosException(Exception):
    def __init__(self, arquivo, solucao="Verifique o espaço em disco e as permissões"):
        mensagem = f"Erro ao salvar dados no arquivo '{arquivo}'."
        super().__init__(mensagem, solucao)
        input("\nPressione Enter para voltar ao menu.")


class XpGanhoInvalidoError(Exception):
    def __init__(self, solucao="O XP ganho deve ser um número inteiro."):
        super().__init__(solucao)


class NivelRequeridoInvalidoError(Exception):
    def __init__(self, solucao="O nível requerido deve ser um número entre 1 e 10."):
        super().__init__(solucao)


class SetorInvalidoError(Exception):
    def __init__(self, solucao="O setor deve ser RH, T.I, Vendas, Marketing ou Financeiro."):
        super().__init__(solucao)


class DificuldadeInvalidaError(Exception):
    def __init__(self, solucao="A dificuldade deve ser um número inteiro entre 1 e 10."):
        super().__init__(solucao)


class CriacaoBossException(Exception):
    def __init__(self, mensagem="Erro ao criar o boss"):
        super().__init__(mensagem, "Verifique as configurações e tente novamente")


class CriacaoSetorException(Exception):
    def __init__(self, mensagem="Erro ao criar o setor"):
        super().__init__(mensagem, "Verifique as configurações do setor e tente novamente")

class ValorInvalidoBossException(Exception):
    def __init__(self, atributo, solucao="O valor fornecido deve ser um número inteiro válido."):
        mensagem = f"Valor inválido para o atributo '{atributo}' do boss."
        super().__init__(mensagem, solucao)

class AtributoInexistenteBossException(Exception):
    def __init__(self, atributo, solucao="Verifique o atributo e tente novamente."):
        mensagem = f"Atributo '{atributo}' não existe no boss."
        super().__init__(mensagem, solucao)


class NumeroSetoresInvalidoError(Exception):
    def __init__(self, solucao="O número de setores deve ser entre 1 e 10."):
        super().__init__(solucao)

class SetorJahFeitoException(Exception):
    def __init__(self, solucao="O setor já foi conquistado, tente outro!"):
        super().__init__(solucao)

class CriacaoDungeonException(Exception):
    def __init__(self, solucao="Já existe uma dungeon com esse nome, tente outra!"):
        super().__init__(solucao)

class HpJahCheioException(Exception):
    def __init__(self, solucao="O Hp Atual já está no máximo!"):
        super().__init__(solucao)

