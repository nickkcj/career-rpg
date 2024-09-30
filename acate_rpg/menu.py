class Menu:
    def __init__(self, dungeons_conquistadas, cursos_realizados):
        self._dungeons_conquistadas = dungeons_conquistadas
        self._cursos_realizados = cursos_realizados

    @property
    def dungeons_conquistadas(self):
        return self._dungeons_conquistadas

    @dungeons_conquistadas.setter
    def dungeons_conquistadas(self, dungeons_conquistadas):
        self._dungeons_conquistadas = dungeons_conquistadas

    @property
    def cursos_realizados(self):
        return self._cursos_realizados

    @cursos_realizados.setter
    def cursos_realizados(self, cursos_realizados):
        self._cursos_realizados = cursos_realizados

    def listar_status(self, personagem):
        return f"{personagem.nome} - Nível: {personagem.nivel} - Experiência: {personagem.experiencia}"

    def listar_cursos(self):
        for curso in self._cursos_realizados:
            status = 'Realizado' if curso.realizado else 'Pendente'
            print(f"Curso: {curso.nome} - Setor: {curso.setor} - Status: {status}")

    def listar_dungeons(self):
        for dungeon in self._dungeons_conquistadas:
            status = 'Conquistada' if dungeon.conquistada else 'Não conquistada'
            print(f"Dungeon: {dungeon.nome} - Dificuldade: {dungeon.dificuldade} - Status: {status}")