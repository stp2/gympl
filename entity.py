class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

class MovableEntity(Entity):
    """
    Movable objects.
    """
    def __init__(self, x, y, char, color):
        super().__init__(x, y, char, color)

    def move(self, move):
        dx, dy = move
        self.x += dx
        self.y += dy
