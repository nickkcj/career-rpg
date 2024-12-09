import json
import time
import os
from curso import Curso
from cursoView import CursoView
from exceptions import NivelRequeridoInvalidoError, SetorInvalidoError, DificuldadeInvalidaError, XpGanhoInvalidoError
class CursoController():
    def __init__(self):
        self.cursos = []
        self.__cursoView = CursoView()

    def carregar_cursos(self, caminho_arquivo = "cursos.json"):
            try:
                with open(caminho_arquivo, "r") as arquivo:
                    dados_curso = json.load(arquivo)

                    for dados in dados_curso:
                        curso = Curso(
                            nome=dados["nome"],
                            nivel_requerido=dados["nivel_requerido"],
                            xp_ganho=dados["xp_ganho"],
                            setor=dados["setor"],
                            dificuldade=dados["dificuldade"],
                            realizado=dados["realizado"]
                        )
                        self.cursos.append(curso)

                self.__cursoView.mostra_mensagem(f"{len(dados_curso)} cursos carregados com sucesso!")

            except Exception as e:
                print(e)

            

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
                self.cursos.append(curso)
                self.__cursoView.mostra_mensagem(f"O curso {dados_curso['nome']} foi cadastrado com sucesso \n")
                break  

            else:
                return

  

    def alterar_curso(self):
        nome = self.__cursoView.seleciona_curso()
        curso = None
        for c in self.cursos:
            if c.nome == nome:
                curso = c
                break

        if curso is None:
            self.__cursoView.mostra_mensagem(f"Curso com o nome {nome} não foi encontrado \n")
            
            

            

        elif curso is not None:
            novos_dados = self.__cursoView.pega_dados_curso()

            curso.nome = novos_dados["nome"]
            curso.nivel_requerido = novos_dados["nivel_requerido"]
            curso.xp_ganho = novos_dados["xp_ganho"]
            curso.setor = novos_dados["setor"]
            curso.dificuldade = novos_dados["dificuldade"]
            curso.realizado = novos_dados["realizado"]

            self.__cursoView.mostra_mensagem(f"O curso foi alterado com sucesso \n")
            time.sleep(0.2)



    def excluir_curso(self):
        nome = self.__cursoView.seleciona_curso()
        for c in self.cursos:
            if c.nome == nome:
                self.cursos.remove(c)
                self.__cursoView.mostra_mensagem(f"O curso {c.nome} foi removido com sucesso \n")
        time.sleep(0.2)



    def mostrar_cursos(self):
        cursos_dicionarios = self.to_dict()   
        self.__cursoView.mostra_cursos(cursos_dicionarios)



    def to_dict(self):
        return [
            {
                "nome": curso.nome,
                "nivel_requerido": curso.nivel_requerido,
                "xp_ganho": curso.xp_ganho,
                "setor": curso.setor,
                "dificuldade": curso.dificuldade,
                "realizado": curso.realizado,
            }
            for curso in self.cursos
        ]







