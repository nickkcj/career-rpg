from atributo import Atributo

class ClassePersonagem(Atributo):
    def __init__(self, nome_classe, evolucao, ataque=0, defesa=0, hp=0, estamina=0):
        super().__init__(ataque, defesa, hp, estamina)
        self._nome_classe = nome_classe
        self._evolucao = evolucao


    @property
    def nome_classe(self):
        return self._nome_classe

    @nome_classe.setter
    def nome_classe(self, nome_classe):
        self._nome_classe = nome_classe

    @property
    def evolucao(self):
        return self._evolucao

    @evolucao.setter
    def evolucao(self, evolucao):
        self._evolucao = evolucao

    @property
    def atributos(self):
        return self._atributos

    @atributos.setter
    def atributos(self, atributos: Atributo):
        self._atributos = atributos

    def habilidades_clt(self, atributos):
        return "Habilidades focadas em estabilidade no mercado e progressão estável."

    def habilidades_estagiario(self, nome_classe, atributos, evolucao):
        return "Habilidades focadas em aprendizado rápido e flexibilidade."

    def habilidades_trainee(self, nome_classe, atributos, evolucao):
        return "Habilidades focadas em crescimento acelerado e promoções rápidas."

    def incrementar_atributo(self, atributo, valor):
        if atributo in self.atributos:
            self.atributos[atributo] += valor
        else:
            raise ValueError(f"Atributo '{atributo}' não encontrado.")