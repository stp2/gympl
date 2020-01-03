import termbox
from handler import handle

t = termbox.Termbox()

screen_width = t.width()
screen_height = t.height()
player_x = screen_width//2
player_y = screen_height//2

t.clear()
t.change_cell(player_x,player_y, ord("@"), termbox.BLACK, termbox.WHITE)
t.present()

run_app = True
while run_app:
    events = t.poll_event()
    change = handle(events)
    move = change.get('move')
    exit = change.get('exit')
    if move:
        dx, dy = move
        player_x += dx
        player_y += dy
    if exit:
        run_app = False
    t.clear()
    t.change_cell(player_x,player_y, ord("@"), termbox.BLACK, termbox.WHITE)
    t.present()
t.close()
