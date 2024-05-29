from item import Item
import color

class Stick(Item):
    def __init__(self,x,y):
        super().__init__(x,y,"/",color.BROWN,name="stick")