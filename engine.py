from head import *
import sys
from handler import handle
from entity import MovableEntity
from render import render_all, clear_all, clear_map

def border(x, y, dx, dy):
    """
    (původní x a y; změna)
    Hlídá hranice obrazovky.
    Pokud dojde k překročení vrátí (0, 0), jinak posun.
    """
    test = False # nedošlo k překročení hranic
    if x+dx < 0:
        test = True
    elif x+dx >= (map_width): # indexuje se od 0
        test = True
    if y+dy < 0:
        test = True
    elif y+dy >= (map_height): # indexuje se od 0
        test = True
    if test:
        return (0, 0)
    else:
        return (dx, dy)


if screen_widht > t.width() or screen_height > t.height():
    t.close()
    print("Too small map\nMust be 80x21")
    sys.exit(0)

run_app = True
clear_map()
player = MovableEntity(map_width/2, map_height/2, '@', termbox.BLACK)
entities = [player]
while run_app:
    render_all(entities)
    t.present()
    events = t.poll_event()
    change = handle(events)
    move = change.get('move')
    exit = change.get('exit')
    clear_all(entities)
    if move:
        dx, dy = move
        player.move(border(player.x, player.y, dx, dy))
    if exit:
        run_app = False
t.close()
