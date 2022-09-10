import pygameextra as pe
from pygameextra.fpslogger import Logger
from grid import *
from tile import *
import random
import checks

# Initiate the display
DDIM = 700
display_width, display_height = DIM, DIM
pe.init()
pe.display.make((display_width, display_height), "Wave Function Collapse")

# Initiate FPS log
log = Logger()

# Initiate the grid
DIM = 100
grid_width, grid_height = DIM, DIM
grid = Grid(grid_width, grid_height)


def load_image(file):
    return pe.Image(file, (display_width / grid_width, display_height / grid_height))

R=1
G=2
B=3

# Tiles
tiles = [
    TileObject(load_image("tiles/0.png"), [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],),
    # Green
    TileObject(load_image("tiles/1.png"), [0, G, 0], [0, G, 0], [0, 0, 0], [0, G, 0],),
    TileObject(load_image("tiles/2.png"), [0, G, 0], [0, G, 0], [0, G, 0], [0, 0, 0],),
    TileObject(load_image("tiles/3.png"), [0, 0, 0], [0, G, 0], [0, G, 0], [0, G, 0],),
    TileObject(load_image("tiles/4.png"), [0, G, 0], [0, 0, 0], [0, G, 0], [0, G, 0],),
    TileObject(load_image("tiles/5.png"), [0, G, 0], [0, G, 0], [0, G, 0], [0, G, 0],),
    TileObject(load_image("tiles/6.png"), [0, 0, 0], [0, G, 0], [0, 0, 0], [0, G, 0],),
    TileObject(load_image("tiles/7.png"), [0, G, 0], [0, 0, 0], [0, G, 0], [0, 0, 0],),
    # Green to blue
    TileObject(load_image("tiles/8.png"), [0, B, 0], [0, B, 0], [0, 0, 0], [0, G, 0],),
    TileObject(load_image("tiles/9.png"), [0, B, 0], [0, B, 0], [0, G, 0], [0, 0, 0],),
    TileObject(load_image("tiles/10.png"), [0, 0, 0], [0, G, 0], [0, B, 0], [0, B, 0],),
    TileObject(load_image("tiles/11.png"), [0, B, 0], [0, 0, 0], [0, G, 0], [0, B, 0],),
    TileObject(load_image("tiles/12.png"), [0, B, 0], [0, B, 0], [0, G, 0], [0, G, 0],),
    TileObject(load_image("tiles/13.png"), [0, 0, 0], [0, G, 0], [0, 0, 0], [0, B, 0],),
    TileObject(load_image("tiles/14.png"), [0, B, 0], [0, 0, 0], [0, G, 0], [0, 0, 0],),
    # Green to red
    TileObject(load_image("tiles/15.png"), [0, R, 0], [0, R, 0], [0, 0, 0], [0, G, 0],),
    TileObject(load_image("tiles/16.png"), [0, R, 0], [0, R, 0], [0, G, 0], [0, 0, 0],),
    TileObject(load_image("tiles/17.png"), [0, 0, 0], [0, G, 0], [0, R, 0], [0, R, 0],),
    TileObject(load_image("tiles/18.png"), [0, R, 0], [0, 0, 0], [0, G, 0], [0, R, 0],),
    TileObject(load_image("tiles/19.png"), [0, R, 0], [0, R, 0], [0, G, 0], [0, G, 0],),
    TileObject(load_image("tiles/20.png"), [0, 0, 0], [0, G, 0], [0, 0, 0], [0, R, 0],),
    TileObject(load_image("tiles/21.png"), [0, R, 0], [0, 0, 0], [0, G, 0], [0, 0, 0],),
    # Red
    TileObject(load_image("tiles/22.png"), [0, R, 0], [0, R, 0], [0, 0, 0], [0, R, 0],),
    TileObject(load_image("tiles/23.png"), [0, R, 0], [0, R, 0], [0, R, 0], [0, 0, 0],),
    TileObject(load_image("tiles/24.png"), [0, 0, 0], [0, R, 0], [0, R, 0], [0, R, 0],),
    TileObject(load_image("tiles/25.png"), [0, R, 0], [0, 0, 0], [0, R, 0], [0, R, 0],),
    TileObject(load_image("tiles/26.png"), [0, R, 0], [0, R, 0], [0, R, 0], [0, R, 0],),
    TileObject(load_image("tiles/27.png"), [0, 0, 0], [0, R, 0], [0, 0, 0], [0, R, 0],),
    TileObject(load_image("tiles/28.png"), [0, R, 0], [0, 0, 0], [0, R, 0], [0, 0, 0],),
    # Red to blue
    TileObject(load_image("tiles/29.png"), [0, B, 0], [0, B, 0], [0, 0, 0], [0, R, 0],),
    TileObject(load_image("tiles/30.png"), [0, B, 0], [0, B, 0], [0, R, 0], [0, 0, 0],),
    TileObject(load_image("tiles/31.png"), [0, 0, 0], [0, R, 0], [0, B, 0], [0, B, 0],),
    TileObject(load_image("tiles/32.png"), [0, B, 0], [0, 0, 0], [0, R, 0], [0, B, 0],),
    TileObject(load_image("tiles/33.png"), [0, B, 0], [0, B, 0], [0, R, 0], [0, R, 0],),
    TileObject(load_image("tiles/34.png"), [0, 0, 0], [0, R, 0], [0, 0, 0], [0, B, 0],),
    TileObject(load_image("tiles/35.png"), [0, B, 0], [0, 0, 0], [0, R, 0], [0, 0, 0],),
    # Red to green
    TileObject(load_image("tiles/36.png"), [0, G, 0], [0, G, 0], [0, 0, 0], [0, R, 0],),
    TileObject(load_image("tiles/37.png"), [0, G, 0], [0, G, 0], [0, R, 0], [0, 0, 0],),
    TileObject(load_image("tiles/38.png"), [0, 0, 0], [0, R, 0], [0, G, 0], [0, G, 0],),
    TileObject(load_image("tiles/39.png"), [0, G, 0], [0, 0, 0], [0, R, 0], [0, G, 0],),
    TileObject(load_image("tiles/40.png"), [0, G, 0], [0, G, 0], [0, R, 0], [0, R, 0],),
    TileObject(load_image("tiles/41.png"), [0, 0, 0], [0, R, 0], [0, 0, 0], [0, G, 0],),
    TileObject(load_image("tiles/42.png"), [0, G, 0], [0, 0, 0], [0, R, 0], [0, 0, 0],),
    # Blue
    TileObject(load_image("tiles/43.png"), [0, B, 0], [0, B, 0], [0, 0, 0], [0, B, 0],),
    TileObject(load_image("tiles/44.png"), [0, B, 0], [0, B, 0], [0, B, 0], [0, 0, 0],),
    TileObject(load_image("tiles/45.png"), [0, 0, 0], [0, B, 0], [0, B, 0], [0, B, 0],),
    TileObject(load_image("tiles/46.png"), [0, B, 0], [0, 0, 0], [0, B, 0], [0, B, 0],),
    TileObject(load_image("tiles/47.png"), [0, B, 0], [0, B, 0], [0, B, 0], [0, B, 0],),
    TileObject(load_image("tiles/48.png"), [0, 0, 0], [0, B, 0], [0, 0, 0], [0, B, 0],),
    TileObject(load_image("tiles/49.png"), [0, B, 0], [0, 0, 0], [0, B, 0], [0, 0, 0],),
    # Blue to red
    TileObject(load_image("tiles/50.png"), [0, R, 0], [0, R, 0], [0, 0, 0], [0, B, 0],),
    TileObject(load_image("tiles/51.png"), [0, R, 0], [0, R, 0], [0, B, 0], [0, 0, 0],),
    TileObject(load_image("tiles/52.png"), [0, 0, 0], [0, B, 0], [0, R, 0], [0, R, 0],),
    TileObject(load_image("tiles/53.png"), [0, R, 0], [0, 0, 0], [0, B, 0], [0, R, 0],),
    TileObject(load_image("tiles/54.png"), [0, R, 0], [0, R, 0], [0, B, 0], [0, B, 0],),
    TileObject(load_image("tiles/55.png"), [0, 0, 0], [0, B, 0], [0, 0, 0], [0, R, 0],),
    TileObject(load_image("tiles/56.png"), [0, R, 0], [0, 0, 0], [0, B, 0], [0, 0, 0],),
    # Blue to green
    TileObject(load_image("tiles/57.png"), [0, G, 0], [0, G, 0], [0, 0, 0], [0, B, 0],),
    TileObject(load_image("tiles/58.png"), [0, G, 0], [0, G, 0], [0, B, 0], [0, 0, 0],),
    TileObject(load_image("tiles/59.png"), [0, 0, 0], [0, B, 0], [0, G, 0], [0, G, 0],),
    TileObject(load_image("tiles/60.png"), [0, G, 0], [0, 0, 0], [0, B, 0], [0, G, 0],),
    TileObject(load_image("tiles/61.png"), [0, G, 0], [0, G, 0], [0, B, 0], [0, B, 0],),
    TileObject(load_image("tiles/62.png"), [0, 0, 0], [0, B, 0], [0, 0, 0], [0, G, 0],),
    TileObject(load_image("tiles/63.png"), [0, G, 0], [0, 0, 0], [0, B, 0], [0, 0, 0],),
]
checks.tiles = tiles

