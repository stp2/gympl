from head import *

class Tile:
    """
    A tile on a map. It may or may not be blocked, and may or may not block sight.
    """
    entities = []
    def __init__(self, id):
        self.id = id
        self.char = tiles_dict[id][0]
        self.color = tiles_dict[id][1]
        self.blocked = tiles_dict[id][2]
        self.block_sight = tiles_dict[id][3]
        self.explored = False

tiles_dict = {
        'floor' : ('.', termbox.BLACK, False, False),
        'rock' : (' ', termbox.WHITE, True, True),
        'corridor' : ('#', termbox.BLACK, False, False),
        'door' : ('+', termbox.YELLOW, False, False),
        'wallH' : ('-', termbox.BLACK, True, True),
        'wallV' : ('|', termbox.BLACK, True, True)
}
