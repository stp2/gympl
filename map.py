from head import *
from tile import Tile

class GameMap:
    def __init__(self):
        self.floor = Tile('.', termbox.BLACK, False)
        self.wall = Tile('#', termbox.BLUE, True)
        self.rock = Tile(' ', termbox.WHITE, True)
        self.corridor = Tile('#', termbox.BLACK, False)
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[self.rock for x in range(map_width)] for y in range(map_height)]

        return tiles

    def isBlocked(self, x, y):
        x = int(x)
        y = int(y)
        test = False
        # nejsem mimo mapu
        if x < 0:
            test = True
        elif x >= (map_width): # indexuje se od 0
            test = True
        if y < 0:
            test = True
        elif y >= (map_height): # indexuje se od 0
            test = True
        # pokud jsem mimo mapu nemé cenu kontrolovat zeď, navíc bych byl mimo list
        if test:
            return True
        # je zeď
        if self.tiles[y][x].blocked == True:
            test = True
        return test

    def createRoom(self, room):
        for y in range(room.y1, room.y2):
            for x in range(room.x1, room.x2):
                self.tiles[y][x] = self.floor

    def makeMap(self):
        room1 = Rect(2, 3, 5, 7)
        room2 = Rect(60, 15, 10, 5)

        self.createRoom(room1)
        self.createRoom(room2)
        self.createHTunnel(7, 62, 5)
        self.createVTunnel(5, 15, 62)

    def createHTunnel(self, x_from, x_to, y):
        for x in range(min(x_from, x_to), max(x_from, x_to)):
            self.tiles[y][x] = self.corridor

    def createVTunnel(self, y_from, y_to, x):
        for y in range(min(y_from, y_to), max(y_from, y_to)):
            self.tiles[y][x] = self.corridor

class Rect():
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h
