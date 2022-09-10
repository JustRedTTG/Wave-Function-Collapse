import pygameextra as pe
from pygameextra.fpslogger import Logger
from grid import *
from tile import *
import random
import checks

# Initiate the display
display_width, display_height = 700, 700
pe.init()
pe.display.make((display_width, display_height), "Wave Function Collapse")

# Initiate FPS log
log = Logger()

# Initiate the grid
DIM = 20
grid_width, grid_height = DIM, DIM
grid = Grid(grid_width, grid_height)


def load_image(file):
    return pe.Image(file, (display_width / grid_width, display_height / grid_height))


# Tiles
tiles = [
    TileObject(load_image("tiles/0.png"), [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0],),
    TileObject(load_image("tiles/1.png"), [0, 1, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0],),
    TileObject(load_image("tiles/2.png"), [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 0, 0],),
    TileObject(load_image("tiles/3.png"), [0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0],),
    TileObject(load_image("tiles/4.png"), [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 1, 0],),
    TileObject(load_image("tiles/5.png"), [0, 1, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0],),
    TileObject(load_image("tiles/6.png"), [0, 0, 0], [0, 1, 0], [0, 0, 0], [0, 1, 0],),
    TileObject(load_image("tiles/7.png"), [0, 1, 0], [0, 0, 0], [0, 1, 0], [0, 0, 0],),
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
        print("Couldn't find any:", smallest, readable(list(filter(pick_not_collapsed, grid_copy))))
        return
    pick = random.choice(smallest)
    pick.value.collapsed = True
    print(pick.value.options)

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



was_pressed = False


while True:
    for pe.event.c in pe.event.get():
        pe.event.quitcheckauto()
    pe.fill.full(pe.colors.black)

    for x in range(grid_width):
        for y in range(grid_height):
            obj = grid.get(x, y)
            if obj.value.collapsed:
                tiles[obj.value.options[0]].image.display(calculate_area(x, y))
            else:
                pe.draw.rect(pe.colors.white, calculate_area(x, y), 1)

    # if pe.mouse.clicked()[0] and not was_pressed:
    #     was_pressed = True
    collapse()
    # elif not pe.mouse.clicked()[0]:
    #     was_pressed = False


    log.render()
    pe.display.update(60)
