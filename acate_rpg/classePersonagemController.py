from classePersonagem import ClassePersonagem

class ClassePersonagemController():
    def __init__(self):
        self.modificadores_classe = {
            "Estagiario": {"ataque": 20, "defesa": 20, "hp": 30, "estamina": 10},
            "CLT": {"ataque": 40, "defesa": 40, "hp": 100, "estamina": 40}
        }

    def criar_classe(self, nome_classe: str) -> ClassePersonagem:
        try:
            # Verificar se o nome da classe é válido
            if nome_classe not in ["Trainee", "Estagiario", "CLT"]:
                raise ValueError(f"Classe '{nome_classe}' não é válida.")

            # Criar e retornar o objeto ClassePersonagem
            return ClassePersonagem(nome_classe=nome_classe)

        except ValueError as e:
            raise ValueError(f"Erro ao criar classe: {e}")

    def definir_atributos_iniciais(self, classe_personagem: ClassePersonagem):
        modificador = self.modificadores_classe.get(classe_personagem.nome_classe)

        if modificador:
            atributos = classe_personagem.atributos
            try:
                atributos['ataque'] += modificador['ataque']
                atributos['defesa'] += modificador['defesa']
                atributos['hp'] += modificador['hp']
                atributos['estamina'] += modificador['estamina']
                classe_personagem.atributos = atributos

            except KeyError as e:
                raise ValueError(f"Atributo inválido ao definir atributos iniciais: {e}")
        else:
            raise ValueError(f"Classe {classe_personagem.nome_classe} não tem modificador definido.")
        

    def atacar(self, personagem: ClassePersonagem, alvo):
        dano = personagem.classe_personagem.atacar(alvo)
        return dano
    
    def defender(self, personagem: ClassePersonagem):
        personagem.classe_personagem.defender()

    def receber_dano(self, personagem: ClassePersonagem, dano):
        personagem.classe_personagem.receber_dano(dano)
