from personagem import Personagem
from boss import Boss

class Batalha(Personagem, Boss):
    def __init__(self, personagem, boss, turno=0, perdedor, vitoria=False, batalha_final=False):
        if isinstance(personagem, Personagem):
            self._personagem = personagem
        else:
            return
        if isinstance(boss, Boss):
            self._boss = boss
        else:
            return
        self._perdedor = perdedor
        self._turno = turno
        self._vitoria = vitoria
        self._batalha_final = batalha_final


    @property
    def personagem(self):
        return self._personagem

    @personagem.setter
    def personagem(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self._personagem = personagem

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, boss: Boss):
        if isinstance(boss, Boss):
            self._boss = boss

    @property
    def turno(self):
        return self._turno

    @turno.setter
    def turno(self, turno):
        self._turno = turno

    @property
    def perdedor(self):
        return self._perdedor

    @perdedor.setter
    def perdedor(self, perdedor):
        self._perdedor = perdedor

    @property
    def vitoria(self):
        return self._vitoria

    @vitoria.setter
    def vitoria(self, vitoria):
        self._vitoria = vitoria

    @property
    def batalha_final(self):
        return self._batalha_final

    @batalha_final.setter
    def batalha_final(self, batalha_final):
        self._batalha_final = batalha_final

    def iniciar(self):
        print(f"A batalha entre {self.personagem.nome} e {self.boss.nome} começou!")
        print(self.mostrar_status())

    def mostrar_status(self):
        return (f"{self.personagem.nome} - HP: {self.personagem.classe_personagem.atributos['hp']} - Estamina: {self.personagem.classe_personagem.atributos['estamina']} | "
                f"{self.boss.nome} - HP: {self.boss.atributos['hp']} - Estamina: {self.boss.atributos['estamina']}")

    def realizar_turno(self):
        print(f"Turno {self.turno}:")
        acao = input("Escolha uma ação (atacar, defender, usar item): ").strip().lower()
        
        def opcao(acao):
            match acao:
        
                case 'atacar':
                    self.atacar()
                case 'defender':
                    self.defender()
                case 'usar item':
                    self.usar_item()
                case 'usar habilidade':
                    sefl.usar_habilidade()
                case _:
                    print("Ação inválida. Tente novamente.")
                    self.realizar_turno()

        self.acao_boss()

        self.turno += 1

    def atacar(self):
        dano = self.personagem.classe_personagem.atributos['ataque'] - self.boss.atributos['defesa']
        dano = max(dano, 1)
        self.boss.atributos['hp'] -= dano
        print(f"{self.personagem.nome} atacou {self.boss.nome} e causou {dano} de dano!")

        if self.boss.atributos['hp'] <= 0:
            print(f"{self.boss.nome} foi derrotado!")
            self.finalizar()
    
    def defender(self):
        dano = self.boss.atributos['ataque'] - self.personagem.classe_personagem.atributos['defesa']
        dano = max(dano, 0)
        self.personagem.classe_personagem.atributos['hp'] -= dano
        print(f"{self.boss.nome} atacou {self.personagem.nome} e causou {dano} de dano!")

        if self.personagem.classe_personagem.atributos['hp'] <= 0:
            print(f"OOOhhh ma god, {self.personagem.nome} morreu! Tente novamente no proximo dia útil")
            self.finalizar(self.personagem.nome)

    def usar_item(self):
        #tem que ter relação com
        pass

    def acao_boss(self):
        #tem que ser aleatório, num sei como faz sem o famoso rand() e um switch-case
        pass

    def finalizar(self, perdedor):
        print("A batalha terminou.")
        if perdedor == self.personagem.nome:
            pass
        elif perdedor == self.boss.nome:
            pass
        