class Atributo:
    def __init__(self, ataque=0, defesa=0, hp=0, estamina=0):
        self.__atributos = {
            'ataque': ataque,
            'defesa': defesa,
            'hp': hp,
            'estamina': estamina
        }

    @property
    def atributos(self):
        return self._atributos

    @atributos.setter
    def atributos(self, novos_atributos):
        if isinstance(novos_atributos, dict):
            self.__atributos.update(novos_atributos)
        else:
            return 'errou'
