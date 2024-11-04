import time
from personagemView import PersonagemView
from personagem import Personagem
from classePersonagem import ClassePersonagem
from exceptions import CadastroInvalidoException, ItemIndisponivelException, OperacaoNaoPermitidaException


class PersonagemController:
    def __init__(self):
        self.__personagens = []
        self.__personagemView = PersonagemView()
        self.__habilidades_por_classe = {
            "Trainee": [
                {"nome": "Hora Extra", "efeito": "Aumenta a Estamina temporariamente", "tipo": "buff"},
                {"nome": "Desmotivar Inimigo", "efeito": "Reduz o Ataque do boss", "tipo": "debuff"}
            ],
            "Estagiario": [
                {"nome": "Cagada Remunerada", "efeito": "Aumenta o HP do personagem", "tipo": "buff"},
                {"nome": "Desestabilizar Boss", "efeito": "Reduz a Defesa do boss", "tipo": "debuff"}
            ],
            "CLT": [
                {"nome": "Festa da Firma", "efeito": "Aumenta o Ataque do personagem", "tipo": "buff"},
                {"nome": "Ataque Corporativo", "efeito": "Dano direto ao HP do boss", "tipo": "dano"}
            ]
        }

        self.__niveis_para_evolucao = {
            "Trainee": 20,
            "Estagiario": 50
        }

    @property
    def personagens(self):
        return self.__personagens

    @property
    def habilidades_por_classe(self):
        return self.__habilidades_por_classe

    @property
    def niveis_para_evolucao(self):
        return self.__niveis_para_evolucao

    def pega_personagem_por_nome(self, nome: str):
        for personagem in self.__personagens:
            if personagem.nome == nome:
                return personagem
        return None
    
    def criar_personagem(self, nome, nivel=1, experiencia_total=0, pontos_disponiveis=0, nome_classe=None, dungeons_conquistadas=None, bosses_derrotados=None, cursos_conquistados=0):
        if dungeons_conquistadas is None:
            dungeons_conquistadas = []
        if bosses_derrotados is None:
            bosses_derrotados = []

        # Verifica se o personagem já existe pelo nome
        if any(p.nome == nome for p in self.personagens):
            raise ValueError(f"Um personagem com o nome '{nome}' já existe.")

        # Lógica para criar o novo personagem
        personagem = Personagem(
            nome=nome,
            nivel=nivel,
            experiencia_total=experiencia_total,
            pontos_disponiveis=pontos_disponiveis,
            nome_classe=nome_classe,
            dungeons_conquistadas=dungeons_conquistadas,
            bosses_derrotados=bosses_derrotados,
            cursos_conquistados=cursos_conquistados
        )
        return personagem

    def mostrar_habilidades(self, personagem: Personagem):
        habilidades_por_classe = {}

        for classe in personagem.classes_historico:
            habilidades_classe = [habilidade for habilidade in self.__habilidades_por_classe.get(classe, [])]
            habilidades_por_classe[classe] = habilidades_classe

        self.__personagemView.mostrar_habilidades(habilidades_por_classe)

    def calcular_nivel(self, experiencia_total):
        nivel = 1
        experiencia_para_proximo = 100

        while experiencia_total >= experiencia_para_proximo:
            nivel += 1
            experiencia_total -= experiencia_para_proximo
            experiencia_para_proximo = 100 + (nivel * 10)

        return nivel
    
    def incrementar_curso(self, personagem: Personagem):
        personagem.cursos_conquistados += 1

    def experiencia_para_proximo_nivel(self, personagem: Personagem):
        nivel_atual = self.calcular_nivel(personagem.experiencia_total)
        return 100 + (nivel_atual * 10)

    def ganhar_experiencia(self, personagem: Personagem, experiencia_ganha: int):
        nivel_anterior = self.calcular_nivel(personagem.experiencia_total)
        personagem.experiencia_total += experiencia_ganha
        novo_nivel = self.calcular_nivel(personagem.experiencia_total)

        if novo_nivel > nivel_anterior:
            aumento_niveis = novo_nivel - nivel_anterior
            personagem.pontos_disponiveis += aumento_niveis * 5
            personagem.hp_atual = personagem.classe_personagem.atributos['hp']
            personagem.nivel = novo_nivel

            self.__personagemView.mostrar_mensagem(
                f"{personagem.nome} upou para o nível {novo_nivel}! Pontos disponíveis: {personagem.pontos_disponiveis}"
            )
            time.sleep(1)
            self.evoluir_classe(personagem)

        self.__personagemView.mostrar_mensagem(
            f"{personagem.nome} ganhou {experiencia_ganha} XP! Experiência total: {personagem.experiencia_total}"
        )
        time.sleep(1)

        self.__personagemView.mostrar_mensagem(
            f"XP para próximo nível: {self.experiencia_para_proximo_nivel(personagem)}"
        )
        time.sleep(1)

    def evoluir_classe(self, personagem: Personagem):
        ordem_classes = ["Trainee", "Estagiario", "CLT"]
        classe_atual = personagem.classe_personagem.nome_classe
        indice_atual = ordem_classes.index(classe_atual)

        if indice_atual < len(ordem_classes) - 1:
            nova_classe = ordem_classes[indice_atual + 1]
            nivel_necessario = self.niveis_para_evolucao.get(classe_atual, None)
            
            if personagem.nivel >= nivel_necessario:
                personagem.classe_personagem.nome_classe=nova_classe
                personagem.classe_personagem.evolucao += 1
                personagem.classe_personagem.atributos['ataque'] += 5
                personagem.classe_personagem.atributos['defesa'] += 5
                personagem.classe_personagem.atributos['hp'] += 25
                personagem.classe_personagem.atributos['estamina'] += 15
                
                novas_habilidades = self.__habilidades_por_classe[nova_classe]
                personagem.habilidades.extend(novas_habilidades)
                personagem.classes_historico.append(nova_classe)

                self.__personagemView.mostrar_mensagem(f"{personagem.nome} evoluiu para {nova_classe}!")
                time.sleep(1)
                self.__personagemView.mostrar_mensagem(f"Novas habilidades adquiridas por {nova_classe}:")

                for habilidade in novas_habilidades:
                    self.__personagemView.mostrar_mensagem(f" - {habilidade['nome']}: {habilidade['efeito']}")
                    time.sleep(1)
            else:
                self.__personagemView.mostrar_mensagem(
                    f"{personagem.nome} precisa estar no nível {nivel_necessario} para evoluir para {nova_classe}."
                )
                time.sleep(1)
        else:
            self.__personagemView.mostrar_mensagem(f"{personagem.nome} já é CLT e não pode evoluir.")
            time.sleep(1)

    def mostrar_status(self, personagem: Personagem):
        try:
            status = {
                'nome': personagem.nome,
                'classe': personagem.classe_personagem.nome_classe,
                'nivel': personagem.nivel,
                'experiencia_total': personagem.experiencia_total,
                'experiencia_para_proximo_nivel': self.experiencia_para_proximo_nivel(personagem),
                'pontos_disponiveis': personagem.pontos_disponiveis,
                'ataque': personagem.classe_personagem.atributos['ataque'],
                'defesa': personagem.classe_personagem.atributos['defesa'],
                'hp': personagem.classe_personagem.atributos['hp'],
                'hp_atual': personagem.hp_atual,
                'estamina': personagem.classe_personagem.atributos['estamina'],
                'pocoes_hp': personagem.pocao_hp.quant,
                'pocoes_est': personagem.pocao_est.quant,
                'cursos_conquistados': personagem.cursos_conquistados,
                'dungeons_conquistadas': [{'nome': d.get('nome')} if isinstance(d, dict) else {'nome': d.nome} for d in personagem.dungeons_conquistadas],
                'bosses_derrotados': [{'nome': b.get('nome')} if isinstance(b, dict) else {'nome': b.nome} for b in personagem.bosses_derrotados]
            }
            self.__personagemView.mostrar_status(status)
        except KeyError as e:
            raise OperacaoNaoPermitidaException(operacao="Mostrar status") from e

    def upar_atributos(self, personagem: Personagem):
        try:
            if personagem.pontos_disponiveis > 0:
                atributo_escolhido = self.__personagemView.escolher_atributo()
                pontos = self.__personagemView.pega_quantidade_pontos()
                if pontos <= personagem.pontos_disponiveis:
                    if atributo_escolhido in personagem.classe_personagem.atributos:
                        personagem.classe_personagem.atributos[atributo_escolhido] += pontos
                        personagem.pontos_disponiveis -= pontos
                        self.__personagemView.mostrar_mensagem(f"Atributo {atributo_escolhido} aumentado em {pontos} pontos!")
                    else:
                        raise CadastroInvalidoException(entidade="Personagem", campo=atributo_escolhido)
                else:
                    raise OperacaoNaoPermitidaException(operacao="Distribuir pontos de atributos")
            else:
                self.__personagemView.mostrar_mensagem("Você não tem pontos disponíveis para distribuir.")
        except CadastroInvalidoException as e:
            self.__personagemView.mostrar_mensagem(str(e))

    def usar_item(self, personagem: Personagem):
        try:
            tipo_item = self.__personagemView.escolher_item(personagem)
            if tipo_item == 1 and personagem.pocao_hp and personagem.pocao_hp.quant > 0:
                personagem.hp_atual += personagem.pocao_hp.valor
                personagem.pocao_hp.quant -= 1
                self.hp_atual = self.hp_atual
                self.__personagemView.mostrar_mensagem(f"{personagem.nome} usou Poção de HP!")
            elif tipo_item == 2 and personagem.pocao_est and personagem.pocao_est.quant > 0:
                personagem.classe_personagem.atributos['estamina'] += personagem.pocao_est.valor
                personagem.pocao_est.quant -= 1
                self.__personagemView.mostrar_mensagem(f"{personagem.nome} usou Poção de Estamina!")
            else:
                raise ItemIndisponivelException(item="Poção")
        except ItemIndisponivelException as e:
            self.__personagemView.mostrar_mensagem(str(e))

    def usar_itens_batalha(self, personagem):
        self.__personagemView.mostrar_mensagem(f"---Inventário---: Poção HP (quantidade: {personagem.pocao_hp.quant}), Poção Estamina (quantidade: {personagem.pocao_est.quant}")
        print("1 - Usar poção HP")
        print("2 - Usar poção Estamina")
        opcao = input("Digite o item que você quer usar: ")
        return opcao

    