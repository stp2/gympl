from head import *
from tile import Tile,tiles_dict
from random import randint

class GameMap:
    def __init__(self):
        self.tiles = self.initialize_tiles()

    def initialize_tiles(self):
        tiles = [[tiles_dict['rock'] for x in range(map_width)] for y in range(map_height)]

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
                self.tiles[y][x] = tiles_dict['floor']

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
            # space between rooms
            bigger = Rect(x-1, y-1, w+2, h+2)
            # run through the other rooms and see if they intersect with this one
            for other_room in rooms:
                if bigger.intersect(other_room):
                    break
            else:
                # this means there are no intersections, so this room is valid
                # "paint" it to the map's tiles
                self.createRoom(new_room)
                self.makeWalls(new_room) # wall is in room
                if numRooms == 0:
                    # this is the first room, where the player starts at
                    # no start at wall
                    player.x = randint(x+1, x+w-2)
                    player.y = randint(y+1, y+h-2)
                # finally, append the new room to the list
                rooms.append(new_room)
                numRooms += 1
        self.rooms = rooms

        # graf of exist corridors
        graph = [[False for i in rooms] for i in rooms]
        for i in range(len(rooms)):
            graph[i][i] = True
        i = -1
        for r in rooms:
            numCorridors = 0
            i += 1
            j = -1
            for cr in rooms:
                j += 1
                # same room
                if r == cr:
                    continue
                # too much corridors
                if numCorridors > randint(1, maxCoridorrs):
                    break
                # corridor exist
                if graph[i][j] == True:
                    continue

                # random coordinates of start tunnel
                (new_x, new_y) = (randint(r.x1, r.x2), randint(r.y1, r.y2))
                # try connect to another room, also random coordinates
                (prev_x, prev_y) = (randint(cr.x1, cr.x2), randint(cr.y1, cr.y2))
                # start to borders
                prev_x, prev_y = cr.border(new_x, new_y)
                new_x, new_y = r.border(prev_x, prev_y)

                # first move horizontally, then vertically
                cor = Rect(min(prev_x, new_x), new_y, abs(new_x-prev_x), 1)
                inter = False
                for through in rooms:
                    if cor.intersect(through):
                        inter = True
                        break
                cor = Rect(prev_x, min(prev_y, new_y), 1, abs(new_y-prev_y))
                for through in rooms:
                    if cor.intersect(through):
                        inter = True
                        break
                if not inter:
                    self.makeDoor(new_x, new_y)
                    self.makeDoor(prev_x, prev_y)
                    self.createHTunnel(prev_x, new_x, new_y)
                    self.createVTunnel(prev_y, new_y, prev_x)
                    graph[i][j] = True
                    graph[j][i] = True
                    numCorridors += 1
                # first move vertically, then horizontally
                else:
                    cor = Rect(min(prev_x, new_x), new_y, abs(new_x-prev_x), 1)
                    inter = False
                    for through in rooms:
                        if cor.intersect(through):
                            inter = True
                            break
                    cor = Rect(prev_x, min(prev_y, new_y), 1, abs(new_y-prev_y))
                    for through in rooms:
                        if cor.intersect(through):
                            inter = True
                            break
                    if not inter:
                        graph[i][j] = True
                        graph[j][i] = True
                        self.makeDoor(new_x, new_y)
                        self.makeDoor(prev_x, prev_y)
                        self.createVTunnel(prev_y, new_y, new_x)
                        self.createHTunnel(prev_x, new_x, prev_y)
                        numCorridors += 1

    def createHTunnel(self, x_from, x_to, y):
        for x in range(min(x_from, x_to), max(x_from, x_to)+1):
            self.tiles[y][x] = tiles_dict['corridor']

    def createVTunnel(self, y_from, y_to, x):
        for y in range(min(y_from, y_to), max(y_from, y_to)+1):
            self.tiles[y][x] = tiles_dict['corridor']

    def makeWalls(self, room):
        # make horizontal walls
        for i in range(room.x1, room.x2+1):
            self.tiles[room.y1][i] = tiles_dict['wallH']
            self.tiles[room.y2][i] = tiles_dict['wallH']
        # make vertical walls
        for i in range(room.y1+1, room.y2):
            self.tiles[i][room.x1] = tiles_dict['wallV']
            self.tiles[i][room.x2] = tiles_dict['wallV']

    def makeDoor(self, x, y):
        walls = (tiles_dict['wallV'], tiles_dict['wallH'])
        for coordinates in near(x, y):
            if self.tiles[coordinates[1]][coordinates[0]] in walls:
                self.tiles[coordinates[1]][coordinates[0]] = tiles_dict['door']

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

    def isIn(self, x, y):
        return x > self.x1 and x < self.x2 and y > self.y1 and y < self.y2

    def border(self, x, y):
        '''
        Call with another end.
        '''
        # x na kraj
        if x >= self.x1 and x <= self.x2: # druhé x mezi x1 a x2
            new_x = x
        elif x > self.x2: # druhé x vpravo
            new_x = self.x2
        else: #druhé x vlevo
            new_x = self.x1
        # y na kraj
        if y > self.y1 and y < self.y2: # y mezi
            new_y = y
        elif y > self.y2: # y dole
            new_y = self.y2-1
        else: # y nahoře
            new_y = self.y1+1
        # posun mimo místnost
        if x > self.x2:
            new_x += 1
        elif x < self.x1:
            new_x -= 1
        elif y > self.y2:
            new_y += 1
        else:
            new_y -= 1
        return new_x, new_y
