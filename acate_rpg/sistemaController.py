
import json
import time
import os
from sistema import Sistema
from sistemaView import SistemaView
from personagemController import PersonagemController
from cursoController import CursoController
from quizController import QuizController
from bossController import BossController
from dungeonController import DungeonController
from batalhaController import BatalhaController
from setorController import SetorController
from rankingController import RankingController
from exceptions import (
    BaseSistemaException,
    CadastroInvalidoException,
    ItemIndisponivelException,
    OperacaoNaoPermitidaException,
    CarregamentoDadosException,
    SalvamentoDadosException,
    XpGanhoInvalidoError,
    NivelRequeridoInvalidoError,
    SetorInvalidoError,
    DificuldadeInvalidaError,
    CriacaoBossException,
    CriacaoSetorException,
    ValorInvalidoBossException,
    SetorJahFeitoException,
    NumeroSetoresInvalidoError
)



class SistemaControllerr:
    def __init__(self):
        self.__sistema = Sistema()
        self.__sistemaView = SistemaView()
        self.__personagemController = PersonagemController()
        self.__cursoController = CursoController()
        self.__quizController = QuizController()
        self.__bossController = BossController()
        self.__setorController = SetorController()
        self.__dungeonController = DungeonController()
        self.__batalhaController = BatalhaController(self)
        self.__rankingController = RankingController(self.__personagemController)
        self.__arquivo_personagens = "personagens.json"
        self.carregar_personagens()
        self.carregar_cursos()
        self.carregar_dungeons()


    @property
    def cursoController(self):
        return self.__cursoController
    
    @property
    def quizController(self):
        return self.__quizController
    
    @property
    def bossController(self):
        return self.__bossController
    
    @property
    def setorController(self):
        return self.__setorController
    
    @property
    def dungeonController(self):
        return self.__dungeonController
    
    @property
    def batalhaController(self):
        return self.__batalhaController
    
    def limpar_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def carregar_cursos(self):
        self.__cursoController.carregar_cursos()


    def carregar_dungeons(self):
        self.__dungeonController.carregar_dungeons()
        


    def cadastrar_personagem(self):
        try:
            dados_personagem = self.__sistemaView.pega_dados_personagem()
            
            if not dados_personagem['classe']:
                raise CadastroInvalidoException(entidade="Personagem", campo="classe")

            for personagem_existente in self.__personagemController.personagens:
                if personagem_existente.nome == dados_personagem["nome"]:
                    raise CadastroInvalidoException(entidade="Personagem", campo="nome")

            personagem = self.__personagemController.criar_personagem(
                nome=dados_personagem["nome"],
                nivel=dados_personagem.get("nivel", 1),
                experiencia_total=dados_personagem.get("experiencia_total", 0),
                pontos_disponiveis=dados_personagem.get("pontos_disponiveis", 10),
                nome_classe=dados_personagem["classe"],
                dungeons_conquistadas=dados_personagem.get("dungeons_conquistadas", []),
                bosses_derrotados=dados_personagem.get("bosses_derrotados", []),
                cursos_conquistados=dados_personagem.get("cursos_conquistados", 0)
            )

            personagem.habilidades = self.__personagemController.habilidades_por_classe.get(dados_personagem["classe"], [])
            personagem.classes_historico = [dados_personagem["classe"]]

            self.__personagemController.personagens.append(personagem)
            self.__sistema.adicionar_personagem(personagem)
            
            self.__sistemaView.mostrar_mensagem(
                f"Personagem {personagem.nome} da classe {personagem.classe_personagem.nome_classe} criado com sucesso! "
                f"Nível: {personagem.nivel}, Experiência: {personagem.experiencia_total}"
            )
            time.sleep(2)

            self.menu_principal_personagem(personagem)
        
        except CadastroInvalidoException as e:
            self.__sistemaView.mostrar_mensagem(str(e))
            time.sleep(2)
            input("\nPressione Enter para voltar.")
        except Exception as e:
            self.__sistemaView.mostrar_mensagem(f"Erro inesperado: {str(e)}")
            input("\nPressione Enter para voltar.")


    def salvar_personagens(self):
        try:
            personagens_salvar = []
            for personagem in self.__personagemController.personagens:
                personagens_salvar.append({
                    'nome': personagem.nome,
                    'nivel': personagem.nivel,
                    'hp_atual': personagem.hp_atual,
                    'experiencia_total': personagem.experiencia_total,
                    'classe': personagem.classe_personagem.nome_classe,
                    'classes_historico': personagem.classes_historico,
                    'habilidades': personagem.habilidades,
                    'pontos_disponiveis': personagem.pontos_disponiveis,
                    'pocoes_hp': personagem.pocao_hp.quant,
                    'pocoes_est': personagem.pocao_est.quant,
                    'atributos': personagem.classe_personagem.atributos,
                    'cursos_conquistados': personagem.cursos_conquistados,
                    'dungeons_conquistadas': [{'nome': d.get('nome'), 'nivel_requerido': d.get('nivel_requerido')} if isinstance(d, dict) else {'nome': d.nome, 'nivel_requerido': d.nivel_requerido} for d in personagem.dungeons_conquistadas],
                    'bosses_derrotados': [{'nome': b.get('nome'), 'nivel_requerido': b.get('nivel_requerido')} if isinstance(b, dict) else {'nome': b.nome, 'nivel_requerido': b.nivel_requerido} for b in personagem.bosses_derrotados]
                })
            with open(self.__arquivo_personagens, 'w') as arquivo:
                json.dump(personagens_salvar, arquivo, indent=4)
            self.__sistemaView.mostrar_mensagem("Personagens salvos com sucesso!")
            time.sleep(2)
        except (OSError, IOError) as e:
            raise SalvamentoDadosException(arquivo=self.__arquivo_personagens) from e


    def carregar_personagens(self):
        try:
            with open(self.__arquivo_personagens, 'r') as arquivo:
                personagens_carregados = json.load(arquivo)
                for dados_personagem in personagens_carregados:
                    # Verifica se o personagem já existe pelo nome
                    personagem_existente = next(
                        (p for p in self.__personagemController.personagens if p.nome == dados_personagem['nome']), None
                    )

                    if personagem_existente:
                        # Atualiza apenas os atributos que podem ser alterados
                        personagem_existente.hp_atual = dados_personagem.get('hp_atual', personagem_existente.hp_atual)
                        personagem_existente.pocao_hp.quant = dados_personagem.get('pocoes_hp', personagem_existente.pocao_hp.quant)
                        personagem_existente.pocao_est.quant = dados_personagem.get('pocoes_est', personagem_existente.pocao_est.quant)
                        personagem_existente.classe_personagem.atributos.update(dados_personagem.get('atributos', {}))
                        personagem_existente.classes_historico = dados_personagem.get('classes_historico', personagem_existente.classes_historico)
                    else:
                        # Se não existir, cria um novo personagem
                        personagem = self.__personagemController.criar_personagem(
                            nome=dados_personagem['nome'],
                            nivel=dados_personagem.get('nivel', 1),
                            experiencia_total=dados_personagem.get('experiencia_total', 0),
                            pontos_disponiveis=dados_personagem.get('pontos_disponiveis', 0),
                            nome_classe=dados_personagem['classe'],
                            dungeons_conquistadas=dados_personagem.get('dungeons_conquistadas', []),
                            bosses_derrotados=dados_personagem.get('bosses_derrotados', []),
                            cursos_conquistados=dados_personagem.get('cursos_conquistados', 0)
                        )

                        personagem.pocao_hp.quant = dados_personagem.get('pocoes_hp', 0)
                        personagem.pocao_est.quant = dados_personagem.get('pocoes_est', 0)
                        personagem.hp_atual = dados_personagem.get('hp_atual', personagem.classe_personagem.atributos['hp'])
                        personagem.classes_historico = dados_personagem.get('classes_historico', [])

                        self.__personagemController.personagens.append(personagem)

                self.__sistemaView.mostrar_mensagem(f"{len(personagens_carregados)} personagens carregados com sucesso!")
                time.sleep(2)

        except FileNotFoundError:
            raise CarregamentoDadosException(arquivo=self.__arquivo_personagens)
        except json.JSONDecodeError:
            raise CarregamentoDadosException(arquivo=self.__arquivo_personagens, mensagem="Erro ao decodificar os dados JSON.")
        except Exception as e:
            raise CarregamentoDadosException(arquivo=self.__arquivo_personagens, mensagem=str(e))

    def iniciar(self):
        while True:
            try:
                self.menu_usuario()
            except Exception as e:
                self.__sistemaView.mostrar_mensagem(f"Erro inesperado: {str(e)}")
                time.sleep(3)
                self.salvar_personagens()
                self.__sistemaView.mostrar_mensagem("Saindo do sistema...")
                time.sleep(2)
                exit()

    def selecionar_personagem(self):
        try:
            personagens = self.__personagemController.personagens
            self.__sistemaView.mostrar_personagens(personagens)

            escolha = self.__sistemaView.pegar_personagem_selecionado()
            if escolha.isdigit() and 1 <= int(escolha) <= len(personagens):
                personagem = personagens[int(escolha) - 1]
                return personagem
            else:
                raise OperacaoNaoPermitidaException(operacao="Selecionar personagem")
        except OperacaoNaoPermitidaException as e:
            self.__sistemaView.mostrar_mensagem(str(e))
            return None

    def mostrar_status(self, personagem):
        try:
            self.__personagemController.mostrar_status(personagem)
        except OperacaoNaoPermitidaException as e:
            self.__sistemaView.mostrar_mensagem(str(e))

    def menu_usuario(self):
        self.limpar_terminal()
        while True:
            try:
                self.limpar_terminal()
                self.__sistemaView.menu_inicial()
                opcao = self.__sistemaView.pegar_opcao()

                if opcao == '1':
                    self.menu_jogador()
                elif opcao == '2':
                    self.menu_dungeons_empresa()
                elif opcao == '3':
                    self.menu_ranking()
                elif opcao == '0':
                    self.salvar_personagens()
                    self.dungeonController.salvar_dungeons()
                    self.__sistemaView.mostrar_mensagem("Saindo do sistema...")
                    time.sleep(2)
                    exit()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu de usuario")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                time.sleep(2)
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")

    def menu_jogador(self):
        self.limpar_terminal()
        while True:
            try:
                self.__sistemaView.menu_jogador()
                opcao = self.__sistemaView.pegar_opcao()

                if opcao == '1':
                    self.cadastrar_personagem()
                elif opcao == '2':
                    personagem = self.selecionar_personagem()
                    if personagem:
                        self.mostrar_status(personagem)
                        self.menu_principal_personagem(personagem)
                elif opcao == '0':
                    self.salvar_personagens()
                    self.__dungeonController.salvar_dungeons()
                    self.__sistemaView.mostrar_mensagem("Voltando ao menu inicial...")
                    time.sleep(2)
                    self.menu_usuario()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu de usuario")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                time.sleep(2)
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")

    def menu_principal_personagem(self, personagem):
        while True:
            try:
                self.limpar_terminal()
                self.__sistemaView.menu_principal_personagem(personagem.nome)
                opcao = self.__sistemaView.pegar_opcao()

                if opcao == '1':
                    self.opcoes_personagem(personagem)
                elif opcao == '2':
                    while True:
                        try:
                            dungeon_selecionada, setor = self.__dungeonController.selecionar_dungeon_e_setor(personagem)
                            if setor.conquistado:
                                raise SetorJahFeitoException("O setor já foi conquistado, tente outro!")
                                
                            if dungeon_selecionada:
                                if dungeon_selecionada.conquistada:
                                    self.__sistemaView.mostrar_mensagem("Você já passou no processo seletivo dessa empresa, tente outra empresa!")
                                    time.sleep(2)
                                else:
                                    if not setor.conquistado:
                                        boss = setor.boss
                                        self.__batalhaController.iniciar_batalha(personagem, boss, dungeon_selecionada, setor)
                                        break
                                    else:
                                        boss_final = dungeon_selecionada.boss_final
                                        self.__batalhaController.iniciar_batalha(personagem, boss_final, dungeon_selecionada, setor)
                                        break
                        except SetorJahFeitoException as e:
                            self.__sistemaView.mostrar_mensagem(e)
                            time.sleep(2)

                elif opcao == '3':
                    resultado = self.__quizController.realizar_quiz(personagem, self.__cursoController.cursos)
                    if resultado == True:
                        self.__personagemController.incrementar_curso(personagem)
                        
                elif opcao == '0':
                    self.menu_jogador()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu principal")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                time.sleep(2)
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")

    def opcoes_personagem(self, personagem):
        while True:
            try:
                self.__sistemaView.mostrar_opcoes_personagem()
                opcao = self.__sistemaView.pegar_opcao()

                if opcao == '1':
                    self.mostrar_status(personagem)
                elif opcao == '2':
                    self.__personagemController.upar_atributos(personagem)
                elif opcao == '3':
                    self.__personagemController.usar_item(personagem)
                elif opcao == '4':
                    self.__personagemController.mostrar_habilidades(personagem)
                elif opcao == '5':
                    experiencia_ganha = int(input("Digite a quantidade de experiência a ganhar: "))
                    self.__personagemController.ganhar_experiencia(personagem, experiencia_ganha)
                elif opcao == '6':
                    self.menu_principal_personagem(personagem)
                elif opcao == '0':
                    self.menu_jogador()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu de personagem")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                time.sleep(2)
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")

    def selecionar_dungeon(self):
        try:
            nome_dungeon = self.__sistemaView.pegar_opcao()
            for dungeon in self.__dungeonController.dungeons:
                if dungeon.nome == nome_dungeon and not dungeon.conquistada:
                    return dungeon
            raise OperacaoNaoPermitidaException(operacao="Selecionar Dungeon")
        except OperacaoNaoPermitidaException as e:
            self.__sistemaView.mostrar_mensagem(str(e))
            return None

    def menu_dungeons_empresa(self):
        self.limpar_terminal()
        while True:
            try:
                self.__sistemaView.menu_empresa()
                opcao = self.__sistemaView.pegar_opcao()

                if opcao == "1":
                    while True:  
                        try:
                            self.dungeonController.cadastrar_dungeon()
                            break  
                        except (NivelRequeridoInvalidoError, 
                                XpGanhoInvalidoError, 
                                NumeroSetoresInvalidoError, 
                                DificuldadeInvalidaError, 
                                CriacaoSetorException, 
                                CriacaoBossException, ValueError) as e:
                            self.__sistemaView.mostrar_mensagem(str(e))
                       
                elif opcao == "2":
                    self.dungeonController.listar_dungeons()
                    input("Pressione Enter para voltar: ")
                elif opcao == "3":
                    while True:

                        try:
                            self.dungeonController.alterar_dungeon()
                            break
                        except (NivelRequeridoInvalidoError, 
                                XpGanhoInvalidoError, 
                                NumeroSetoresInvalidoError, 
                                DificuldadeInvalidaError, 
                                CriacaoSetorException, 
                                CriacaoBossException, ValueError) as e:
                            self.__sistemaView.mostrar_mensagem(str(e))
                elif opcao == "4":
                    self.dungeonController.excluir_dungeon()

                elif opcao == "5":
                    self.menu_curso_empresa()
                elif opcao == "0":
                    self.menu_usuario()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu de empresa")

            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
            
            time.sleep(2)



    def menu_curso_empresa(self):
        self.limpar_terminal()
        while True:
            opcao = input("\nMenu de Cursos:\n1. Lista de Cursos\n2. Cadastrar Curso\n3. Alterar Curso\n4. Excluir Curso\n5. Voltar\nEscolha uma opção: ")
            if opcao == '1':
                self.__cursoController.mostrar_cursos()
            elif opcao == '2':
                self.__cursoController.cadastrar_curso()
                time.sleep(2)
            elif opcao == '3':
                self.__cursoController.alterar_curso()
            elif opcao == '4':
                self.__cursoController.excluir_curso()
            elif opcao == '5':
                self.menu_dungeons_empresa()

    def menu_ranking(self):
        while True:
            try:
                self.__sistemaView.menu_ranking()
                opcao = self.__sistemaView.pegar_opcao()

                if opcao == '1':
                    self.__rankingController.exibir_ranking_nivel()
                elif opcao == '2':
                    self.__rankingController.exibir_ranking_dungeons()
                elif opcao == '3':
                    self.__rankingController.exibir_ranking_cursos()
                elif opcao == '0':
                    self.menu_usuario()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu de ranking")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                time.sleep(2)
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")
