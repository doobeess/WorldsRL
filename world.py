from game_map_2d import GameMap2D

from typing import Tuple

class World:
    def __init__(self, levels: Tuple[GameMap2D]):
        self.levels = levels