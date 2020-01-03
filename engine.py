import termbox

screen_width = 80
screen_height = 21
player_x = screen_width//2
player_y = screen_height//2

t = termbox.Termbox()
t.clear()

t.change_cell(player_x,player_y, ord("@"), termbox.BLACK, termbox.WHITE)
t.present()

run_app = True
while run_app:
    events = t.poll_event()
    while events:
        (type, ch, key, mod, w, h, x, y) = events
        if type == termbox.EVENT_KEY and key == termbox.KEY_ESC:
            run_app = False
        events = t.peek_event()
    t.close()
