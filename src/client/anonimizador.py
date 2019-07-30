from src.consulta.consultaDeRangoArtificial import ConsultaDeRangoArtificial
from src.region.rangeArea import CellRangeArea
from src.grid.gridCell import Cell
from src.grid.point import Point
import random

class Anonimizador(object):
    def __init__(self, grid):
        self.grid = grid
        self.cellOfUser = None


    def anonimizar_consulta(self, user, consultaDeRango):
        #EXTRAER DIMENSION DE LA CONSULTA
        #cellOfUser = user.get_cell(self.grid)
        radius = self.cellOfUser.side * 3

        x0 = user.point.pointX - radius
        y0 = user.point.pointY - radius
        x1 = user.point.pointX + radius
        y1 = user.point.pointY + radius

        cloackingRegion = Cell('Region de encubrimiento')
        point = Point()
        point.pointX = x0
        point.pointY = y0
        cloackingRegion.pointA = point
        point = Point()
        point.pointX = x0
        point.pointY = y1
        cloackingRegion.pointB = point
        point = Point()
        point.pointX = x1
        point.pointY = y0
        cloackingRegion.pointC = point
        point = Point()
        point.pointX = x1
        point.pointY = y1
        cloackingRegion.pointD = point

        #self.user.painter.canvas.create_rectangle(x0, y0, x1, y1)

        selectedCells = []
        #num_to_k = random.randint(2, 5)
        num_to_k = 3

        for cell in self.grid.cells:
            if cloackingRegion.contain(cell.pointA.pointX, cell.pointA.pointY) \
                    or cloackingRegion.contain(cell.pointB.pointX, cell.pointB.pointY)\
                    or cloackingRegion.contain(cell.pointC.pointX,cell.pointC.pointY) \
                    or cloackingRegion.contain(cell.pointD.pointX, cell.pointD.pointY):
                # color = "#%02x%02x%02x" % (216, 90, 90)
                # self.user.painter.canvas.itemconfig(cell.rectangle, fill=color)
                selectedCells.append(cell)

        selectedCells.remove(self.cellOfUser)

        list_of_random_items = random.sample(selectedCells, num_to_k)

        consultaEncubierta = []

        for cell in list_of_random_items:
            #color = "#%02x%02x%02x" % (81, 27, 175)
            #self.user.painter.canvas.itemconfig(cell.rectangle, fill=color)

            centerX = cell.pointD.pointX - ((cell.pointD.pointX - cell.pointA.pointX) / 2)
            centerY = cell.pointD.pointY - ((cell.pointD.pointY - cell.pointA.pointY) / 2)

            id = (centerX / cell.side) + (self.grid.width * (centerY / cell.side))

            #print 'id: {}'.format(id)
            area = ConsultaDeRangoArtificial(id, self.grid)
            point = Point()
            point.pointX = centerX
            point.pointY = centerY
            area.pointA = point
            point = Point()
            point.pointX = centerX
            point.pointY = centerY + consultaDeRango.distance
            area.pointB = point
            point = Point()
            point.pointX = centerX + consultaDeRango.distance
            point.pointY = centerY
            area.pointC = point
            point = Point()
            point.pointX = centerX + consultaDeRango.distance
            point.pointY = centerY + consultaDeRango.distance
            area.pointD = point
            consultaEncubierta.append(area)

        consultaEncubierta.append(consultaDeRango)
        return consultaEncubierta