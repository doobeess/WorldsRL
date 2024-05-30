from game_map_2d import GameMap2D

from .terrain_types import long_grass, short_grass, tree
from .item_types import Stick, Rock
from .creature_types import Deer

import numpy as np



def procgen(world_width, world_height):
    terrain_array = [short_grass]*10 + [long_grass, tree]
    items_list = []


    working_game_map = GameMap2D(
        width=world_width, height=world_height,
        tiles=np.array(
            [
                [np.random.choice(terrain_array) for i in range(world_height)]
            for i in range(world_width) ] 
        ),
        creatures=[
            Deer(np.random.randint(0,world_width), np.random.randint(0,world_height))
            for i in range(15)
        ]
    )

    for i in range(20):
        placed = False
        current_item = None
        while not placed:
            position = (np.random.randint(0, world_width), np.random.randint(0, world_height))
            current_item = np.random.choice([Stick(*position), Rock(*position)])
            if working_game_map.tiles["walkable"][current_item.x, current_item.y]:
                items_list.append(current_item)
                placed = True

    working_game_map.items = items_list

    return working_game_map
    
