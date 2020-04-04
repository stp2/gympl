from head import *

class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """
    entities = []
    def __init__(self, char, color, blocked, block_sight=None):
        self.char = char
        self.color = color
        self.blocked = blocked
        self.explored = False

        # By default, if a tile is blocked, it also blocks sight
        if block_sight is None:
            block_sight = blocked

        self.block_sight = block_sight

    def compare(self):
        return (self.char, self.color, self.blocked, self.block_sight)

tiles_dict = {
        'floor' : Tile('.', termbox.BLACK, False).compare(),
        'rock' : Tile(' ', termbox.WHITE, True).compare(),
        'corridor' : Tile('#', termbox.BLACK, False).compare(),
        'door' : Tile('+', termbox.YELLOW, False).compare(),
        'wallH' : Tile('-', termbox.BLACK, True).compare(),
        'wallV' : Tile('|', termbox.BLACK, True).compare()
}
