import numpy as np
import random
from src.client.cliente import Usuario
from src.grid.point import Point


class SeleccionDeLaMustraDeUsuarios(object):
    def __init__(self, numberUsers, grid, cells, time):
        self.numberUsers = numberUsers
        self.numberUser = 0
        self.cells = cells
        self.grid = grid
        self.dataCells = []
        self.probabilityCell = []
        self.time = time
        for cell in self.cells:
            self.dataCells.append(cell)
            self.probabilityCell.append(cell.probabilityToUsers)

    def distributeUsers(self, cardinalPointsProbability):
        #self.__printCells(cellDistribution)
        self.cardinalPointsProbability = cardinalPointsProbability
        for cell in self._selecRandomCell():
            # print "Celda: {}".format(i)
            # self.__printCell(cell)
            self._randomUserIn(cell)
            self.numberUser +=1

    def _printCells(self, cells):
        for cell in cells:
            print "Celda: {}".format(cell)
            print "Punto A: {}, {}".format(cell.getPointA().getPointX(), cell.getPointA().getPointY())
            print "Punto B: {}, {}".format(cell.getPointB().getPointX(), cell.getPointB().getPointY())
            print "Punto C: {}, {}".format(cell.getPointC().getPointX(), cell.getPointC().getPointY())
            print "Punto D: {}, {}".format(cell.getPointD().getPointX(), cell.getPointD().getPointY())
            print "Probabilidad: {:.20E}".format(cell.getProbability())

    def _randomUserIn(self, cell):
        x = random.uniform(cell.pointA.pointX+2, cell.pointD.pointX-2)
        y = random.uniform(cell.pointA.pointY+2, cell.pointD.pointY-2)
        u = Usuario()
        u.name = self.numberUser
        u.time = self.time
        p = Point()
        p.pointX = x
        p.pointY = y
        u.point = p
        u.movement_probability(self.cardinalPointsProbability)
        self.grid.addUser(u)
        #print 'Posicion Usuario: {},{}'.format(x,y)

    def _selecRandomCell(self):
        # EJEMPLO
        # https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.choice.html
        return np.random.choice(self.dataCells, self.numberUsers, p=self.probabilityCell)

    def _printCell(self, cell):
        print "Punto A: {}, {}".format(cell.getPointA().getPointX(), cell.getPointA().getPointY())
        print "Punto B: {}, {}".format(cell.getPointB().getPointX(), cell.getPointB().getPointY())
        print "Punto C: {}, {}".format(cell.getPointC().getPointX(), cell.getPointC().getPointY())
        print "Punto D: {}, {}".format(cell.getPointD().getPointX(), cell.getPointD().getPointY())
        print "Probabilidad: {:.20E}".format(cell.getProbability())