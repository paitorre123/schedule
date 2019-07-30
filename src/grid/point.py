

class Point(object):
    def __init__(self):
        self.pointX = 0.0
        self.pointY = 0.0

    @property
    def pointX(self):
        return self.__pointX

    @pointX.setter
    def pointX(self, point):
        self.__pointX = point

    @property
    def pointY(self):
        return self.__pointY

    @pointY.setter
    def pointY(self, point):
        self.__pointY = point
