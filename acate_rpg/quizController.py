from quiz import Quiz
from quizView import QuizView

from cursoController import CursoController

class QuizController():
    def __init__(self):
        self.__quizes = []
        self.__quizView = QuizView()


    def responder(self):
        resposta = self.__quizView.pega_resposta()
        
    def realizar_quiz(self, gabarito):
        if not CursoController.__cursos:
            self.__quizView.mostra_mensagem("Não há cursos disponíveis para realizar o quiz")
            return
        
        self.__quizView.escolher_setor(self.__cursos)
        nome_curso = self.__quizView.seleciona_curso()

    