from head import *

def render_all(t, entities):
    for ent in entities:
        draw_entity(t, ent)

def draw_entity(t, entity):
    t.change_cell(entity.x, entity.y, ord(entity.char), entity.color, default_background_color)

def clear_all(t, entities):
    for ent in entities:
        clear_entity(t, ent)

def clear_entity(t, entity):
    t.change_cell(entity.x, entity.y, ord(default_background_char), entity.color,  default_background_color)

def clear_map(t):
    for y in range(screen_height-1): # indexuje se od 0
        for x in range(screen_width-1):
            t.change_cell(x, y, ord(default_background_char), default_background_color, default_background_color)
