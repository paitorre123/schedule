from src.distribution.uniforme import DistribucionUniformeCeldas
from src.distribution.selectionPointsInterest import SeleccionDeLaMuestraDePuntosDeInteres

class ProbabilityPointsInterest(object):
    def __init__(self, numberPointsInterest, grid):
        self.numberPointsInterest = numberPointsInterest
        self.grid = grid
        self.swithDistribution = {'Uniforme': self._uniformePoints}

    def generateDistributionPointsInterest(self, distribution):
        self.swithDistribution[distribution]()

    def _uniformePoints(self):
       distribution = DistribucionUniformeCeldas(self.grid.cells)
       distribution.getPointsInterest()

    def distribute_points_interest(self):
        seleccion_muestra = SeleccionDeLaMuestraDePuntosDeInteres(self.numberPointsInterest, self.grid.cells)
        seleccion_muestra.distribute_points_interest()
        cantidad = 0
        for cell in self.grid.cells:
            cantidad+=len(cell.pointsInterest)
        #print 'Numero puntos de interes: {}'.format(cantidad)