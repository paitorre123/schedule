from src.distribution.uniforme import DistribucionUniformeCeldas
from src.distribution.cuadratica import DistribucionCuadraticaCeldas
from src.distribution.zipf import DistribucionZipfCeldas
from src.distribution.selectionUsers import SeleccionDeLaMustraDeUsuarios
from src.distribution.gamma import DistribucionGammaCeldas
from src.distribution.exponencial import DistribucionExponencialCeldas


class ProbabilityUsers(object):
    def __init__(self, numberUsers, grid, time):
        self.numberUsers = numberUsers
        self.grid = grid
        self.time = time
        self.swithDistributionCell = {'Uniforme':self.uniformeCell, 'Cuadratica':self.quadraticCell, 'Zipf, S=2':self.zipf2,
                                    'Zipf, S=3':self.zipf3, 'Zipf, S=4':self.zipf4,
                                    'Gamma Beta=2 y Alfa=2.0=K':self.gammaBeta2Alfa2Cell, 'Gamma  Beta=9 y Alfa=2.0=K':self.gammaBeta9Alfa2Cell,
                                    'Gamma  Beta=7 y Alfa=3.0=K':self.gammaBeta7Alfa3Cell,'Exponencial, Lambda=0.5':self.exponencial05Cell,
                                    'Exponencial, Lambda=1.0':self.exponencial10Cell, 'Exponencial, Lambda=1.5':self.exponencial15Cell}

    def generateDistributionCells(self, distribution):
        self.swithDistributionCell[distribution]()

    def uniformeCell(self):
        distri_unifome = DistribucionUniformeCeldas(cells=self.grid.cells)
        distri_unifome.getPointsUsers()

    def quadraticCell(self):
        distri_cuadratica = DistribucionCuadraticaCeldas(self.numberUsers, self.grid.cells)
        distri_cuadratica.getPointsUsers()

    def zipf2(self):
        distri_zipf2 = DistribucionZipfCeldas(self.numberUsers, self.grid.cells, 2)
        distri_zipf2.getPointsUsers()

    def zipf3(self):
        distri_zipf3 = DistribucionZipfCeldas(self.numberUsers, self.grid.cells, 3)
        distri_zipf3.getPointsUsers()

    def zipf4(self):
        distri_zipf4 = DistribucionZipfCeldas(self.numberUsers, self.grid.cells, 4)
        distri_zipf4.getPointsUsers()

    def gammaBeta2Alfa2Cell(self):
        distri_gamma2 = DistribucionGammaCeldas(self.numberUsers, self.grid.cells)
        distri_gamma2.getPointsUsers('Beta=2.0, Alfa=2.0')

    def gammaBeta9Alfa2Cell(self):
        distri_gamma2 = DistribucionGammaCeldas(self.numberUsers, self.grid.cells)
        distri_gamma2.getPointsUsers('Beta=9.0, Alfa=2.0')

    def gammaBeta7Alfa3Cell(self):
        distri_gamma2 = DistribucionGammaCeldas(self.numberUsers, self.grid.cells)
        distri_gamma2.getPointsUsers('Beta=7.0, Alfa=3.0')

    def exponencial05Cell(self):
        distr_exponencial05 = DistribucionExponencialCeldas(self.numberUsers, self.grid.cells, 0.5)
        distr_exponencial05.getPointsUsers()

    def exponencial10Cell(self):
        distr_exponencial10 = DistribucionExponencialCeldas(self.numberUsers, self.grid.cells, 1.0)
        distr_exponencial10.getPointsUsers()

    def exponencial15Cell(self):
        distr_exponencial15 = DistribucionExponencialCeldas(self.numberUsers, self.grid.cells, 1.5)
        distr_exponencial15.getPointsUsers()

    def generateDistributionUser(self, cardinalPointsProbability):
        seleccion_muestra = SeleccionDeLaMustraDeUsuarios(self.numberUsers, self.grid, self.grid.cells, self.time)
        seleccion_muestra.distributeUsers(cardinalPointsProbability)


    @property
    def numberUsers(self):
        return self.__numberUsers

    @numberUsers.setter
    def numberUsers(self, numberUsers):
        self.__numberUsers = numberUsers

    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, grid):
        self.__grid = grid

    @property
    def swithDistributionCell(self):
        return self.__swithDistributionCell

    @swithDistributionCell.setter
    def swithDistributionCell(self, swithDistributionCell):
        self.__swithDistributionCell = swithDistributionCell
