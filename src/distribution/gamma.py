from decimal import Decimal
from math import expm1


class DistribucionGammaCeldas(object):
    def __init__(self, numberUsers, cells):
        self.numberUsers = numberUsers
        self.cells = cells
        self.numberCells = len(cells)
        self.switchGamma = {'Beta=2.0, Alfa=2.0':self._distributeBeta2Alfa2Cells, 'Beta=9.0, Alfa=2.0':self._distributeBeta9Alfa2Cells,
                              'Beta=7.0, Alfa=3.0': self._distributeBeta7Alfa3Cells}

    def getPointsUsers(self, beta):
        return self.switchGamma[beta]()

    def _distributeBeta2Alfa2Cells(self):
        #print 'Numero de celdas: {}'.format(len(self.__cells))
        suma = float(0.0)
        E = float(0.0)
        for i in range(1, self.numberCells+1):
            E = -1*((float(i) )/2.0)
            suma = suma + float(0.25)* float(i) *expm1(E)

        i = 1
        for cell in self.cells:
            i_ = Decimal(i)
            E = -1 *((float(i) )/2.0)
            cell.probabilityToUsers =  (float(0.25)*float(i_)*expm1(E))/suma
            i = i + 1
        #self.__printCells()
        return True

    def _distributeBeta9Alfa2Cells(self):
        suma = float(0.0)
        E = float(0.0)
        for i in range(1, self.numberCells + 1):
            E = -1 * ((float(i)) / 9.0)
            suma = suma + float(0.012345) * float(i) * expm1(E)

        i = 1
        for cell in self.cells:
            i_ = Decimal(i)
            E = -1 * ((float(i)) / 9.0)
            cell.probabilityToUsers = (float(0.012345) * float(i_) * expm1(E)) / suma
            i = i + 1
        # self._printCells()
        return True

    def _distributeBeta7Alfa3Cells(self):
        suma = float(0.0)
        E = float(0.0)
        for i in range(1, self.numberCells + 1):
            E = -1 * ((float(i)) / 7.0)
            suma = suma + float(0.001457) * float(i) * expm1(E)

        i = 1
        for cell in self.cells:
            i_ = Decimal(i)
            E = -1 * ((float(i)) / 7.0)
            cell.probabilityToUsers = (float(0.001457) * float(i_) * expm1(E)) / suma
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