import time
import json
from dungeonView import DungeonView
from dungeon import Dungeon
from setorController import SetorController
from bossController import BossController
from exceptions import (
    CadastroInvalidoException,
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
        self.__dungeons = []
        self.__dungeonView = DungeonView()
        self.__setorController = SetorController()
        self.__bossController = BossController()
        self.__setorView = SetorView()
        self.__arquivo_dungeons = "dungeons.json"

    @property
    def dungeons(self):
        return self.__dungeons
    
    @dungeons.setter
    def dungeons(self, dungeons):
        self._dungeons = dungeons


    def cadastrar_dungeon(self):
        dados_dungeon = self.__dungeonView.pega_dados_dungeon()

        if dados_dungeon:
        
            if any(dungeon.nome == dados_dungeon["nome"] for dungeon in self.__dungeons):
                raise CriacaoDungeonException(f"A dungeon com o nome '{dados_dungeon['nome']}' já existe. Escolha um nome diferente.")
            
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

            time.sleep(0.5)

            dungeon = Dungeon(
                dados_dungeon["nome"], dados_dungeon["nivel_requerido"], dados_dungeon["xp_ganho"],
                dificuldade_media, setores, boss_final
            )

            self.__dungeons.append(dungeon)
            self.salvar_dungeons()

        else:
            return
        

        
        




    def salvar_dungeons(self):
        try:
            dungeons_data = []
            for dungeon in self.__dungeons:
                try:
                    setores_data = [
                        setor if isinstance(setor, dict) else self.__setorController.to_dict(setor)
                        for setor in dungeon.setores
                    ]
                except Exception as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao converter setor para dicionário: {str(e)}")
                    continue
                
                try:
                    boss_final_data = dungeon.boss_final
                    if not isinstance(boss_final_data, dict):
                        boss_final_data = self.__bossController.to_dict(dungeon.boss_final)
                except Exception as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao converter boss_final para dicionário: {str(e)}")
                    continue

                try:
                    dungeon_data = {
                        "nome": dungeon.nome,
                        "nivel_requerido": dungeon.nivel_requerido,
                        "xp_ganho": dungeon.xp_ganho,
                        "dificuldade": dungeon.dificuldade,
                        "setores": setores_data,
                        "boss_final": boss_final_data
                    }
                    dungeons_data.append(dungeon_data)
                except Exception as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao criar dicionário da dungeon: {str(e)}")
                    continue
                    #tinha colocado esses try/except para ver onde que ocorria um erro, mas vou deixar ai mesmo
            try:
                with open(self.__arquivo_dungeons, "w") as file:
                    json.dump(dungeons_data, file, indent=4)
                self.__dungeonView.mostra_mensagem("Dungeons salvas com sucesso!")
            except Exception as e:
                self.__dungeonView.mostra_mensagem(f"Erro ao escrever no arquivo: {str(e)}")
                input("\nPressione Enter para Voltar")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro desconhecido ao salvar dungeons: {str(e)}")
            input("\nPressione Enter para Voltar")

    def carregar_dungeons(self):
        try:
            with open(self.__arquivo_dungeons, 'r') as file:
                data = json.load(file)
                self.__dungeons = []

                for d in data:
                    try:
                        setores = []
                        for setor_data in d["setores"]:
                            try:
                                setor = self.__setorController.criar_setor_de_dicionario(setor_data)
                                setores.append(setor)
                            except Exception as e:
                                print(f"Erro ao criar setor: {str(e)}")
                                continue

                        try:
                            boss_final = self.__bossController.criar_boss_final(
                                d["boss_final"]["nome"],
                                d["boss_final"]["dificuldade"],
                                d["boss_final"]["nivel_requerido"]
                            )
                        except Exception as e:
                            print(f"Erro ao criar boss final: {str(e)}")
                            continue

                        dungeon = Dungeon(
                            d["nome"],
                            d["nivel_requerido"],
                            d["xp_ganho"],
                            d["dificuldade"],
                            setores,
                            boss_final
                        )
                        self.__dungeons.append(dungeon)

                    except Exception as e:
                        print(f"Erro ao processar a dungeon {d['nome']}: {str(e)}")
                        continue

            self.__dungeonView.mostra_mensagem(f"{len(data)} empresas carregadas com sucesso!")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro ao carregar empresas: {str(e)}")
            input("\nPressione Enter para Voltar")

    def listar_dungeons(self):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return
        
        self.__dungeonView.mostra_dungeon(self.dungeons)
            


    def selecionar_dungeon_e_setor(self, personagem):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return None, None

        self.listar_dungeons()
        dungeon_nome = self.__dungeonView.pega_nome_dungeon()
        os.system('cls' if os.name == 'nt' else 'clear')

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

            index = self.__dungeonView.mostra_dungeons_enum(self.__dungeons)
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
                self.__dungeonView.mostra_mensagem("Todos os atributos foram alterados com sucesso.")
            
            elif atributo == "xp":
                try:
                    novo_xp = int(self.__dungeonView.capturar_entrada("Digite o novo xp ganho:"))
                    if novo_xp <= 0:  
                        raise XpGanhoInvalidoError("O XP ganho deve ser um número positivo.") 
                    dungeon.xp_ganho = novo_xp
                except XpGanhoInvalidoError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao alterar o xp ganho da {dungeon.nome}: {str(e)}")

            elif atributo == "nivel":
                try:
                    novo_nivel = int(self.__dungeonView.capturar_entrada("Digite o novo nível:"))
                    if novo_xp <= 0:  
                        raise XpGanhoInvalidoError("O XP ganho deve ser um número positivo.") 
                    dungeon.xp_ganho = novo_xp
                except XpGanhoInvalidoError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao alterar o xp ganho da {dungeon.nome}: {str(e)}")

            elif atributo == "setores":
                self.alterar_setor(dungeon)
                
            elif atributo == "boss final":
                self.alterar_boss(dungeon.boss_final)

            elif atributo == 'dificuldade':
                try:
                    nova_dificuldade = float(self.__dungeonView.capturar_entrada("Digite a nova dificuldade:"))
                    if nova_dificuldade < 0:
                        raise ValueError("A dificuldade deve ser um número não negativo.")
                    dungeon.dificuldade = nova_dificuldade
                    self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
                except ValueError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro ao alterar dificuldade da {dungeon.nome}: {str(e)}")

            elif hasattr(dungeon, atributo):
                novo_valor = (self.__dungeonView.capturar_entrada("Digite a novo valor para o atributo:"))
                setattr(dungeon, atributo, novo_valor)
                self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
                
            else:
                raise OperacaoNaoPermitidaException("Atributo inválido.")
        except (OperacaoNaoPermitidaException, ValueError, NivelRequeridoInvalidoError, XpGanhoInvalidoError, DificuldadeInvalidaError) as e:
            self.__dungeonView.mostra_mensagem(f"Erro ao alterar os dados da {dungeon.nome}: {str(e)}")
            
    def alterar_setor(self, dungeon):
        setores = dungeon.setores
        if not setores:
            print("Esta dungeon não possui setores.")
            return

        self.__dungeonView.mensagem_basica("\nSetores da Empresa:")
        for i, setor in enumerate(setores):
            self.__dungeonView.mensagem_basica(f"{i + 1}. Nome: {setor.nome}, Dificuldade: {setor.dificuldade}")

        setor_num = int(input("Escolha o número do setor que deseja alterar ou excluir: ")) - 1
        if setor_num < 0 or setor_num >= len(setores):
            raise ValueError("Número de setor inválido.")

        setor = setores[setor_num]
        acao = input("Digite 'alterar' para alterar o setor ou 'excluir' para excluir: ").lower()
        nomes_disponiveis = ["RH", "T.I", "Vendas", "Financeiro", "Marketing"]

        if acao == "alterar":
            atributo = input("Digite o nome do atributo a ser alterado, 'boss' para alterar os dados do boss deste setor ou 'todos' para alterar tudo: ").lower()
            if atributo == "todos":
                novo_nome = input("Digite o novo nome do setor (disponíveis: RH, T.I, Vendas, Financeiro, Marketing): ")
                if novo_nome not in nomes_disponiveis:
                    raise SetorInvalidoError("Nome do setor inválido.")
                setor.nome = novo_nome
                
                try:
                    novo_dificuldade = float(input("Digite a nova dificuldade: "))
                    if novo_dificuldade < 0:
                        raise ValueError("A dificuldade deve ser um número não negativo.")
                    setor.dificuldade = novo_dificuldade
                    dungeon.dificuldade = self.calcular_dificuldade(dungeon)
                    self.__dungeonView.mostra_mensagem("Todos os atributos do setor foram alterados com sucesso.")
                except ValueError as e:
                    self.__dungeonView.mostra_mensagem(f"Erro: {str(e)}")

            elif hasattr(setor, atributo):
                novo_valor = input(f"Digite o novo valor para {atributo}: ")
                if atributo == 'nome':
                    if novo_valor not in nomes_disponiveis:
                        raise SetorInvalidoError("Nome do setor inválido.")
                    setor.nome = novo_valor
                elif atributo == 'dificuldade':
                    try:
                        novo_valor_float = float(novo_valor)
                        if novo_valor_float < 0:
                            raise ValueError("A dificuldade deve ser um número não negativo.")
                        setor.dificuldade = novo_valor_float
                        dungeon.dificuldade = self.calcular_dificuldade(dungeon)
                        self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
                    except ValueError as e:
                        self.__dungeonView.mostra_mensagem(f"Erro: {str(e)}")
                elif atributo == "boss":
                    try:
                        self.alterar_boss(setor.boss)
                    except ValueError:
                        self.__dungeonView.mostra_mensagem("Este setor não possui um boss para alterar.")
                else:
                    setattr(setor, atributo, novo_valor)
                    self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
            else:
                self.__dungeonView.mostra_mensagem("Atributo inválido.")

        elif acao == "excluir":
            if len(setores) == 1:
                confirmacao = input("Este é o último setor da dungeon. Tem certeza que deseja excluir? (s/n): ")
                if confirmacao.lower() == 's':
                    self.excluir_dungeon_sem_setores(dungeon)
                else:
                    self.__dungeonView.mostra_mensagem("Exclusão cancelada.")
            else:
                confirmacao = input(f"Tem certeza que deseja excluir o setor '{setor.nome}'? (s/n): ")
                if confirmacao.lower() == 's':
                    dungeon.setores.remove(setor)
                    dungeon.dificuldade = self.calcular_dificuldade(dungeon)
                    self.__dungeonView.mostra_mensagem("Setor excluído com sucesso.")
                else:
                    self.__dungeonView.mostra_mensagem("Exclusão cancelada.")

    def alterar_boss(self, boss):
        try:
            self.__dungeonView.mostra_mensagem("Alterando atributos do Boss:")
            self.__bossController.to_dict(boss)
            opcao = input("Digite o nome do atributo a ser alterado ou 'todos' para alterar tudo: ").lower()
            
            if opcao == 'todos':
                novo_nome = input("Digite o novo nome do boss: ")
                boss.nome = novo_nome

                nova_dificuldade = int(input("Digite a nova dificuldade: "))
                boss.dificuldade = nova_dificuldade
                atributos_recalculados = self.__bossController.criar_boss(
                    boss.nome, boss.dificuldade, boss.nivel_requerido, 0, 0, 0, 0).atributos
                boss.atributos.update(atributos_recalculados)

                novo_nivel_requerido = int(input("Digite o novo nível requerido: "))
                boss.nivel_requerido = novo_nivel_requerido

                self.__dungeonView.mostra_mensagem("Todos os atributos do boss foram alterados com sucesso.")

            elif opcao == "dificuldade":
                nova_dificuldade = int(input("Digite a nova dificuldade: "))
                if nova_dificuldade < 0:
                    raise ValueError("Dificuldade deve ser um número não negativo, de 1-10.")
                boss.dificuldade = nova_dificuldade
                atributos_recalculados = self.__bossController.criar_boss(
                    boss.nome, boss.dificuldade, boss.nivel_requerido, 0, 0, 0, 0).atributos
                boss.atributos.update(atributos_recalculados)
                self.__dungeonView.mostra_mensagem("Dificuldade e atributos recalculados com sucesso.")

            elif opcao == "nivel_requerido":
                novo_nivel_requerido = int(input("Digite o novo nível requerido: "))
                boss.nivel_requerido = novo_nivel_requerido
                self.__dungeonView.mostra_mensagem("Nível requerido alterado com sucesso.")

            elif hasattr(boss, opcao):
                novo_valor = input(f"Digite o novo valor para {opcao}: ")
                setattr(boss, opcao, int(novo_valor) if opcao in ['ataque', 'defesa', 'hp', 'estamina'] else novo_valor)
                self.__dungeonView.mostra_mensagem(f"Atributo {opcao} alterado com sucesso.")
            else:
                raise CadastroInvalidoException("Boss", opcao, "Verifique o nome do atributo e tente novamente.")

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

    def excluir_dungeon_sem_setores(self, dungeon):
        confirmacao = input(f"Tem certeza que deseja excluir a dungeon '{dungeon.nome}'? (s/n): ")
        if confirmacao.lower() == 's':
            self.dungeons.remove(dungeon)
            self.__dungeonView.mostra_mensagem("Dungeon excluída com sucesso.")
        else:
            self.__dungeonView.mostra_mensagem("Exclusão cancelada.")

    def excluir_dungeon(self):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return

        dungeon_opcao = self.__dungeonView.mostra_dungeons_enum(self.__dungeons)
        try:
            dungeon = self.__dungeons[dungeon_opcao]
            if self.__dungeonView.confirma_exclusao(dungeon.nome):
                del self.__dungeons[dungeon_opcao]
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
        for dungeon in self.dungeons:
            if dungeon.nome.lower() == nome.lower():
                return dungeon
        return None
