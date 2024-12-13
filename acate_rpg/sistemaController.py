from gamelogger import LogJogadas
import json
import time
import PySimpleGUI as sg
import os
from sistemaView import SistemaView
from gameloggerController import LogController
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
    NumeroSetoresInvalidoError,
    CriacaoDungeonException
)



class SistemaControllerr:
    def __init__(self):
        self.__sistemaView = SistemaView()
        self.__log = LogController()
        self.__personagemController = PersonagemController()
        self.__cursoController = CursoController()
        self.__quizController = QuizController()
        self.__bossController = BossController()
        self.__setorController = SetorController()
        self.__dungeonController = DungeonController()
        self.__batalhaController = BatalhaController(self)
        self.__rankingController = RankingController(self.__personagemController)
        self.carregar_personagens()
        self.carregar_cursos()
        self.carregar_dungeons()


    @property
    def log(self):
        return self.__log
    
    @log.setter
    def log(self, log):
        self.__log = log

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
        n_cursos = self.__cursoController.carregar_cursos()
        self.__sistemaView.mostrar_mensagem(f"{n_cursos} cursos carregados com sucesso!")

    def carregar_dungeons(self):
        n_dungoens = self.__dungeonController.carregar_dungeons()
        self.__sistemaView.mostrar_mensagem(f"{n_dungoens} empresas carregadas com sucesso!")

    def carregar_personagens(self):
        n_personagens = self.__personagemController.carregar_personagens()
        self.__sistemaView.mostrar_mensagem(f"{n_personagens} personagens carregadas com sucesso!")

    def iniciar(self):
        while True:
            try:
                self.menu_usuario()
            except Exception as e:
                self.__sistemaView.mostrar_mensagem(f"Erro inesperado: {str(e)}")
                self.salvar_dados()
                self.__sistemaView.mostrar_mensagem("Saindo do sistema...")
                exit()

    def menu_usuario(self):
        while True:
            try:
                evento = self.__sistemaView.menu_inicial()

                if evento == '1':
                    self.menu_jogador()
                elif evento == '2':
                    self.menu_dungeons_empresa()
                elif evento == '3':
                    self.menu_ranking()
                elif evento == '0' or evento == sg.WINDOW_CLOSED:
                    self.salvar_dados()
                    self.__sistemaView.mostrar_mensagem("Saindo do sistema...")
                    exit()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu de usuario")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                time.sleep(2)
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")

    def menu_jogador(self):
        while True:
            try:
                evento = self.__sistemaView.menu_jogador()

                if evento == '1':
                    self.__personagemController.incluir_personagem()
                elif evento == '2':
                    personagem = self.__personagemController.selecionar_personagem()
                    if personagem:
                        self.menu_principal_personagem(personagem)
                elif evento == '3':
                    personagem = self.__personagemController.selecionar_personagem()
                    if personagem:
                        self.__personagemController.alterar_dados_personagem(personagem)
                elif evento == '4':
                    self.__personagemController.excluir_personagem()
                elif evento == '0':
                    self.salvar_dados()
                    return
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu jogador")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))

    def menu_principal_personagem(self, personagem):
        while True:
            try:
                opcao = self.__sistemaView.menu_principal_personagem(personagem.nome)

                if opcao == '1':
                    self.opcoes_personagem(personagem)
                elif opcao == '2':
                    while True:
                        try:
                            dungeon_selecionada, setor = self.__dungeonController.selecionar_dungeon_e_setor(personagem)
                            if setor is not None and setor.conquistado:
                                raise SetorJahFeitoException("O setor já foi conquistado, tente outro!")
                                
                            if dungeon_selecionada:
                                if dungeon_selecionada.conquistada:
                                    self.__sistemaView.mostrar_mensagem("Você já passou no processo seletivo dessa empresa, tente outra empresa!")
                                    time.sleep(2)
                                else:
                                    if setor is not None and not setor.conquistado:
                                        boss = setor.boss
                                        self.__batalhaController.iniciar_batalha(personagem, boss, dungeon_selecionada, setor, self.__log)
                                        self.salvar_dados()
                                        break
                                    else:
                                        boss_final = dungeon_selecionada.boss_final
                                        self.__batalhaController.iniciar_batalha(personagem, boss_final, dungeon_selecionada, setor, self.__log)
                                        self.salvar_dados()
                                        break
                            else:
                                self.__sistemaView.mostrar_mensagem("Nenhuma dungeon selecionada. Tente novamente.")
                                time.sleep(2)
                        except SetorJahFeitoException as e:
                            self.__sistemaView.mostrar_mensagem(e)
                            time.sleep(2)


                elif opcao == '3':
                    resultado, nome = self.__quizController.realizar_quiz(personagem, self.__cursoController.to_dict())
                    if resultado:
                        for cursos in self.__cursoController.cursos:
                            if cursos.nome == nome:
                                cursos.realizado = True
                        self.__personagemController.incrementar_curso(personagem)

                elif opcao == '4':
                    self.menu_log(personagem)
                    self.salvar_dados()

                elif opcao == '0':
                    self.menu_jogador()

                elif opcao == '-EXIT-':
                    self.salvar_dados()
                    exit()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu principal do personagem")
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")

    def menu_log(self, personagem):
        while True:
            try:
                opcao = self.__sistemaView.menu_log()


                if opcao == '1':
                    self.__log.listar_registros(personagem.nome)

                elif opcao == '2':
                    self.__log.alterar_registro()

                elif opcao == '3':
                    self.__log.excluir_registro()

                elif opcao == '4':
                    self.salvar_dados()
                    self.menu_principal_personagem(personagem)

                else:
                    raise OperacaoNaoPermitidaException
            
            except OperacaoNaoPermitidaException:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido")


    def opcoes_personagem(self, personagem):
        while True:
            try:
                opcao = self.__sistemaView.mostrar_opcoes_personagem()

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
                    break
                
                return
                
                
            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
                time.sleep(2)
            except ValueError:
                self.__sistemaView.mostrar_mensagem("Por favor, insira um número válido.")

    def mostrar_status(self, personagem):
        try:
            self.__personagemController.mostrar_status(personagem)
        except OperacaoNaoPermitidaException as e:
            self.__sistemaView.mostrar_mensagem(str(e))

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
        while True:
            try:
                opcao = self.__sistemaView.menu_empresa()

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
                                CriacaoBossException, ValueError, CriacaoDungeonException) as e:
                            self.__sistemaView.mostrar_mensagem(str(e))
                       
                elif opcao == "2":
                    self.dungeonController.listar_dungeons()
                    
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
                elif opcao == '0':
                    self.menu_usuario()
                else:
                    raise OperacaoNaoPermitidaException(operacao="Escolha de opção no menu de empresa")

            except OperacaoNaoPermitidaException as e:
                self.__sistemaView.mostrar_mensagem(str(e))
            
            time.sleep(2)



    def menu_curso_empresa(self):
        while True:
            opcao = self.__sistemaView.menu_cursos()
            time.sleep(1)
            if opcao == '1':
                self.__cursoController.mostrar_cursos()
            elif opcao == '2':
                self.__cursoController.cadastrar_curso()
                
            elif opcao == '3':
                self.__cursoController.alterar_curso()
            elif opcao == '4':
                self.__cursoController.excluir_curso()
            elif opcao == '5':
                self.menu_dungeons_empresa()

    def menu_ranking(self):
        while True:
            try:
                opcao = self.__sistemaView.menu_ranking()

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

    def salvar_dados(self):
        print("[INFO] Salvando todas as alterações antes de sair...")
        self.__personagemController.personagens
        self.__dungeonController.dungeons
        self.__cursoController.cursos
        self.__log.registros