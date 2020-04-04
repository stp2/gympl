from head import *
from tile import tiles_dict

class Fov():
    def __init__(self):
        self.map = [[False for x in range(map_width)] for y in range(map_height)]

    def clear(self):
        self.map = [[False for x in range(map_width)] for y in range(map_height)]

    def compute(self, map, x, y):
        if map.tiles[y][x].compare() == tiles_dict['corridor']: # Pokud v chodbě, dohled 1
            can = (tiles_dict['corridor'], tiles_dict['door']) # kam může vidět
            for coordinates in near(x, y): # dlaždice vedle
                if map.tiles[coordinates[1]][coordinates[0]].compare() in can:
                    self.map[coordinates[1]][coordinates[0]] = True
                    map.tiles[coordinates[1]][coordinates[0]].explored = True
        elif map.tiles[y][x].compare() == tiles_dict['door']: # ve dveřích vidí vedle a do místnosti
            for coordinates in near(x, y):
                if map.tiles[coordinates[1]][coordinates[0]].compare() == tiles_dict['corridor']:
                    self.map[coordinates[1]][coordinates[0]] = True
                    map.tiles[coordinates[1]][coordinates[0]].explored = True
                elif map.tiles[coordinates[1]][coordinates[0]].compare() == tiles_dict['floor']:
                    for r in map.rooms:
                        if r.isIn(coordinates[0], coordinates[1]):
                            for h in range(r.y1, r.y2+1):
                                for w in range(r.x1, r.x2+1):
                                    self.map[h][w] = True
                                    map.tiles[h][w].explored = True
        elif map.tiles[y][x].compare() == tiles_dict['floor']: # v místnosti ji vidí celou
            for r in map.rooms:
                if r.isIn(x, y):
                    for h in range(r.y1, r.y2+1):
                        for w in range(r.x1, r.x2+1):
                            self.map[h][w] = True
                            map.tiles[h][w].explored = True
        self.map[y][x] = True
        map.tiles[y][x].explored = True
