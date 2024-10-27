from curso import Curso
from cursoView import CursoView
from excecoes import NivelRequeridoInvalidoError, SetorInvalidoError, DificuldadeInvalidaError, XpGanhoInvalidoError
class CursoController():
    def __init__(self):
        self.cursos = []
        self.__cursoView = CursoView()

    def cadastrar_curso(self):
        while True:  
            erros = []  
            dados_curso = self.__cursoView.pega_dados_curso()
            try:
                if not dados_curso["xp_ganho"].isdigit():  
                    raise XpGanhoInvalidoError("O XP ganho deve ser um número inteiro.")
                dados_curso["xp_ganho"] = int(dados_curso["xp_ganho"])
            except XpGanhoInvalidoError as e:
                erros.append(str(e))

            
            try:
                if not dados_curso["nivel_requerido"].isdigit():  
                    raise NivelRequeridoInvalidoError("O nível requerido deve ser um número inteiro entre 1 e 10.")
                dados_curso["nivel_requerido"] = int(dados_curso["nivel_requerido"])
                if not (1 <= dados_curso["nivel_requerido"] <= 10):
                    raise NivelRequeridoInvalidoError("O nível requerido deve ser um número entre 1 e 10.")
            except NivelRequeridoInvalidoError as e:
                erros.append(str(e))

            
            setores_validos = ["RH", "T.I", "Vendas", "Marketing", "Financeiro"]
            try:
                if dados_curso.get("setor") not in setores_validos:
                    raise SetorInvalidoError(f"O setor deve ser um dos seguintes: {', '.join(setores_validos)}.")
            except SetorInvalidoError as e:
                erros.append(str(e))

            
            try:
                if not dados_curso["dificuldade"].isdigit():  
                    raise DificuldadeInvalidaError("A dificuldade deve ser um número inteiro entre 1 e 10.")
                dados_curso["dificuldade"] = int(dados_curso["dificuldade"])
                if not (1 <= dados_curso["dificuldade"] <= 10):
                    raise DificuldadeInvalidaError("A dificuldade deve ser um número entre 1 e 10.")
            except DificuldadeInvalidaError as e:
                erros.append(str(e))

            
            if erros:
                mensagem_erro = "Erros ao cadastrar curso:\n" + "\n".join(erros)
                self.__cursoView.mostra_mensagem(mensagem_erro)
            else:
                
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
        self.__cursoView.mostra_cursos(self.cursos)
        nome = self.__cursoView.seleciona_curso()
        curso = None
        for c in self.cursos:
            if c.nome == nome:
                self.cursos.remove(c)
        self.__cursoView.mostra_mensagem(f"O curso {c.nome} foi removido com sucesso \n")


    def mostrar_cursos(self):
        self.__cursoView.mostra_cursos(self.cursos)



