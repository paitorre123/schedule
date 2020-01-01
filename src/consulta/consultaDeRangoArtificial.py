from src.grid.gridCell import Cell

class ConsultaDeRangoArtificial(Cell):
    def __init__(self, id, grid, cue):
        Cell.__init__(self, id)
        self.tiempoLlegadaServidor = None
        self.grid = grid
        self.elementosRequeridos = []
        self.cueALaQuePertenece = cue

    def __str__(self):
        return '{}-{}'.format(str(self.id), self.cueALaQuePertenece )
