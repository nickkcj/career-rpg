from curso import Curso
from cursoView import CursoView

class CursoController():
    def __init__(self):
        self.cursos = []
        self.__cursoView = CursoView()

    def cadastrar_curso(self):
        dados_curso = self.__cursoView.pega_dados_curso()
        curso = Curso(dados_curso["nome"], dados_curso["nivel_requerido"], dados_curso["xp_ganho"], dados_curso["setor"], dados_curso["dificuldade"], dados_curso["realizado"])
        self.cursos.append(curso)
        self.__cursoView.mostra_mensagem(f"O curso {dados_curso["nome"]} foi cadastrado com sucesso \n")


    def alterar_curso(self):
        self.__cursoView.mostra_cursos(self.cursos)
        nome = self.__cursoView.seleciona_curso()
        curso = None
        for c in self.cursos:
            if c.nome == nome:
                curso = c
                break

        if curso is None:
            self.__cursoView.mostra_mensagem(f"Curso com o nome {nome} não foi encontrado \n")


        novos_dados = self.__cursoView.pega_dados_curso()

        curso.nome = novos_dados["nome"]
        curso.nivel_requerido = novos_dados["nivel_requerido"]
        curso.xp_ganho = novos_dados["xp_ganho"]
        curso.setor = novos_dados["setor"]
        curso.dificuldade = novos_dados["dificuldade"]
        curso.realizado = novos_dados["realizado"]

        self.__cursoView.mostra_mensagem(f"O curso foi alterado com sucesso \n")


    def excluir_curso(self):
        self.__cursoView.mostra_cursos(self.__cursos)
        nome = self.__cursoView.seleciona_curso()
        curso = None
        for c in self.cursos:
            if c.nome == nome:
                self.cursos.remove(c)
        self.__cursoView.mostra_mensagem(f"O curso {c.nome} foi removido com sucesso \n")

