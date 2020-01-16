from head import *
from tile import Tile
from random import randint

class GameMap:
    def __init__(self):
        self.floor = Tile('.', termbox.BLACK, False)
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
        # pokud jsem mimo mapu nemá cenu kontrolovat zeď, navíc bych byl mimo list
        if test:
            return True
        # je zeď
        if self.tiles[y][x].blocked == True:
            test = True
        return test

    def createRoom(self, room):
        for y in range(room.y1, room.y2+1):
            for x in range(room.x1, room.x2+1):
                self.tiles[y][x] = self.floor

    def makeMap(self, player):
        rooms = []
        numRooms = 0

        for i in range(maxRooms):
            # random width and height
            w = randint(roomMinSize, roomMaxSize)
            h = randint(roomMinSize, roomMaxSize)
            # random position without going out of the boundaries of the map
            x = randint(0, map_width - w)
            y = randint(0, map_height - h)
             # "Rect" class makes rectangles easier to work with
            new_room = Rect(x, y, w, h)
            # run through the other rooms and see if they intersect with this one
            for other_room in rooms:
                if new_room.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid
                # "paint" it to the map's tiles
                self.createRoom(new_room)
                (new_x, new_y) = (randint(new_room.x1, new_room.x2), randint(new_room.y1, new_room.y2))
                # center coordinates of new room, will be useful later
                if numRooms == 0:
                    # this is the first room, where the player starts at
                    player.x = randint(x, x+w-1)
                    player.y = randint(y, y+h-1)
                else:
                    # all rooms after the first:
                    # connect it to the previous room with a tunnel
                    (prev_x, prev_y) = (randint(rooms[numRooms-1].x1, rooms[numRooms-1].x2), randint(rooms[numRooms-1].y1, rooms[numRooms-1].y2))
                    prev_x, prev_y = rooms[numRooms-1].border(new_x, new_y)

                    new_x, new_y = new_room.border(prev_x, prev_y)
                    # flip a coin (random number that is either 0 or 1)
                    if randint(0, 1) == 1:
                        # first move horizontally, then vertically
                        self.createHTunnel(prev_x, new_x, prev_y)
                        self.createVTunnel(prev_y, new_y, new_x)
                    else:
                        # first move vertically, then horizontally
                        self.createVTunnel(prev_y, new_y, prev_x)
                        self.createHTunnel(prev_x, new_x, new_y)

                # finally, append the new room to the list
                rooms.append(new_room)
                numRooms += 1

    def createHTunnel(self, x_from, x_to, y):
        for x in range(min(x_from, x_to), max(x_from, x_to)+1):
            self.tiles[y][x] = self.corridor

    def createVTunnel(self, y_from, y_to, x):
        for y in range(min(y_from, y_to), max(y_from, y_to)+1):
            self.tiles[y][x] = self.corridor

class Rect():
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w -1
        self.y2 = y + h -1

    def intersect(self, other):
        # returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

    def border(self, x, y):
        # x na kraj
        if x >= self.x1 and x <= self.x2:
            new_x = x
        elif x > self.x2:
            new_x = self.x2
        else:
            new_x = self.x1
        # y na kraj
        if y >= self.y1 and y <= self.y2:
            new_y = y
        elif y > self.y2:
            new_y = self.y2
        else:
            new_y = self.y1
        # posun mimo místnost
        # rohové pozice
        if (new_x == self.x1 or new_x == self.x2) and (new_y == self.y1 or new_y == self.y2):
            if randint(0, 1) % 2 == 0:
                if x > self.x2:
                    new_x += 1
                else:
                    new_x -= 1
            else:
                if y > self.y2:
                    new_y += 1
                else:
                    new_y -= 1
        # hranové pozice
        else:
            if x > self.x2:
                new_x += 1
            else:
                new_x -= 1
            if y > self.y2:
                new_y += 1
            else:
                new_y -= 1
        return new_x, new_y
