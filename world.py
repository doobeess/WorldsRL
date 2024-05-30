from game_map_2d import GameMap2D

from typing import List

class World:
    def __init__(self, levels: List[GameMap2D]):
        self.levels = levels