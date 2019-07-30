from decimal import Decimal


class DistribucionZipfCeldas(object):
    def __init__(self, numberUsers, cells, zipf):
        self.numberUsers = numberUsers
        self.cells = cells
        self.zipf = zipf
        self.numberCells = len(cells)
        self.suma = 0
        self._prepararSuma()

    def _prepararSuma(self):
        for x in range(1, self.numberCells+1):
            self.suma = Decimal(self.suma  + self.numberCells / pow(x, self.zipf))

    def getPointsUsers(self):
        # print 'Numero de celdas: {}'.format(len(self.__cells))
        i = 0
        for cell in self.cells:
            cell.probabilityToUsers = Decimal((self.numberCells / (pow((i + 1), self.zipf))) / self.suma)
            i = i + 1
        # self._printCells()
        return True

    def _printCells(self):
        for cell in self.__cells:
            print "Celda: {}".format(cell)
            print "Punto A: {}, {}".format(cell.getPointA().getPointX(), cell.getPointA().getPointY())
            print "Punto B: {}, {}".format(cell.getPointB().getPointX(), cell.getPointB().getPointY())
            print "Punto C: {}, {}".format(cell.getPointC().getPointX(), cell.getPointC().getPointY())
            print "Punto D: {}, {}".format(cell.getPointD().getPointX(), cell.getPointD().getPointY())
            print "Probabilidad: {:.20E}".format(cell.getProbability())


