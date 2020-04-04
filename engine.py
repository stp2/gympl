from head import *
import sys
from handler import handle
from entity import MovableEntity
from render import render_all, clear_all, clear_map
from map import GameMap
from fov import Fov

if screen_widht > t.width() or screen_height > t.height():
    t.close()
    print("Too small map\nMust be 80x21")
    sys.exit(0)

run_app = True
clear_map()
player = MovableEntity(0, 0, '@', termbox.BLACK)
entities = [player]
game_map = GameMap()
game_map.makeMap(player)
fov = Fov()
fov.compute(game_map, player.x, player.y)
while run_app:
    clear_map()
    render_all(entities, game_map, fov)
    t.set_cursor(player.x, player.y)
    t.present()
    events = t.poll_event()
    change = handle(events)
    move = change.get('move')
    exit = change.get('exit')
    clear_all(entities)
    if move:
        dx, dy = move
        if not game_map.isBlocked(player.x + dx, player.y + dy):
            player.move(move)
            fov.clear()
            fov.compute(game_map, player.x, player.y)
    if exit:
        run_app = False
t.close()
