from pygameextra.image import Image
class Tile:
    collapsed = False
    options = []

    def __init__(self, options):
        self.collapsed = False
        self.options = options


class TileObject:
    left_side = []
    right_side = []
    up_side = []
    down_side = []
    image = None

    def __init__(self, image: Image, u, r, d, l):
        self.image = image
        self.left_side = l
        self.right_side = r
        self.up_side = u
        self.down_side = d