# Options of tiles
allOptions = list(range(0, len(tiles)))

# Fill the grid with all options
for x in range(grid_width):
    for y in range(grid_height):
        grid.set(x, y, GridObject(Tile(allOptions.copy()), grid))


def calculate_area(x_location, y_location):
    tile_width = display_width / grid_width
    tile_height = display_height / grid_height
    return x_location * tile_width, y_location * tile_height, tile_width, tile_height


def key(member):
    return len(member.value.options)  # Grab the amount of options for this member


pick_smallest_value = 0


def pick_smallest(member):
    global pick_smallest_value
    return (not member.value.collapsed) and len(member.value.options) <= pick_smallest_value


def pick_not_collapsed(member):
    return not member.value.collapsed


def readable(l):
    new = []
    for item in l:
        new.append(item.value.options)
    return new


def collapse():
    global pick_smallest_value
    grid_copy = grid.array.copy()
    grid_copy.sort(key=key, reverse=True)
    pick_smallest_value = len(grid_copy[0].value.options)
    smallest = list(filter(pick_smallest, grid_copy))
    if len(smallest) < 1:
        return
    pick = random.choice(smallest)
    pick.value.collapsed = True

    left = pick.left()
    right = pick.right()
    up = pick.up()
    down = pick.down()

    pick.value.options = allOptions.copy()

    if left and not left.value.collapsed:
        pick.value.options = checks.check_valid_options_left(pick.value.options, left.value.options[0])
    if right and not right.value.collapsed:
        pick.value.options = checks.check_valid_options_right(pick.value.options, right.value.options[0])
    if up and not up.value.collapsed:
        pick.value.options = checks.check_valid_options_up(pick.value.options, up.value.options[0])
    if down and not down.value.collapsed:
        pick.value.options = checks.check_valid_options_down(pick.value.options, down.value.options[0])

    if len(pick.value.options) > 0:
        pick.value.options = [random.choice(pick.value.options)]
    else:
        pick.value.options = [0]
    tiles[pick.value.options[0]].image.display(calculate_area(pick.x, pick.y))


was_pressed = False
finished = False
snake = None
pe.fill.full(pe.colors.black)


while True:
    finished = True
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()


    for x in range(grid_width):
        for y in range(grid_height):
            obj = grid.get(x, y)
            if not obj.value.collapsed:
                finished = False

    collapse()


    #log.render()
    pe.display.update()
