from decimal import Decimal


class DistribucionUniformeCeldas(object):
    def __init__(self, cells):
        self.cells = cells

    def getPointsUsers(self):
        print 'Numero de celdas: {}'.format(len(self.cells))
        print 'uniforme'
        for cell in self.cells:
            cell.probabilityToUsers = Decimal(1) / len(self.cells)
        # self.__printCells()
        return True

    def getPointsInterest(self):
        # print 'Numero de celdas: {}'.format(len(self.__cells))
        for cell in self.cells:
            cell.probabilityPointsInterest = Decimal(1) / len(self.cells)
        # self.__printCells()
        return True

    def _printCells(self):
        for cell in self.__cells:
            print "Celda: {}".format(cell)
            print "Punto A: {}, {}".format(cell.getPointA().getPointX(), cell.getPointA().getPointY())
            print "Punto B: {}, {}".format(cell.getPointB().getPointX(), cell.getPointB().getPointY())
            print "Punto C: {}, {}".format(cell.getPointC().getPointX(), cell.getPointC().getPointY())
            print "Punto D: {}, {}".format(cell.getPointD().getPointX(), cell.getPointD().getPointY())
            print "Probabilidad: {:.20E}".format(cell.getProbability())


