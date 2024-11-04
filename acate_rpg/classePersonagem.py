from atributo import Atributo

class ClassePersonagem(Atributo):
    def __init__(self, nome_classe, evolucao=0, ataque=1, defesa=1, hp=100, estamina=20):
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



        