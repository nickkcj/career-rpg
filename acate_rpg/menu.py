from personagem import Personagem
from dungeon import Dungeon
from curso import Curso


class Menu(Personagem, Dungeon, Curso):
    def __init__(self, personagem: Personagem, dungeon: Dungeon, curso: Curso):
        self.__personagem = personagem
        self.__dungeon = dungeon
        self.__curso = curso


    @property
    def personagem(self):
        return self.__personagem

    @personagem.setter
    def personagem(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    @property
    def dungeon(self):
        return self.__dungeon

    @dungeon.setter
    def dungeon(self, dungeon: Dungeon):
        if isinstance(dungeon, Dungeon):
            self.__dungeon = dungeon

    @property
    def curso(self):
        return self.__curso

    @curso.setter
    def curso(self, curso: Curso):
        if isinstance(curso, Curso):
            self.__curso = curso

    def listar_status(self):
        pass

    def listar_cursos(self):
        pass

    def listar_dungeons(self):
        pass

    