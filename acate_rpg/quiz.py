class Quiz:
    def __init__(self, setor, pergunta, respostas, resposta_correta):
        self._setor = setor
        self._pergunta = pergunta
        self._respostas = respostas
        self._resposta_correta = resposta_correta
        self._selecionada = None
        self._gabaritou_miga = False


    @property
    def setor(self):
        return self._setor

    @setor.setter
    def setor(self, setor):
        self._setor = setor

    @property
    def pergunta(self):
        return self._pergunta

    @pergunta.setter
    def pergunta(self, pergunta):
        self._pergunta = pergunta

    @property
    def respostas(self):
        return self._respostas

    @respostas.setter
    def respostas(self, respostas):
        self._respostas = respostas

    @property
    def resposta_correta(self):
        return self._resposta_correta

    @resposta_correta.setter
    def resposta_correta(self, resposta_correta):
        self._resposta_correta = resposta_correta

    @property
    def selecionada(self):
        return self._selecionada

    @selecionada.setter
    def selecionada(self, selecionada):
        self._selecionada = selecionada

    @property
    def gabaritou_miga(self):
        return self._gabaritou_miga

    @gabaritou_miga.setter
    def gabaritou_miga(self, gabaritou_miga):
        self._gabaritou_miga = gabaritou_miga

    def responder(self, resposta_selecionada):
        pass