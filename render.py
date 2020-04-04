from head import *

def render_all(entities, game_map, fov):
    """
    Draw all objects to map.
    """
    for y in range(map_height):
        for x in range(map_width):
            if fov.map[y][x] or game_map.tiles[y][x].explored:
                t.change_cell(x, y, ord(game_map.tiles[y][x].char), game_map.tiles[y][x].color, default_background_color)
    for ent in entities:
        draw_entity(ent)

def draw_entity(entity):
    t.change_cell(entity.x, entity.y, ord(entity.char), entity.color, default_background_color)

def clear_all(entities):
    for ent in entities:
        clear_entity(ent)

def clear_entity(entity):
    t.change_cell(entity.x, entity.y, ord(default_background_char), entity.color,  default_background_color)

def clear_map():
    for y in range(map_height):
        for x in range(map_width):
            t.change_cell(x, y, ord(default_background_char), default_background_color, default_background_color)
