import termbox

def handle(events):
    (type, ch, key, mod, w, h, x, y) = events
    if type == termbox.EVENT_KEY:
        if key == termbox.KEY_ESC:
            return {'exit':True}
        elif ch == 'h':
            return {'move':(-1,0)}
        elif ch == 'j':
            return {'move':(0,+1)}
        elif ch == 'k':
            return {'move':(0,-1)}
        elif ch == 'l':
            return {'move':(+1,0)}
        elif ch == 'u':
            return {'move':(+1,-1)}
        elif ch == 'n':
            return {'move':(+1,+1)}
        elif ch == 'b':
            return {'move':(-1,+1)}
        elif ch == 'y':
            return {'move':(-1,-1)}
    return {}
