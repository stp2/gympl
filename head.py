import termbox

default_background_color = termbox.WHITE
default_background_char = ' '

#init termbox
t = termbox.Termbox()
t.clear()
# Nethack like size of map
map_width = 80
map_height = 21
screen_widht = 80
screen_height = 24
roomMaxSize = 14
roomMinSize = 4
maxRooms = 6
maxCoridorrs = 3

def near(x, y):
    return ((x-1,y),(x+1,y),(x,y-1),(x,y+1))
