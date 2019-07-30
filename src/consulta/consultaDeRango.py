from src.grid.gridCell import Cell
from src.grid.gridCell import Point
import os

class ConsultaDeRango(Cell):
    def __init__(self, user, grid, distance):
        Cell.__init__(self, 0)
        self.user = user
        self.grid = grid
        self.distance = distance
        self.celdaDeUsuario = None
        self.area = None
        self.tiempoLlegadaServidor = None

    def generar_consulta(self):
        self._calcular_perimetro()

    def _calcular_perimetro(self):
        self.side = distance = self.distance
        centerX = self.celdaDeUsuario.pointD.pointX - ((self.celdaDeUsuario.pointD.pointX - self.celdaDeUsuario.pointA.pointX) / 2)
        centerY = self.celdaDeUsuario.pointD.pointY - ((self.celdaDeUsuario.pointD.pointY - self.celdaDeUsuario.pointA.pointY) / 2)

        self.id = (centerX / self.side) + (self.grid.width * (centerY / self.side))


        point = Point()
        point.pointX = centerX
        point.pointY = centerY
        self.pointA = point
        point = Point()
        point.pointX = centerX
        point.pointY = centerY + distance
        self.pointB = point
        point = Point()
        point.pointX = centerX + distance
        point.pointY = centerY
        self.pointC = point
        point = Point()
        point.pointX = centerX + distance
        point.pointY = centerY + distance
        self.pointD = point

