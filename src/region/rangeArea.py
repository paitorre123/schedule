from src.grid.gridCell import Cell

class CellRangeArea(Cell):
    def __init__(self, id):
        Cell.__init__(self, id)
        self.foundItems = []