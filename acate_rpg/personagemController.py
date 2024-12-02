import time
from personagemView import PersonagemView
from personagem import Personagem
from classePersonagemController import ClassePersonagemController
from exceptions import CadastroInvalidoException, ItemIndisponivelException, OperacaoNaoPermitidaException, HpJahCheioException
from batalhaView import BatalhaView


class PersonagemController():
    def __init__(self):
        self.__personagens = []
        self.__personagemView = PersonagemView()
        self.__batalhaView = BatalhaView()
        self.__classeController = ClassePersonagemController()
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
    

    def usar_habilidade(self, personagem, boss):
        classe = personagem.classe_personagem.nome_classe
        opcao = self.__batalhaView.escolher_habilidade(classe)
        
        if personagem.classe_personagem.atributos['estamina'] >= 2:
            
            if classe == 'CLT' and opcao == '1':
                personagem.classe_personagem.atributos['ataque'] += 5
                personagem.classe_personagem.atributos['estamina'] -= 5
                mensagem = f"O personagem {personagem.nome} usou a habilidade *Festa da Firma* e aumentou seu ataque em 5 pontos!"

            elif classe == 'CLT' and opcao == '2':
                boss.atributos['hp'] = max(boss.atributos['hp'] - 10, 0)
                personagem.classe_personagem.atributos['estamina'] -= 5
                mensagem = f"O personagem {personagem.nome} usou a habilidade *Ataque Corporativo* e diminuiu o HP do boss em 10 pontos!"

            elif classe == 'Estagiario' and opcao == '1':
                personagem.hp_atual += 10
                personagem.classe_personagem.atributos['estamina'] -= 5
                mensagem = f"O personagem {personagem.nome} usou a habilidade *Cagada Remunerada* e aumentou seu HP em 10 pontos!"

            elif classe == 'Estagiario' and opcao == '2':
                boss.atributos['defesa'] = max(boss.atributos['defesa'] - 5, 1)
                personagem.classe_personagem.atributos['estamina'] -= 5
                mensagem = f"O personagem {personagem.nome} usou a habilidade *Desestabilizar Boss* e diminuiu a defesa do boss em 5 pontos!"

            elif classe == 'Trainee' and opcao == '1':
                personagem.classe_personagem.atributos['estamina'] += 15
                personagem.classe_personagem.atributos['estamina'] -= 5
                mensagem = f"O personagem {personagem.nome} usou a habilidade *Hora Extra* e aumentou sua estamina em 10 pontos!"

            elif classe == 'Trainee' and opcao == '2':
                boss.atributos['ataque'] = max(boss.atributos['ataque'] - 7.5, 1)
                personagem.classe_personagem.atributos['estamina'] -= 5
                mensagem = f"O personagem {personagem.nome} usou a habilidade *Desmotivar Inimigo* e reduziu o ataque do boss em 7.5 pontos!"

            else:
                raise OperacaoNaoPermitidaException("Opção inválida, tente novamente")

            self.__batalhaView.mostra_mensagem(mensagem)
            

        else:
            self.__batalhaView.mostra_mensagem("O personagem não possui estamina o suficiente para usar uma habilidade!")
              


    def pega_personagem_por_nome(self, nome: str):
        personagem = next((p for p in self.__personagens if p.nome == nome), None)
        if personagem is None:
            raise CadastroInvalidoException(f"Personagem '{nome}' não encontrado.")
        return personagem
    
    def criar_personagem(self, nome, nivel=1, experiencia_total=0, pontos_disponiveis=0, nome_classe=None, dungeons_conquistadas=None, bosses_derrotados=None, cursos_conquistados=0):
        try:
            if dungeons_conquistadas is None:
                dungeons_conquistadas = []
            if bosses_derrotados is None:
                bosses_derrotados = []

            if any(p.nome == nome for p in self.personagens):
                raise CadastroInvalidoException(f"Um personagem com o nome '{nome}' já existe.")

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
            personagem.classes_historico = [nome_classe]
            classe_inicial = personagem.classes_historico[0]
            if classe_inicial in ["Estagiario", "CLT"]:
                self.__classeController.definir_atributos_iniciais(personagem.classe_personagem)

            return personagem

        except AttributeError as e:
            raise OperacaoNaoPermitidaException("Erro ao criar personagem") from e

    def mostrar_habilidades(self, personagem: Personagem):
        try:
            habilidades_por_classe = {
                classe: [habilidade for habilidade in self.__habilidades_por_classe.get(classe, [])]
                for classe in personagem.classes_historico
            }
            self.__personagemView.mostrar_habilidades(habilidades_por_classe)
        except KeyError as e:
            raise OperacaoNaoPermitidaException("Erro ao mostrar habilidades") from e

    def calcular_nivel(self, experiencia_total):
        try:
            if experiencia_total < 0:
                raise ValueError("Experiência total não pode ser negativa.")
            
            nivel = 1
            experiencia_para_proximo = 100

            while experiencia_total >= experiencia_para_proximo:
                nivel += 1
                experiencia_total -= experiencia_para_proximo
                experiencia_para_proximo = 100 + (nivel * 10)

            return nivel

        except TypeError as e:
            raise TypeError("Experiência total deve ser um número.") from e
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro inesperado ao calcular nível: {e}")
    
    def incrementar_curso(self, personagem: Personagem):
        try:
            if not isinstance(personagem, Personagem):
                raise TypeError("Objeto fornecido não é uma instância de Personagem.")
            
            personagem.cursos_conquistados += 1

        except AttributeError as e:
            raise AttributeError("Atributo 'cursos_conquistados' não encontrado no objeto Personagem.") from e
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro inesperado ao incrementar curso: {e}")

    def experiencia_para_proximo_nivel(self, personagem: Personagem):
        try:
            if not isinstance(personagem, Personagem):
                raise TypeError("Objeto fornecido não é uma instância de Personagem.")
            
            nivel_atual = self.calcular_nivel(personagem.experiencia_total)
            return 100 + (nivel_atual * 10)

        except AttributeError as e:
            raise AttributeError("Atributo 'experiencia_total' não encontrado no objeto Personagem.") from e
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro inesperado ao calcular XP para o próximo nível: {e}")

    def ganhar_experiencia(self, personagem: Personagem, experiencia_ganha: int):
        try:
            if not isinstance(personagem, Personagem):
                raise TypeError("Objeto fornecido não é uma instância de Personagem.")
            if experiencia_ganha < 0:
                raise ValueError("Experiência ganha não pode ser negativa.")
            
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

        except AttributeError as e:
            raise AttributeError("Erro ao acessar atributos do objeto Personagem.") from e
        except ValueError as e:
            self.__personagemView.mostrar_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro inesperado ao ganhar experiência: {e}")

    def evoluir_classe(self, personagem: Personagem):
        try:
            ordem_classes = ["Trainee", "Estagiario", "CLT"]
            if not isinstance(personagem, Personagem):
                raise TypeError("Objeto fornecido não é uma instância de Personagem.")
            
            classe_atual = personagem.classe_personagem.nome_classe
            if classe_atual not in ordem_classes:
                raise ValueError(f"A classe '{classe_atual}' não é uma classe válida para evolução.")
            
            indice_atual = ordem_classes.index(classe_atual)

            if indice_atual < len(ordem_classes) - 1:
                nova_classe = ordem_classes[indice_atual + 1]
                nivel_necessario = self.niveis_para_evolucao.get(classe_atual, None)
                
                if nivel_necessario is None:
                    raise KeyError(f"Nível necessário para evolução da classe '{classe_atual}' não definido.")
                
                if personagem.nivel >= nivel_necessario:
                    personagem.classe_personagem.nome_classe = nova_classe
                    personagem.classe_personagem.evolucao += 1
                    personagem.classe_personagem.atributos['ataque'] += 5
                    personagem.classe_personagem.atributos['defesa'] += 5
                    personagem.classe_personagem.atributos['hp'] += 25
                    personagem.classe_personagem.atributos['estamina'] += 15
                    
                    novas_habilidades = self.__habilidades_por_classe.get(nova_classe, [])
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

        except KeyError as e:
            raise KeyError("Erro ao acessar informações de evolução da classe.") from e
        except ValueError as e:
            self.__personagemView.mostrar_mensagem(f"Erro: {e}")
        except AttributeError as e:
            raise AttributeError("Erro ao acessar atributos do objeto Personagem.") from e
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro inesperado ao evoluir classe: {e}")

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
                atributo_escolhido, pontos = self.__personagemView.escolher_atributo_e_quantidade()

                if atributo_escolhido is None or pontos is None:
                    self.__personagemView.mostrar_mensagem("Ação cancelada.")
                    return

                if pontos <= personagem.pontos_disponiveis:
                    if atributo_escolhido in personagem.classe_personagem.atributos:
                        personagem.classe_personagem.atributos[atributo_escolhido] += pontos
                        personagem.pontos_disponiveis -= pontos

                        self.__personagemView.mostrar_mensagem(
                            f"Atributo {atributo_escolhido} aumentado em {pontos} pontos!"
                        )
                    else:
                        raise CadastroInvalidoException(entidade="Personagem", campo=atributo_escolhido)
                else:
                    raise OperacaoNaoPermitidaException(operacao="Distribuir pontos de atributos")
            else:
                self.__personagemView.mostrar_mensagem("Você não tem pontos disponíveis para distribuir.")
        except CadastroInvalidoException as e:
            self.__personagemView.mostrar_mensagem(str(e))
        except OperacaoNaoPermitidaException as e:
            self.__personagemView.mostrar_mensagem(str(e))
        except ValueError:
            self.__personagemView.mostrar_mensagem("Valor inválido para pontos. Tente novamente.")

    def usar_item(self, personagem: Personagem):
        try:
            itens_personagem = {
                'pocoes_hp': personagem.pocao_hp.quant,
                'pocoes_est': personagem.pocao_est.quant,
            }
            tipo_item = self.__personagemView.escolher_item(itens_personagem)
            if tipo_item == 1 and personagem.pocao_hp and personagem.pocao_hp.quant > 0:
                if personagem.hp_atual < personagem.classe_personagem.atributos['hp']:
                    personagem.hp_atual += personagem.pocao_hp.valor
                    personagem.pocao_hp.quant -= 1
                    personagem.hp_atual = personagem.hp_atual
                    self.__personagemView.mostrar_mensagem(f"{personagem.nome} usou Poção de HP!")
                else:
                    raise HpJahCheioException("Não é possível usar a Poção de HP, o seu HP já está Cheio!")
            elif tipo_item == 2 and personagem.pocao_est and personagem.pocao_est.quant > 0:
                personagem.classe_personagem.atributos['estamina'] += personagem.pocao_est.valor
                personagem.pocao_est.quant -= 1
                self.__personagemView.mostrar_mensagem(f"{personagem.nome} usou Poção de Estamina!")
            else:
                raise ItemIndisponivelException(item="Poção")
        except (ItemIndisponivelException, HpJahCheioException) as e:
            self.__personagemView.mostrar_mensagem(str(e))

    def usar_itens_batalha(self, personagem):
        self.__personagemView.mostrar_mensagem(f"---Inventário---: Poção HP (quantidade: {personagem.pocao_hp.quant}), Poção Estamina (quantidade: {personagem.pocao_est.quant}")
        print("1 - Usar poção HP")
        print("2 - Usar poção Estamina")
        opcao = input("Digite o item que você quer usar: ")
        return opcao


    