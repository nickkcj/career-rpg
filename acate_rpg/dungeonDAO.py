from dao import DAO
from dungeon import Dungeon

#cada entidade terá uma classe dessa, implementação bem simples.
class DungeonDAO(DAO):
    def __init__(self):
        super().__init__('dungeons.pkl')

    def add(self, dungeon: Dungeon):
        if((dungeon is not None) and isinstance(dungeon, Dungeon) and isinstance(dungeon.nome, str)):
            super().add(dungeon.nome, dungeon)

    def update(self, dungeon: Dungeon):
        if((dungeon is not None) and isinstance(dungeon, Dungeon) and isinstance(dungeon.nome, str)):
            super().update(dungeon.nome, dungeon)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(self, key:str):
        if(isinstance(key, str)):
            return super().remove(key)