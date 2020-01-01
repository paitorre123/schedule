from src.grid.point import Point
from src.consulta.elemento import Elemento

class PuntosDeInteres(object):
    def __init__(self):
        self.name = None
        self.rectangle = None
        self.point = Point()
        self.dato = Elemento(self)

    def __str__(self):
        return self.name

    def paintPointsOfInterest(self, canvas):
        x1, y1 = (int(self.point.pointX) - 2), (int(self.point.pointY) - 2)
        x2, y2 = (int(self.point.pointX) + 2), (int(self.point.pointY) + 2)
        # print "Position: {},{}".format(event.x, event.y)
        #colorRectangle = "#%02x%02x%02x" % (255, 36, 36)
        #self.rectangle = canvas.create_rectangle(x1, y1, x2, y2, fill=colorRectangle, tags='poi')