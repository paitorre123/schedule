from src.grid.gridCell import Cell

class ConsultaDeRangoArtificial(Cell):
    def __init__(self, id, grid):
        Cell.__init__(self, id)
        self.tiempoLlegadaServidor = None
        self.grid = grid
