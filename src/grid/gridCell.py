from src.grid.point import Point


class Cell(object):
    def __init__(self, id):
        self.id = id
        self.pointA = Point()
        self.pointB = Point()
        self.pointC = Point()
        self.pointD = Point()
        self.rectangle = None
        self.side = 0
        self.probabilityToUsers = 0.0
        self.probabilityPointsInterest = 0.0
        #self.users = [] #las celdas de una grilla no contienen al usuario
        self.pointsInterest = []

    def __str__(self):
        return str(self.id)

    def contain(self, x, y):
        #print 'Punto: {},{}'.format(x,y)

        if self._orient(self.pointB, self.pointA, x, y) < 0.0:
            #Oeste
            return False

        if self._orient(self.pointC, self.pointD, x, y) < 0.0:
            #Este
            return False

        if self._orient(self.pointA, self.pointC, x, y) < 0.0:
            #Norte
            return False

        if self._orient(self.pointD, self.pointB, x, y) < 0.0:
            #Sur
            return False

        return True

    def _orient(self, puntoA, puntoB, x, y):
        #print 'Celda[A][B]: {},{}-{},{}'.format(puntoA.pointX, puntoA.pointY, puntoB.pointX, puntoB.pointY)
        #print '{}'.format( ((puntoA.pointX-x)*(puntoB.pointY-y))-((puntoA.pointY-y)*(puntoB.pointX-x)))
        return ((puntoA.pointX-x)*(puntoB.pointY-y))-((puntoA.pointY-y)*(puntoB.pointX-x))


    def addPointsInterest(self, poi):
        self.pointsInterest.append(poi)


    def removePointsInterest(self, poi):
        self.pointsInterest.remove(poi)


    @property
    def pointA(self):
        return self.__pointA

    @pointA.setter
    def pointA(self, point):
        self.__pointA = point

    @property
    def pointB(self):
        return self.__pointB

    @pointB.setter
    def pointB(self, point):
        self.__pointB = point

    @property
    def pointC(self):
        return self.__pointC

    @pointC.setter
    def pointC(self, point):
        self.__pointC = point

    @property
    def pointD(self):
        return self.__pointD

    @pointD.setter
    def pointD(self, point):
        self.__pointD = point

    @property
    def probabilityToUsers(self):
        return self.__probabilityToUsers

    @probabilityToUsers.setter
    def probabilityToUsers(self, probability):
        self.__probabilityToUsers = probability

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, side):
        self.__side = side



