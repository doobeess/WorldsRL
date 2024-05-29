from creature import Creature
import color

class Deer(Creature):
    def __init__(self, x, y):
        super().__init__(x, y, "D", color.BROWN, 10, name="Deer", ai_type="neutral")
