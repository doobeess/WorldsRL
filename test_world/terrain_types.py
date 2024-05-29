from tile_types import new_tile
import color

long_grass = new_tile(
    walkable=True, transparent=False, dark=(ord("\""), color.DARK_TILE, (0, 0, 0)),
    light=(ord("\""), (22, 135, 33), (0, 0, 0)),
)

short_grass = new_tile(
    walkable=True, transparent=True, dark=(ord(","), color.DARK_TILE, (0, 0, 0)),
    light=(ord(","), (22, 135, 33), (0, 0, 0)), 
)

tree = new_tile(
    walkable=False, transparent=False, dark=(ord("4"), color.DARK_TILE, (0, 0, 0)),
    light=(ord("4"), (22, 135, 33), (0, 0, 0)), 
)