import sys
import termbox
from handler import handle

t = termbox.Termbox()

# Nethack like size of map
screen_width = 80
screen_height = 21
if screen_width > t.width() or screen_height > t.height():
    t.close()
    print("Too small screen\nMust be 80x21")
    sys.exit(0)
player_x = screen_width//2
player_y = screen_height//2

t.clear()
t.change_cell(player_x,player_y, ord("@"), termbox.BLACK, termbox.WHITE)
t.present()

def border(x, y, dx, dy):
    """
    (původní x a y; změna)
    Hlídá hranice obrazovky.
    Pokud dojde k překročení vrátí původní souřadnice, jinak nové.
    """
    test = False
    if x+dx < 0:
        test = True
    elif x+dx > (screen_width - 1): # indexuje se od 0
        test = True
    if y+dy < 0:
        test = True
    elif y+dy > (screen_height - 1): # indexuje se od 0
        test = True
    if test:
        return (x, y)
    else:
        return (x+dx, y+dy)


run_app = True
while run_app:
    events = t.poll_event()
    change = handle(events)
    move = change.get('move')
    exit = change.get('exit')
    if move:
        dx, dy = move
        player_x, player_y = border(player_x, player_y, dx, dy)
    if exit:
        run_app = False
    t.clear()
    t.change_cell(player_x,player_y, ord("@"), termbox.BLACK, termbox.WHITE)
    t.present()
t.close()
