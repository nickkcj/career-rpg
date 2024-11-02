import time
import json
from dungeonView import DungeonView
from dungeon import Dungeon
from setorController import SetorController
from bossController import BossController
from exceptions import CriacaoSetorException, CriacaoBossException, CadastroInvalidoException, CriacaoBossException, OperacaoNaoPermitidaException

class DungeonController:
    def __init__(self):
        self.__dungeons = []
        self.__dungeonView = DungeonView()
        self.__setorController = SetorController()
        self.__bossController = BossController()
        self.__arquivo_dungeons = "dungeons.json"

    @property
    def dungeons(self):
        return self.__dungeons
    
    @dungeons.setter
    def dungeons(self, dungeons):
        self._dungeons = dungeons

    def cadastrar_dungeon(self):
        try:
            dados_dungeon = self.__dungeonView.pega_dados_dungeon()
            setores = []
            
            for i in range(dados_dungeon["n_setores"]):
                nome_setor = self.__dungeonView.pega_nome_setor(i + 1)
                dificuldade_setor = self.__dungeonView.pega_dificuldade_setor()
                
                setor = self.__setorController.criar_setor_com_boss(nome_setor, dificuldade_setor, dados_dungeon["nivel_requerido"], dados_dungeon["nome"])
                if setor:
                    setores.append(setor)
                else:
                    raise CriacaoSetorException("Erro ao criar setor com boss.")

            dificuldade = round(sum(setor.dificuldade for setor in setores) / len(setores), 1)
            
            nome_boss_final = self.__dungeonView.pega_nome_boss_final()
            boss_final = self.__bossController.criar_boss_final(nome_boss_final, dificuldade, dados_dungeon["nivel_requerido"])
            time.sleep(1)

            dungeon = Dungeon(dados_dungeon["nome"], dados_dungeon["nivel_requerido"], dados_dungeon["xp_ganho"], dificuldade, setores, boss_final)
            self.__dungeons.append(dungeon)
            print(f"Dungeon: {dungeon.nome}")
            print(f"Boss final: {self.__bossController.to_dict(boss_final)}")
            self.salvar_dungeons()
            self.__dungeonView.mostra_dungeon(dungeon)
            time.sleep(2)
            input("\nPressione Enter para voltar ao menu.")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro inesperado no cadastro: {str(e)}")
            input("\nPressione Enter para voltar ao menu.")

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

            self.__dungeonView.mostra_mensagem(f"{len(data)} dungeons carregadas com sucesso!")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro ao carregar dungeons: {str(e)}")
            input("\nPressione Enter para Voltar")

    def listar_dungeons(self):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return

        self.__dungeonView.mostra_mensagem("Dungeons cadastradas:")
        for dungeon in self.__dungeons:
            self.__dungeonView.mostra_dungeon(dungeon)
        input("\nPressione Enter para Voltar")

    def selecionar_dungeon_e_setor(self):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return None, None

        self.listar_dungeons()
        dungeon_nome = self.__dungeonView.pega_nome_dungeon()

        dungeon_selecionada = next((dungeon for dungeon in self.__dungeons if dungeon.nome == dungeon_nome), None)
        if not dungeon_selecionada:
            self.__dungeonView.mostra_mensagem("Dungeon não encontrada.")
            return None, None

        self.__dungeonView.mostra_mensagem(f"Setores da dungeon {dungeon_nome}:")
        for idx, setor in enumerate(dungeon_selecionada.setores):
            self.__dungeonView.mostra_mensagem(f"{idx + 1} - Setor: {setor.nome}, Dificuldade: {setor.dificuldade}")

        setor_opcao = int(self.__dungeonView.pega_opcao_setor()) - 1
        if 0 <= setor_opcao < len(dungeon_selecionada.setores):
            setor_selecionado = dungeon_selecionada.setores[setor_opcao]
            return dungeon_selecionada, setor_selecionado
        else:
            self.__dungeonView.mostra_mensagem("Setor inválido.")
            return dungeon_selecionada, None
        
    def alterar_dungeon(self):
        if not self.__dungeons:
            self.__dungeonView.mostra_mensagem("Nenhuma dungeon cadastrada.")
            return

        self.__dungeonView.mostra_dungeons_enum(self.__dungeons)
        dungeon_num = int(input("Escolha o número da dungeon que deseja alterar: ")) - 1
        try:
            dungeon = self.dungeons[dungeon_num]
            self.__dungeonView.mostra_dungeon(dungeon)

            atributo = input("\nDigite o nome do atributo a ser alterado ou 'todos' para alterar tudo: ").lower()
            if atributo == "todos":
                novo_nome = input("Digite o novo nome da dungeon: ")
                dungeon.nome = novo_nome
                novo_nivel = int(input("Digite o novo nível requerido: "))
                dungeon.nivel_requerido = novo_nivel
                novo_xp = int(input("Digite o novo XP ganho: "))
                dungeon.xp_ganho = novo_xp
                novo_dificuldade = float(input("Digite a nova dificuldade: "))
                dungeon.dificuldade = novo_dificuldade
                self.__dungeonView.mostra_mensagem("Todos os atributos foram alterados com sucesso.")
            elif atributo == "setores":
                self.alterar_setor(dungeon)
            elif atributo == "boss final":
                self.alterar_boss(dungeon.boss_final)
            elif hasattr(dungeon, atributo):
                novo_valor = input(f"Digite o novo valor para {atributo}: ")
                setattr(dungeon, atributo, novo_valor)
                self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
            else:
                self.__dungeonView.mostra_mensagem("Atributo inválido.")
        except ValueError as ve:
            self.__dungeonView.mostra_mensagem(f"Erro ao alterar dungeon: {str(ve)}")
            input("\nPressione Enter para Voltar")
        except IndexError:
            self.__dungeonView.mostra_mensagem("Número de dungeon inválido.")
            input("\nPressione Enter para Voltar")
        except Exception as e:
            self.__dungeonView.mostra_mensagem(f"Erro inesperado ao alterar dungeon: {str(e)}")
            input("\nPressione Enter para Voltar")

    def alterar_setor(self, dungeon):
        setores = dungeon.setores
        if not setores:
            print("Esta dungeon não possui setores.")
            return

        print("Setores da Dungeon:")
        for i, setor in enumerate(setores):
            print(f"{i + 1}. Nome: {setor.nome}, Dificuldade: {setor.dificuldade}")

        setor_num = int(input("Escolha o número do setor que deseja alterar ou excluir: ")) - 1
        if setor_num < 0 or setor_num >= len(setores):
            print("Número de setor inválido.")
            return

        setor = setores[setor_num]
        acao = input("Digite 'alterar' para alterar o setor ou 'excluir' para excluir: ").lower()
        
        if acao == "alterar":
            atributo = input("Digite o nome do atributo a ser alterado ou 'todos' para alterar tudo: ").lower()
            if atributo == "todos":
                novo_nome = input("Digite o novo nome do setor: ")
                setor.nome = novo_nome
                novo_dificuldade = float(input("Digite a nova dificuldade: "))
                setor.dificuldade = novo_dificuldade
                self.__dungeonView.mostra_mensagem("Todos os atributos do setor foram alterados com sucesso.")
            elif hasattr(setor, atributo):
                novo_valor = input(f"Digite o novo valor para {atributo}: ")
                setattr(dungeon, atributo, novo_valor)
                self.__dungeonView.mostra_mensagem(f"Atributo {atributo} alterado com sucesso.")
            else:
                self.__dungeonView.mostra_mensagem("Atributo inválido.")

        elif acao == "boss":
            if setor.boss:
                self.alterar_boss(setor.boss)
            else:
                self.__dungeonView.mostra_mensagem("Este setor não possui um boss para alterar.")
                #impossivel, mas vamos deixar pra ver se não dá erro

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
            print("Alterar atributos do Boss:")
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

        self.__dungeonView.mostra_dungeons_enum(self.__dungeons)
        dungeon_opcao = int(input("Escolha o número da dungeon que deseja excluir: ")) - 1
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
