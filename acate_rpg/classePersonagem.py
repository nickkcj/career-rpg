from atributo import Atributo

class ClassePersonagem(Atributo):
    def __init__(self, nome_classe, evolucao, ataque=0, defesa=0, hp=0, estamina=0):
        super().__init__(ataque, defesa, hp, estamina)
        self.__nome_classe = nome_classe
        self.__evolucao = evolucao


    @property
    def nome_classe(self):
        return self.__nome_classe

    @nome_classe.setter
    def nome_classe(self, nome_classe):
        self.__nome_classe = nome_classe

    @property
    def evolucao(self):
        return self.__evolucao

    @evolucao.setter
    def evolucao(self, evolucao):
        self.__evolucao = evolucao

    @property
    def atributos(self):
        return self.__atributos

    @atributos.setter
    def atributos(self, atributos: Atributo):
        self.__atributos = atributos

    def habilidades_clt(self, atributos):
        pass #Habilidades focadas em estabilidade no mercado e progressão estável."

    def habilidades_estagiario(self, nome_classe, atributos, evolucao):
        pass #Habilidades focadas em aprendizado rápido e flexibilidade."

    def habilidades_trainee(self, nome_classe, atributos, evolucao):
        pass #Habilidades focadas em crescimento acelerado e promoções rápidas."

    def incrementar_atributo(self, atributo, valor):
        if atributo in self.atributos:
            self.atributos[atributo] += valor
        else:
            return f"Atributo '{atributo}' não encontrado."