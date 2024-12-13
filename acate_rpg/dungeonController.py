import time
import json
from dungeonView import DungeonView
from dungeon import Dungeon
from dungeonDAO import DungeonDAO
from setorController import SetorController
from bossController import BossController
from exceptions import (
    CadastroInvalidoException,
    CarregamentoDadosException,
    OperacaoNaoPermitidaException,
    XpGanhoInvalidoError,
    NivelRequeridoInvalidoError,
    DificuldadeInvalidaError,
    CriacaoBossException,
    CriacaoSetorException,
    NumeroSetoresInvalidoError,
    CriacaoDungeonException,
    SetorInvalidoError
)
import os
from setorView import SetorView
class DungeonController:
    def __init__(self):
        self.__dungeon_dao = DungeonDAO()
        self.__dungeons = list(self.__dungeon_dao.get_all())
        self.__dungeonView = DungeonView()
        self.__setorController = SetorController()
        self.__bossController = BossController()
        self.__setorView = SetorView()

    @property
    def dungeons(self):
        return list(self.__dungeon_dao.get_all())
    
    def adicionar_dungeon(self, dungeon):
        self.__dungeon_dao.add(dungeon)

    def atualizar_dungeon(self, dungeon):
        self.__dungeon_dao.update(dungeon)

    def remover_dungeon(self, nome_dungeon):
        self.__dungeon_dao.remove(nome_dungeon)

    def carregar_dungeons(self):
        try:
            dungeons_carregadas = self.__dungeons
            return len(dungeons_carregadas)
        except Exception as e:
            raise CarregamentoDadosException(arquivo="dungeons.pkl", mensagem=str(e))

    def cadastrar_dungeon(self):
        try:
            dados_dungeon = self.__dungeonView.pega_dados_dungeon()

            if dados_dungeon:
                if any(dungeon.nome == dados_dungeon["nome"] for dungeon in self.__dungeons):
                    raise CriacaoDungeonException(
                        f"A dungeon com o nome '{dados_dungeon['nome']}' já existe. Escolha um nome diferente."
                    )

                setores = []
                for i in range(dados_dungeon["n_setores"]):
                    nome_setor = self.__setorView.pega_nome_setor(i + 1)
                    dificuldade_setor = self.__setorView.pega_dificuldade_setor()

                    if not isinstance(dificuldade_setor, int) or not (1 <= dificuldade_setor <= 10):
                        raise DificuldadeInvalidaError("A dificuldade do setor deve ser um número inteiro entre 1 e 10.")

                    setor = self.__setorController.criar_setor_com_boss(
                        nome_setor, dificuldade_setor, dados_dungeon["nivel_requerido"], dados_dungeon["nome"]
                    )

                    if setor:
                        setores.append(setor)
                    else:
                        raise CriacaoSetorException("Erro ao criar setor com boss.")

                dificuldade_media = round(sum(setor.dificuldade for setor in setores) / len(setores), 1)

                nome_boss_final = self.__dungeonView.pega_nome_boss_final()
                boss_final = self.__bossController.criar_boss_final(
                    nome_boss_final, dificuldade_media, dados_dungeon["nivel_requerido"]
                )

                dungeon = Dungeon(
                    dados_dungeon["nome"], dados_dungeon["nivel_requerido"], dados_dungeon["xp_ganho"],
                    dificuldade_media, setores, boss_final
                )

                self.adicionar_dungeon(dungeon)
                self.__dungeons = list(self.__dungeon_dao.get_all())
                self.__dungeonView.mostra_mensagem(f"Dungeon '{dungeon.nome}' cadastrada com sucesso!")

        except (CriacaoDungeonException, DificuldadeInvalidaError, CriacaoSetorException) as e:
            self.__dungeonView.mostra_mensagem(f"Erro ao cadastrar dungeon: {e}")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro inesperado ao cadastrar dungeon: {e}")

    def listar_dungeons(self):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return

        # Converte as dungeons para dicionários
        dungeons_formatadas = [
            {
                "nome": dungeon.nome,
                "nivel_requerido": dungeon.nivel_requerido,
                "xp_ganho": dungeon.xp_ganho,
                "dificuldade": dungeon.dificuldade,
                "setores": [
                    {
                        "nome": setor.nome,
                        "dificuldade": setor.dificuldade,
                        "boss": {
                            "nome": setor.boss.nome,
                            "dificuldade": setor.boss.dificuldade,
                            "nivel_requerido": setor.boss.nivel_requerido
                        }
                    }
                    for setor in dungeon.setores
                ],
                "boss_final": {
                    "nome": dungeon.boss_final.nome,
                    "dificuldade": dungeon.boss_final.dificuldade,
                    "nivel_requerido": dungeon.boss_final.nivel_requerido
                }
            }
            for dungeon in self.__dungeons
        ]

        self.__dungeonView.mostra_dungeon(dungeons_formatadas)

            


    def selecionar_dungeon_e_setor(self, personagem):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return None, None

        self.listar_dungeons()
        dungeon_nome = self.__dungeonView.pega_nome_dungeon()
        
        if dungeon_nome == None:
            return None, None

        dungeon_selecionada = next((dungeon for dungeon in self.__dungeons if dungeon.nome == dungeon_nome), None)
        if not dungeon_selecionada:
            self.__dungeonView.mostra_mensagem("Empresa não encontrada.")
            return None, None
        
        if dungeon_selecionada.nivel_requerido > personagem.nivel:
            self.__dungeonView.mostra_mensagem("Infelizmente esperamos candidatos com mais experiência, boa sorte na próxima!")
            time.sleep(2)
            return None, None

        self.__dungeonView.mensagem_basica(f"Setores da empresa {dungeon_nome}:")
        for idx, setor in enumerate(dungeon_selecionada.setores):
            self.__dungeonView.mensagem_basica(f"{idx + 1} - Setor: {setor.nome}, Dificuldade: {setor.dificuldade}")

        self.__dungeonView.mensagem_basica("\nVocê deseja aplicar para o processo seletivo de um setor (1) ou para o de diretor geral (2)?")
        opcao = self.__setorView.pega_opcao_boss()

        if opcao == '1':
            setor_opcao = int(self.__setorView.pega_opcao_setor()) - 1
            if 0 <= setor_opcao < len(dungeon_selecionada.setores):
                setor_selecionado = dungeon_selecionada.setores[setor_opcao]
                return dungeon_selecionada, setor_selecionado
            else:
                self.__dungeonView.mostra_mensagem("Setor inválido.")
                return dungeon_selecionada, None

        elif opcao == '2':
            return dungeon_selecionada, None
        else:
            self.__dungeonView.mostra_mensagem("Opção inválida.")
            return None, None

    def alterar_dungeon(self):
        try:
            if not self.__dungeons:
                raise OperacaoNaoPermitidaException("Nenhuma dungeon cadastrada.")
            dungeons_formatadas = [
            {
                "nome": dungeon.nome,
                "nivel_requerido": dungeon.nivel_requerido,
                "xp_ganho": dungeon.xp_ganho,
                "dificuldade": dungeon.dificuldade,
                "setores": [
                    {
                        "nome": setor.nome,
                        "dificuldade": setor.dificuldade,
                        "boss": {
                            "nome": setor.boss.nome,
                            "dificuldade": setor.boss.dificuldade,
                            "nivel_requerido": setor.boss.nivel_requerido
                        }
                    }
                    for setor in dungeon.setores
                ],
                "boss_final": {
                    "nome": dungeon.boss_final.nome,
                    "dificuldade": dungeon.boss_final.dificuldade,
                    "nivel_requerido": dungeon.boss_final.nivel_requerido
                }
            }
            for dungeon in self.__dungeons
        ]

            index = self.__dungeonView.mostra_dungeons_enum(dungeons_formatadas)
            if index is None:
                return
            
            dungeon_num = index
            dungeon = self.__dungeons[dungeon_num]

            self.__dungeonView.mensagem_basica("\nAtributos alteráveis: nome, nivel, xp, dificuldade, setores e boss final")
            atributo = self.__dungeonView.capturar_entrada("Digite o atributo que você quer alterar ou Todos")
            if atributo.lower() == "todos":
                novo_nome = self.__dungeonView.capturar_entrada("Digite o novo nome:")
                if novo_nome == "":
                    raise ValueError("O nome não pode ser vazio")

                dungeon.nome = novo_nome

                novo_nivel = int(self.__dungeonView.capturar_entrada("Digite o novo nível:"))
                if not (1 <= novo_nivel <= 100):
                    raise NivelRequeridoInvalidoError("O nível requerido deve ser um número inteiro entre 1 e 100.")
                dungeon.nivel_requerido = novo_nivel

                novo_xp = int(self.__dungeonView.capturar_entrada("Digite o novo xp ganho:"))
                if novo_xp <= 0:
                    raise XpGanhoInvalidoError("O XP ganho deve ser um número positivo.")
                dungeon.xp_ganho = novo_xp

                novo_dificuldade = float(self.__dungeonView.capturar_entrada("Digite a nova dificuldade:"))
                if not (1 <= novo_dificuldade <= 10):
                    raise DificuldadeInvalidaError("O número de setores deve estar entre 1 e 10.")
                dungeon.dificuldade = novo_dificuldade

                self.atualizar_dungeon(dungeon)
                self.__dungeonView.mostra_mensagem("Todos os atributos foram alterados com sucesso.")

            elif atributo == "xp":
                try:
                    novo_xp = int(self.__dungeonView.capturar_entrada("Digite o novo xp ganho:"))
                    if novo_xp <= 0:
                        raise XpGanhoInvalidoError("O XP ganho deve ser um número positivo.")
                    dungeon.xp_ganho = novo_xp
                    self.atualizar_dungeon(dungeon)
                except XpGanhoInvalidoError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao alterar o xp ganho da {dungeon.nome}: {str(e)}")

            elif atributo == "nivel":
                try:
                    novo_nivel = int(self.__dungeonView.capturar_entrada("Digite o novo nível:"))
                    if not (1 <= novo_nivel <= 100):
                        raise NivelRequeridoInvalidoError("O nível requerido deve ser um número inteiro entre 1 e 100.")
                    dungeon.nivel_requerido = novo_nivel
                    self.atualizar_dungeon(dungeon)
                except NivelRequeridoInvalidoError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao alterar o nível da {dungeon.nome}: {str(e)}")

            elif atributo == "setores":
                self.alterar_setor(dungeon)
                self.atualizar_dungeon(dungeon)

            elif atributo == "boss final":
                self.alterar_boss(dungeon.boss_final)
                self.atualizar_dungeon(dungeon)

            elif atributo == 'dificuldade':
                try:
                    nova_dificuldade = float(self.__dungeonView.capturar_entrada("Digite a nova dificuldade:"))
                    if nova_dificuldade < 0:
                        raise ValueError("A dificuldade deve ser um número não negativo.")
                    dungeon.dificuldade = nova_dificuldade
                    self.atualizar_dungeon(dungeon)
                    self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
                except ValueError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao alterar dificuldade da {dungeon.nome}: {str(e)}")

            elif hasattr(dungeon, atributo):
                novo_valor = self.__dungeonView.capturar_entrada(f"Digite o novo valor para o atributo {atributo}:")
                setattr(dungeon, atributo, novo_valor)
                self.atualizar_dungeon(dungeon)
                self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
            else:
                raise OperacaoNaoPermitidaException("Atributo inválido.")

            self.atualizar_dungeon(dungeon)
            self.__dungeons = list(self.__dungeon_dao.get_all())

        except (OperacaoNaoPermitidaException, ValueError, NivelRequeridoInvalidoError, XpGanhoInvalidoError, DificuldadeInvalidaError) as e:
            self.__dungeonView.mostra_mensagem(f"Erro ao alterar os dados da {dungeon.nome}: {str(e)}")
            
    def alterar_setor(self, dungeon):
        setores = dungeon.setores
        if not setores:
            self.__dungeonView.mostra_mensagem("Esta dungeon não possui setores.")
            return

        self.__dungeonView.mensagem_basica("\nSetores da Empresa:")
        for i, setor in enumerate(setores):
            self.__dungeonView.mensagem_basica(f"{i + 1}. Nome: {setor.nome}, Dificuldade: {setor.dificuldade}")

        setor_num = int(self.__dungeonView.capturar_entrada("Escolha o número do setor que deseja alterar ou excluir: ")) - 1
        if setor_num < 0 or setor_num >= len(setores):
            raise ValueError("Número de setor inválido.")

        setor = setores[setor_num]
        acao = self.__dungeonView.capturar_entrada("Digite 'alterar' para alterar o setor ou 'excluir' para excluir: ").lower()
        nomes_disponiveis = ["RH", "T.I", "Vendas", "Financeiro", "Marketing"]

        if acao == "alterar":
            atributo = self.__dungeonView.capturar_entrada("Digite o nome do atributo a ser alterado, 'boss' para alterar o boss ou 'todos' para alterar tudo: ").lower()
            if atributo == "todos":
                novo_nome = self.__dungeonView.capturar_entrada("Digite o novo nome do setor:")
                if novo_nome not in nomes_disponiveis:
                    raise SetorInvalidoError("Nome do setor inválido.")
                setor.nome = novo_nome

                try:
                    novo_dificuldade = float(self.__dungeonView.capturar_entrada("Digite a nova dificuldade: "))
                    if novo_dificuldade < 0:
                        raise ValueError("A dificuldade deve ser um número não negativo.")
                    setor.dificuldade = novo_dificuldade
                    dungeon.dificuldade = self.calcular_dificuldade(dungeon)
                    self.atualizar_dungeon(dungeon)
                    self.__dungeonView.mostra_mensagem("Todos os atributos do setor foram alterados com sucesso.")
                except ValueError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro: {str(e)}")

            elif atributo == "boss":
                self.alterar_boss(setor.boss)
                self.atualizar_dungeon(dungeon)

            else:
                novo_valor = self.__dungeonView.capturar_entrada(f"Digite o novo valor para {atributo}: ")
                setattr(setor, atributo, novo_valor)
                self.atualizar_dungeon(dungeon)
                self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")

        elif acao == "excluir":
            if len(setores) == 1:
                confirmacao = self.__dungeonView.capturar_entrada("Este é o último setor da dungeon. Tem certeza que deseja excluir? (s/n): ")
                if confirmacao.lower() == 's':
                    self.remover_dungeon(dungeon.nome)
                    self.__dungeons = list(self.__dungeon_dao.get_all())
                    self.__dungeonView.mostra_mensagem("Dungeon excluída pois não possui mais setores.")
                else:
                    self.__dungeonView.mostra_mensagem("Exclusão cancelada.")
            else:
                confirmacao = self.__dungeonView.capturar_entrada(f"Tem certeza que deseja excluir o setor '{setor.nome}'? (s/n): ")
                if confirmacao.lower() == 's':
                    dungeon.setores.remove(setor)
                    dungeon.dificuldade = self.calcular_dificuldade(dungeon)
                    self.atualizar_dungeon(dungeon)
                    self.__dungeonView.mostra_mensagem("Setor excluído com sucesso.")
                else:
                    self.__dungeonView.mostra_mensagem("Exclusão cancelada.")

    def alterar_boss(self, dungeon, boss):
        try:
            self.__dungeonView.mostra_mensagem("Alterando atributos do Boss:")
            self.__bossController.to_dict(boss)
            opcao = self.__dungeonView.capturar_entrada("Digite o nome do atributo a ser alterado ou 'todos' para alterar tudo: ").lower()

            if opcao == 'todos':
                novo_nome = self.__dungeonView.capturar_entrada("Digite o novo nome do boss: ")
                boss.nome = novo_nome

                nova_dificuldade = int(self.__dungeonView.capturar_entrada("Digite a nova dificuldade: "))
                boss.dificuldade = nova_dificuldade
                atributos_recalculados = self.__bossController.criar_boss(
                    boss.nome, boss.dificuldade, boss.nivel_requerido, 0, 0, 0, 0).atributos
                boss.atributos.update(atributos_recalculados)

                novo_nivel_requerido = int(self.__dungeonView.capturar_entrada("Digite o novo nível requerido: "))
                boss.nivel_requerido = novo_nivel_requerido

                self.__dungeonView.mostra_mensagem("Todos os atributos do boss foram alterados com sucesso.")

            elif opcao == "dificuldade":
                nova_dificuldade = int(self.__dungeonView.capturar_entrada("Digite a nova dificuldade: "))
                if nova_dificuldade < 0:
                    raise ValueError("Dificuldade deve ser um número não negativo, de 1-10.")
                boss.dificuldade = nova_dificuldade
                atributos_recalculados = self.__bossController.criar_boss(
                    boss.nome, boss.dificuldade, boss.nivel_requerido, 0, 0, 0, 0).atributos
                boss.atributos.update(atributos_recalculados)
                self.__dungeonView.mostra_mensagem("Dificuldade e atributos recalculados com sucesso.")

            elif opcao == "nivel_requerido":
                novo_nivel_requerido = int(self.__dungeonView.capturar_entrada("Digite o novo nível requerido: "))
                boss.nivel_requerido = novo_nivel_requerido
                self.__dungeonView.mostra_mensagem("Nível requerido alterado com sucesso.")

            elif hasattr(boss, opcao):
                novo_valor = self.__dungeonView.capturar_entrada(f"Digite o novo valor para {opcao}: ")
                setattr(boss, opcao, int(novo_valor) if opcao in ['ataque', 'defesa', 'hp', 'estamina'] else novo_valor)
                self.__dungeonView.mostra_mensagem(f"Atributo {opcao} alterado com sucesso.")
            else:
                raise CadastroInvalidoException("Boss", opcao, "Verifique o nome do atributo e tente novamente.")

            self.atualizar_dungeon(dungeon)

        except ValueError:
            self.__dungeonView.mostra_mensagem("Erro: o valor digitado é inválido. Insira um número para atributos numéricos.")
        except CadastroInvalidoException as e:
            self.__dungeonView.mostra_mensagem(str(e))
        except CriacaoBossException as e:
            self.__dungeonView.mostra_mensagem(f"Erro ao criar ou alterar boss: {str(e)}")
        except OperacaoNaoPermitidaException as e:
            self.__dungeonView.mostra_mensagem(f"Operação não permitida: {str(e)}")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro inesperado ao alterar boss: {str(e)}")


    def excluir_dungeon(self):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return

        # Prepara os dados como dicionários
        dungeons_formatadas = [
            {"nome": dungeon.nome, "nivel_requerido": dungeon.nivel_requerido}
            for dungeon in self.__dungeons
        ]

        # Exibe a lista e retorna a seleção
        dungeon_opcao = self.__dungeonView.mostra_dungeons_enum(dungeons_formatadas)

        if dungeon_opcao is None:
            self.__dungeonView.mostra_mensagem("Operação cancelada.")
            return

        try:
            # Exclui a dungeon com base no índice selecionado
            dungeon = self.__dungeons[dungeon_opcao]
            if self.__dungeonView.confirma_exclusao(dungeon.nome):
                self.remover_dungeon(dungeon.nome)
                self.__dungeons = list(self.__dungeon_dao.get_all())
                self.__dungeonView.mostra_mensagem("Dungeon excluída com sucesso.")
            else:
                self.__dungeonView.mostra_mensagem("Exclusão cancelada.")
        except IndexError:
            self.__dungeonView.mostra_mensagem("Número de dungeon inválido.")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro inesperado ao excluir dungeon: {str(e)}")


    def calcular_dificuldade(self, dungeon):
        return sum(setor.dificuldade for setor in dungeon.setores) / len(dungeon.setores)
    
    def buscar_dungeon_por_nome(self, nome):
        for dungeon in self.__dungeons:
            if dungeon.nome.lower() == nome.lower():
                return dungeon
        return None

