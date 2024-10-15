from curso import Curso
from cursoView import CursoView

class CursoController():
    def __init__(self):
        self.__cursos = []
        self.__cursoView = CursoView()

    def cadastrar_curso(self):
        dados_curso = self.__cursoView.pega_dados_curso()
        curso = Curso(dados_curso["nome"], dados_curso["nivel_requerido"], dados_curso["xp_ganho"], dados_curso["setor"], dados_curso["dificuldade"], dados_curso["realizado"])
        self.__cursos.append(curso)
        self.__cursoView.mostra_mensagem(f"O curso {dados_curso["nome"]} foi cadastrado com sucesso")