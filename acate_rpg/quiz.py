class Quiz:
    def __init__(self, setor, dificuldade):
        self._setor = setor
        self._dificuldade = dificuldade
        self._gabaritou_miga = False


    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, setor):
        self._setor = setor

    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @property
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def gabaritou_miga(self):
        return self._gabaritou_miga

    @gabaritou_miga.setter
    def gabaritou_miga(self, gabaritou_miga):
        self._gabaritou_miga = gabaritou_miga


    