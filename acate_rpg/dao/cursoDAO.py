from dao import DAO
from curso import Curso

#cada entidade terá uma classe dessa, implementação bem simples.
class CursoDAO(DAO):
    def __init__(self):
        super().__init__('cursos.pkl')

    def add(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.nome, str)):
            super().add(curso.nome, curso)

    def update(self, curso: Curso):
        if((curso is not None) and isinstance(curso, Curso) and isinstance(curso.nome, str)):
            super().update(curso.nome, curso)
            print(f"[DEBUG] Curso '{curso.nome}' atualizado no DAO.")

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)
    
    