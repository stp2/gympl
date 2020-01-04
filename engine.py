from head import *
import sys
from handler import handle
from entity import MovableEntity

def border(x, y, dx, dy):
    """
    (původní x a y; změna)
    Hlídá hranice obrazovky.
    Pokud dojde k překročení vrátí (0, 0), jinak posun.
    """
    test = False # nedošlo k překročení hranic
    if x+dx < 0:
        test = True
    elif x+dx > (screen_width - 1): # indexuje se od 0
        test = True
    if y+dy < 0:
        test = True
    elif y+dy > (screen_height - 1): # indexuje se od 0
        test = True
    if test:
        return (0, 0)
    else:
        return (dx, dy)


if screen_width > t.width() or screen_height > t.height():
    t.close()
    print("Too small screen\nMust be 80x21")
    sys.exit(0)

run_app = True
player = MovableEntity(screen_width/2, screen_height/2, '@', termbox.BLACK)
while run_app:
    t.clear()
    t.change_cell(player.x, player.y, ord(player.char), player.color,  default_background)
    t.present()
    events = t.poll_event()
    change = handle(events)
    move = change.get('move')
    exit = change.get('exit')
    if move:
        dx, dy = move
        player.move(border(player.x, player.y, dx, dy))
    if exit:
        run_app = False
t.close()
