from decimal import Decimal
from math import expm1
import numpy as np


class DistribucionExponencialCeldas(object):
    def __init__(self, numberUsers, cells, exponente):
        self.numberUsers = numberUsers
        self.cells = cells
        self.exponente = exponente
        self.numberCells = len(cells)

    def getPointsUsers(self):
        suma = float(0.0)
        E = float(0.0)
        for i in range(1, self.numberCells + 1):
            E = ((float(i)) * self.exponente)
            suma = suma + float(self.exponente) * expm1(E)

        # print 'Numero de celdas: {}'.format(len(self.__cells))
        i = 1
        for cell in self.cells:
            i_ = float(i)
            E = self.exponente * i_
            cell.probabilityToUsers = Decimal((self.exponente * expm1(E)) / suma)
            i = i + 1
        # self.__printCells()
        return True

    def _printCells(self):
        for cell in self.__cells:
            print "Celda: {}".format(cell)
            print "Punto A: {}, {}".format(cell.pointA.getPointX(), cell.pointA().getPointY())
            print "Punto B: {}, {}".format(cell.pointB.getPointX(), cell.pointB().getPointY())
            print "Punto C: {}, {}".format(cell.pointC.getPointX(), cell.pointC().getPointY())
            print "Punto D: {}, {}".format(cell.pointD.getPointX(), cell.pointD().getPointY())
            print "Probabilidad: {:.20E}".format(cell.getProbability())