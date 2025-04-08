import json
import time
import os
from models.curso import Curso
from cursoView import CursoView
from dao.cursoDAO import CursoDAO
from acate_rpg.exceptions.exceptions import CarregamentoDadosException, NivelRequeridoInvalidoError, SetorInvalidoError, DificuldadeInvalidaError, XpGanhoInvalidoError
class CursoController():
    def __init__(self):
        self.__curso_dao = CursoDAO()
        self.__cursoView = CursoView()
        self.__cursos = list(self.__curso_dao.get_all())

    @property
    def cursos(self):
        return self.__cursos
    
    def adicionar_curso(self, curso):
        self.__curso_dao.add(curso)

    def atualizar_curso(self, curso):
        self.__curso_dao.update(curso)

    def remover_curso(self, nome_curso):
        self.__curso_dao.remove(nome_curso)

    def carregar_cursos(self, caminho_arquivo = "cursos.json"):
        try:
            cursos_carregadas = self.__cursos
            return len(cursos_carregadas)
        except Exception as e:
            raise CarregamentoDadosException(arquivo="cursos.pkl", mensagem=str(e))

    def cadastrar_curso(self):
        while True:  
            dados_curso = self.__cursoView.pega_dados_curso()
            
            if dados_curso:        
                curso = Curso(
                        dados_curso["nome"], 
                        dados_curso["nivel_requerido"], 
                        dados_curso["xp_ganho"], 
                        dados_curso["setor"], 
                        dados_curso["dificuldade"], 
                        dados_curso["realizado"]
                    )
                self.adicionar_curso(curso)
                self.__cursos = list(self.__curso_dao.get_all())
                self.__cursoView.mostra_mensagem(f"O curso {dados_curso['nome']} foi cadastrado com sucesso \n")
                break  

            else:
                return

    def alterar_curso(self):
        nome = self.__cursoView.seleciona_curso(self.__cursos)
        curso = next((c for c in self.__cursos if c.nome == nome), None)

        if not curso:
            self.__cursoView.mostra_mensagem(
                f"Curso com o nome '{nome}' não foi encontrado."
            )
            return
        
        novos_dados = self.__cursoView.pega_dados_curso()
        if novos_dados:
            curso.nome = novos_dados["nome"]
            curso.nivel_requerido = novos_dados["nivel_requerido"]
            curso.xp_ganho = novos_dados["xp_ganho"]
            curso.setor = novos_dados["setor"]
            curso.dificuldade = novos_dados["dificuldade"]
            curso.realizado = novos_dados["realizado"]

            self.atualizar_curso(curso.nome)
            self.__cursos = list(self.__curso_dao.get_all())
            self.__cursoView.mostra_mensagem(f"O curso foi alterado com sucesso \n")

    def excluir_curso(self):
        nome = self.__cursoView.seleciona_curso(self.__cursos)
        curso = next((c for c in self.__cursos if c.nome == nome), None)

        if curso:
            self.remover_curso(curso.nome)
            self.__cursos = list(self.__curso_dao.get_all())
            self.__cursoView.mostra_mensagem(f"O curso '{curso.nome}' foi removido com sucesso.")
        else:
            self.__cursoView.mostra_mensagem(
                f"Curso com o nome '{nome}' não foi encontrado."
            )

    def mostrar_cursos(self):
        cursos_dicionarios = self.to_dict()   
        self.__cursoView.mostra_cursos(cursos_dicionarios)

    def to_dict(self):
        self.__cursos = list(self.__curso_dao.get_all())
        return [
            {
                "nome": curso.nome,
                "nivel_requerido": curso.nivel_requerido,
                "xp_ganho": curso.xp_ganho,
                "setor": curso.setor,
                "dificuldade": curso.dificuldade,
                "realizado": curso.realizado,
            }
            for curso in self.__cursos
        ]







