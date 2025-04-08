import time
from personagemView import PersonagemView
from models.personagem import Personagem
from dao.personagemDAO import PersonagemDAO
from classePersonagemController import ClassePersonagemController
from acate_rpg.exceptions.exceptions import CadastroInvalidoException, CarregamentoDadosException, ItemIndisponivelException, OperacaoNaoPermitidaException, HpJahCheioException
from batalhaView import BatalhaView


class PersonagemController():
    def __init__(self):
        self.__personagem_dao = PersonagemDAO()
        self.__personagens = list(self.__personagem_dao.get_all())
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
        return list(self.__personagem_dao.get_all())

    @property
    def habilidades_por_classe(self):
        return self.__habilidades_por_classe

    @property
    def niveis_para_evolucao(self):
        return self.__niveis_para_evolucao
    
    def adicionar_personagem(self, personagem):
        self.__personagem_dao.add(personagem)

    def atualizar_personagem(self, personagem):
        self.__personagem_dao.update(personagem)

    def remover_personagem(self, nome_personagem):
        self.__personagem_dao.remove(nome_personagem)

    def pega_personagem_por_nome(self, nome: str):
        personagem = next((p for p in self.__personagem_dao.get_all() if p.nome == nome), None)
        if personagem is None:
            raise CadastroInvalidoException(f"Personagem '{nome}' não encontrado.")
        return personagem
    
    def carregar_personagens(self):
        try:
            personagens_carregados = self.__personagens
            return len(personagens_carregados)
        except Exception as e:
            raise CarregamentoDadosException(arquivo="personagens.pkl", mensagem=str(e))


    def incluir_personagem(self):
        try:
            dados_personagem = self.__personagemView.pega_dados_personagem()
            
            if not dados_personagem['classe']:
                raise CadastroInvalidoException(entidade="Personagem", campo="classe")
            
            if any(p.nome == dados_personagem["nome"] for p in self.__personagem_dao.get_all()):
                raise CadastroInvalidoException(f"Um personagem com o nome '{dados_personagem['nome']}' já existe.")
            
            dungeons_conquistadas = dados_personagem.get("dungeons_conquistadas", [])
            bosses_derrotados = dados_personagem.get("bosses_derrotados", [])
            
            personagem = Personagem(
                nome=dados_personagem["nome"],
                nivel=dados_personagem.get("nivel", 1),
                experiencia_total=dados_personagem.get("experiencia_total", 0),
                pontos_disponiveis=dados_personagem.get("pontos_disponiveis", 10),
                nome_classe=dados_personagem["classe"],
                dungeons_conquistadas=dungeons_conquistadas,
                bosses_derrotados=bosses_derrotados,
                cursos_conquistados=dados_personagem.get("cursos_conquistados", 0)
            )
            
            personagem.habilidades = self.habilidades_por_classe.get(dados_personagem["classe"], [])
            personagem.classes_historico = [dados_personagem["classe"]]
            
            classe_inicial = personagem.classes_historico[0]
            if classe_inicial in ["Estagiario", "CLT"]:
                self.__classeController.definir_atributos_iniciais(personagem.classe_personagem)
            
            self.adicionar_personagem(personagem)
            
            self.__personagemView.mostrar_mensagem(
                f"Personagem {personagem.nome} da classe {personagem.classe_personagem.nome_classe} criado com sucesso! "
                f"Nível: {personagem.nivel}, Experiência: {personagem.experiencia_total}"
            )
        
        except CadastroInvalidoException as e:
            self.__personagemView.mostrar_mensagem(str(e))
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro inesperado no cadastro do Personagem: {str(e)}")
    
    def alterar_dados_personagem(self, personagem: Personagem):
        try:
            novos_dados = self.__personagemView.pega_novos_dados_personagem(personagem)

            if novos_dados is None:
                self.__personagemView.mostrar_mensagem("Ação cancelada.")
                return

            personagem.nome = novos_dados.get("nome", personagem.nome)
            personagem.nivel = novos_dados.get("nivel", personagem.nivel)
            personagem.experiencia_total = novos_dados.get("experiencia_total", personagem.experiencia_total)
            personagem.pontos_disponiveis = novos_dados.get("pontos_disponiveis", personagem.pontos_disponiveis)
            personagem.cursos_conquistados = novos_dados.get("cursos_conquistados", personagem.cursos_conquistados)

            if novos_dados.get("classe") != personagem.classe_personagem.nome_classe:
                self.alterar_classe(personagem, novos_dados["classe"])

            self.atualizar_personagem(personagem)
            self.__personagemView.mostrar_mensagem(f"Dados do personagem '{personagem.nome}' atualizados com sucesso!")
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro ao alterar dados do personagem: {str(e)}")

    def alterar_classe(self, personagem: Personagem, nova_classe_nome: str):
        try:
            # Criar a nova classe usando o ClassePersonagemController
            nova_classe = self.__classeController.criar_classe(nova_classe_nome)

            # Verificar se a nova classe já está no histórico
            if nova_classe_nome in personagem.classes_historico:
                self.__personagemView.mostrar_mensagem(
                    f"{personagem.nome} já teve a classe {nova_classe_nome}. Atualizando classe atual..."
                )
            else:
                # Adicionar nova classe ao histórico (como nome da classe)
                personagem.classes_historico.append(nova_classe_nome)

                # Adicionar habilidades da nova classe
                novas_habilidades = self.__habilidades_por_classe.get(nova_classe_nome, [])
                personagem.habilidades.extend(novas_habilidades)

                self.__personagemView.mostrar_mensagem(
                    f"{personagem.nome} mudou para a classe {nova_classe_nome} e ganhou novas habilidades."
                )

            # Atualizar a classe do personagem com o objeto de classe
            personagem.classe_personagem = nova_classe
            self.atualizar_personagem(personagem)

        except ValueError as e:
            self.__personagemView.mostrar_mensagem(f"Erro: {e}")
        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro ao alterar classe: {e}")

    def excluir_personagem(self):
        try:
            personagens = self.__personagens
            if not personagens:
                self.__personagemView.mostrar_mensagem("Nenhum personagem cadastrado para excluir.")
                return

            # Selecionar personagem para excluir
            personagem_selecionado = self.__personagemView.selecionar_personagem_para_excluir(personagens)

            if personagem_selecionado is None:
                self.__personagemView.mostrar_mensagem("Ação de exclusão cancelada.")
                return

            # Solicitar confirmação ao jogador na View
            confirmacao = self.__personagemView.confirmar_exclusao(personagem_selecionado.nome)
            if not confirmacao:
                self.__personagemView.mostrar_mensagem("Exclusão cancelada pelo jogador.")
                return

            # Remover personagem do DAO
            self.remover_personagem(personagem_selecionado.nome)

            # Atualizar lista de personagens em memória
            self.__personagens = [
                personagem for personagem in self.__personagens if personagem.nome != personagem_selecionado.nome
            ]

            self.__personagemView.mostrar_mensagem(f"Personagem '{personagem_selecionado.nome}' excluído com sucesso!")

        except Exception as e:
            self.__personagemView.mostrar_mensagem(f"Erro ao excluir personagem: {str(e)}")

    def selecionar_personagem(self):
        # Exibir os personagens na tela
        personagens = self.__personagens
        dados_personagens = [
            f"Nome: {personagem.nome} - Classe: {personagem.classe_personagem.nome_classe} - Nível: {personagem.nivel}"
            for personagem in personagens
        ]
        
        # Mostrar os personagens na View e aguardar a seleção
        personagem_selecionado = self.__personagemView.mostrar_personagens(dados_personagens)

        if personagem_selecionado is not None:
            # Encontrar o personagem correspondente ao índice selecionado
            idx_selecionado = dados_personagens.index(personagem_selecionado)
            if isinstance(self.__personagens, dict):
                personagens_lista = list(self.__personagens.values())
            else:
                personagens_lista = list(self.__personagens)
            return personagens_lista[idx_selecionado]

    def mostrar_habilidades(self, personagem: Personagem):
        try:
            habilidades_por_classe = {
                classe: [habilidade for habilidade in self.__habilidades_por_classe.get(classe, [])]
                for classe in personagem.classes_historico
            }
            self.__personagemView.mostrar_habilidades(habilidades_por_classe)
        except KeyError as e:
            raise OperacaoNaoPermitidaException("Erro ao mostrar habilidades") from e

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
            self.atualizar_personagem(personagem)

        else:
            self.__batalhaView.mostra_mensagem("O personagem não possui estamina o suficiente para usar uma habilidade!")

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
            self.atualizar_personagem(personagem)
            self.__personagens = list(self.__personagem_dao.get_all())

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
            self.__personagens = list(self.__personagem_dao.get_all())
            novo_nivel = self.calcular_nivel(personagem.experiencia_total)

            if novo_nivel > nivel_anterior:
                aumento_niveis = novo_nivel - nivel_anterior
                personagem.pontos_disponiveis += aumento_niveis * 5
                personagem.hp_atual = personagem.classe_personagem.atributos['hp']
                personagem.nivel = novo_nivel

                self.__personagemView.mostrar_mensagem(
                    f"{personagem.nome} upou para o nível {novo_nivel}! Pontos disponíveis: {personagem.pontos_disponiveis}"
                )
                self.evoluir_classe(personagem)

            self.__personagemView.mostrar_mensagem(
                f"{personagem.nome} ganhou {experiencia_ganha} XP! Experiência total: {personagem.experiencia_total}"
            )

            self.__personagemView.mostrar_mensagem(
                f"XP para próximo nível: {self.experiencia_para_proximo_nivel(personagem)}"
            )

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
                    self.__personagemView.mostrar_mensagem(f"Novas habilidades adquiridas por {nova_classe}:")

                    for habilidade in novas_habilidades:
                        self.__personagemView.mostrar_mensagem(f" - {habilidade['nome']}: {habilidade['efeito']}")
                else:
                    self.__personagemView.mostrar_mensagem(
                        f"{personagem.nome} precisa estar no nível {nivel_necessario} para evoluir para {nova_classe}."
                    )
            else:
                self.__personagemView.mostrar_mensagem(f"{personagem.nome} já é CLT e não pode evoluir.")

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

    