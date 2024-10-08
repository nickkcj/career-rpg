from batalha import Batalha
from batalhaView import BatalhaView

class BatalhaController(Boss, Personagem):
    def __init__(self, batalha: Batalha):
        self.__batalha = batalha
        self.__tela = BatalhaView()

    def realizar_turno(self, acao_personagem):
        personagem = self.__batalha.personagem
        boss = self.__batalha.boss

        if acao_personagem == 1:
            personagem.atacar(boss)
            self.__tela.mostra_mensagem(f"{personagem.nome} atacou {boss.nome}!")
        elif acao_personagem == 2:
            personagem.defender()
            self.__tela.mostra_mensagem(f"{personagem.nome} se defendeu!")
        elif acao_personagem == 3:
            tipo_item = self.__tela.escolher_item()
            if tipo_item:
                personagem.usar_item(tipo_item)
        elif acao_personagem == 4:
            personagem.usar_habilidade(boss)
            self.__tela.mostra_mensagem(f"{personagem.nome} usou uma habilidade!")

        if not self.__batalha.finalizada:
            boss.realizar_acao(personagem)

        self.__batalha.turno += 1

    def verificar_vencedor(self):
        if self.__batalha.boss.atributos['hp'] <= 0:
            self.__batalha.finalizada = True
            return "vitória"
        elif self.__batalha.personagem.atributos['hp'].valor <= 0:
            self.__batalha.finalizada = True
            return "derrota"
        return

    def iniciar_batalha(self):
        while not self.__batalha.finalizada:
            acao_personagem = self.__view.tela_opcoes()
            self.realizar_turno(acao_personagem)

            resultado = self.verificar_vencedor()
            if resultado == "vitória":
                self.__view.mostra_resultado("Você venceu!")
            elif resultado == "derrota":
                self.__view.mostra_resultado("Você foi derrotado!")