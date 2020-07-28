from src.consulta.consultaDeRangoArtificial import ConsultaDeRangoArtificial
from src.region.rangeArea import CellRangeArea
from src.grid.gridCell import Cell
from src.grid.point import Point
import random
import xlsxwriter
import openpyxl


import os


class Anonimizador(object):
    ANONIMATO = 4

    def __init__(self, grid):
        self.grid = grid
        self.cellOfUser = None

    def anonimizar_consulta(self, user, consultaDeRango, cue):
        # EXTRAER DIMENSION DE LA CONSULTA
        # cellOfUser = user.get_cell(self.grid)
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

        # self.user.painter.canvas.create_rectangle(x0, y0, x1, y1)

        selectedCells = []
        # num_to_k = random.randint(2, 5)
        num_to_k = self.ANONIMATO - 1

        for cell in self.grid.cells:
            selectedCells.append(cell)

        selectedCells.remove(self.cellOfUser)
        listOfRandomCells = []

        datosceldas = []
        ncc = user.numeroCUESCreadas
        print user.CELDAS_CUES[ncc]
        for c in user.CELDAS_CUES[ncc]:
            # selecciona desde un  array un objeto por su id
            celda = next((x for x in selectedCells if x.id == c), None)
            if celda != None:
                listOfRandomCells.append(celda)
                datosceldas.append(c)
                # print "CELDA ENCONTRADA: {}".format(celda.id)

        # listOfRandomCells = random.sample(selectedCells, num_to_k)

        # print ":" * 20
        # print ":" * 20
        # print 'user: {}'.format(user)
        # print "CUES Creadas: {}".format(ncc)
        # print "celdas: {}".format(user.CELDAS_CUES[ncc])
        # print "selected cell: {}".format(datosceldas)
        # print "CUE: {}".format(user.numeroCUESCreadas+1)
        # print "k-anonimato: {}".format(self.ANONIMATO )
        # print "user cell: {}".format(self.cellOfUser.id)
        # for cell in listOfRandomCells:

        # print "virtual cell: {}".format(cell.id)

        # print ":" * 20
        # print ":" * 20
        # os.system('pause')
        # ManejoDeDatosCues.escribir_datos_celdas(user.numeroCUESCreadas+1, user.name+1,celdas)

        consultaEncubierta = []

        for cell in listOfRandomCells:
            # color = "#%02x%02x%02x" % (81, 27, 175)
            # self.user.painter.canvas.itemconfig(cell.rectangle, fill=color)

            centerX = cell.pointD.pointX - ((cell.pointD.pointX - cell.pointA.pointX) / 2)
            centerY = cell.pointD.pointY - ((cell.pointD.pointY - cell.pointA.pointY) / 2)

            id = (centerX / cell.side) + (self.grid.width * (centerY / cell.side))

            # print 'id: {}'.format(id)
            area = ConsultaDeRangoArtificial(id, self.grid, cue)
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
