import random
import numpy as np
from src.puntoDeInteres.puntosDeInteres import PuntosDeInteres
from  src.grid.point import Point


class SeleccionDeLaMuestraDePuntosDeInteres(object):
    def __init__(self, numberPointsInteres, cells):
        self.numberPointsInteres = numberPointsInteres
        self.cells = cells
        self.dataCells = []
        self.probabilityCell = []
        self.id_poi = 0
        for cell in self.cells:
            self.dataCells.append(cell)
            self.probabilityCell.append(cell.probabilityPointsInterest)

    def distribute_points_interest(self):
        #self.__printCells(cellDistribution)
        for cell in self._selecRandomCell():
            # print "Celda: {}".format(i)
            # self.__printCell(cell)
            self._randomPointInteresIn(cell)
            self.id_poi+=1

    def _selecRandomCell(self):
        # EJEMPLO
        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html
        return np.random.choice(self.dataCells, self.numberPointsInteres, p=self.probabilityCell)

    def _randomPointInteresIn(self, cell):
        x = random.uniform(cell.pointA.pointX+2, cell.pointD.pointX-2)
        y = random.uniform(cell.pointA.pointY+2, cell.pointD.pointY-2)
        poi = PuntosDeInteres()
        poi.name = str(self.id_poi)
        p = Point()
        p.pointX = x
        p.pointY = y
        poi.point = p
        cell.addPointsInterest(poi)
        # rint 'Posicion Usuario: {},{}'.format(x,y)