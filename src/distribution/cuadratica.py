from decimal import Decimal


class DistribucionCuadraticaCeldas(object):
    def __init__(self, numberUsers, cells):
        self.numberUsers = numberUsers
        self.cells = cells
        self.numberCells = len(cells)
        self.suma = Decimal((self.numberCells*(self.numberCells + 1) * (2 * self.numberCells + 1)) / 6)

    def getPointsUsers(self):
        # print 'Numero de celdas: {}'.format(self.__numberCells )
        i = 1
        for cell in self.cells:
            cell.probabilityToUsers = Decimal(pow(i, 2)) / Decimal(self.suma)
            i = i + 1
        # self.__printCells()
        return True

    def printCells(self):
        for cell in self.__cells:
            print "Celda: {}".format(cell)
            print "Punto A: {}, {}".format(cell.getPointA().getPointX(), cell.getPointA().getPointY())
            print "Punto B: {}, {}".format(cell.getPointB().getPointX(), cell.getPointB().getPointY())
            print "Punto C: {}, {}".format(cell.getPointC().getPointX(), cell.getPointC().getPointY())
            print "Punto D: {}, {}".format(cell.getPointD().getPointX(), cell.getPointD().getPointY())
            print "Probabilidad: {:.20E}".format(cell.getProbability())
