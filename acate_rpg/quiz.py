class Quiz:
    def __init__(self, setor, dificuldade):
        self.__setor = setor
        self.__dificuldade = dificuldade
        self.__gabaritou_miga = False


    @property
    def setor(self):
        return self.__setor

    @setor.setter
    def setor(self, setor):
        self.__setor = setor

    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @property
    def dificuldade(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def gabaritou_miga(self):
        return self.__gabaritou_miga

    @gabaritou_miga.setter
    def gabaritou_miga(self, gabaritou_miga):
        self.__gabaritou_miga = gabaritou_miga


    