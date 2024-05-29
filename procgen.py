import numpy

def generate_map(width, height, maptype="basic"):
    GameMap2D = numpy.array(width, height, str)
    GameMap2D.fill(".")
    return GameMap2D
