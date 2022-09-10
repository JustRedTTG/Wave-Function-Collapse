class Grid:
    width = 2
    height = 2
    length = 4
    array = []
    initiator = None

    def __init__(self, width, height, initiator: any = None):
        self.width = width
        self.height = height
        self.length = width * height
        self.array = [initiator] * self.length
        self.initiator = initiator

    def get(self, x, y):
        if x < 0 or y < 0 or x > self.width-1 or y > self.height-1:
            return None
        return self.array[x + (y * self.width)]

    def set(self, x, y, value):
        self.array[x + (y * self.width)] = value
        if type(value) == GridObject:
            value.x = x
            value.y = y


class GridObject:
    value = None
    grid = None
    x = 0
    y = 0

    def __init__(self, value, grid: Grid, x: int = 1, y: int = 1):
        self.value = value
        self.grid = grid
        self.x = x
        self.y = y

    def left(self):
        return self.grid.get(self.x-1, self.y)

    def right(self):
        return self.grid.get(self.x+1, self.y)

    def up(self):
        return self.grid.get(self.x, self.y-1)

    def down(self):
        return self.grid.get(self.x-1, self.y+1)
