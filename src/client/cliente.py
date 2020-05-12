from src.grid.point import Point
from src.caminanteAleatorio.localizacion import Localizacion
from decimal import Decimal
import numpy as np
import random
import math
from src.consulta.consultaDeRango import ConsultaDeRango
from src.client.anonimizador import Anonimizador
import os
from src.client.almacen import Almacen
from src.consulta.consultaEncubierta import ConsultaEncubierta

class Usuario(object):
    CUES_USUARIOS = 7
    def __init__(self, name=None):
        self.numeroCues = 7
        self.oval = None
        self.speed = None
        self.consultaEncubierta = ConsultaEncubierta(self)
        self.anonimizador = None
        self.painter = None
        self.name = name
        self.point = Point()
        self.itemes = []
        self.randomWalk = None
        self.ovalQueryArea = []
        #self.consultasDeRango = []
        self.time = None
        self.almacenes = []


    def __str__(self):
        return str(self.name)

    def movement_probability(self, cardinalPointsProbability):
        self.cardinalPointsProbability = cardinalPointsProbability
        self.switchCardinal = {'Random':self._movement_probability_random, 'Uniforme':self._movement_probability_uniform,
                               'Direccion Predefinida': self._movement_predefinido,
                               'Uniforme Direccion Norte': self._movement_probability_uniform_north_direction,
                               'Uniforme Direccion Noroeste': self._movement_probability_uniform_northWest_direction,
                               'Uniforme Direccion Noreste': self._movement_probability_uniform_northEast_direction,
                               'Uniforme Direccion oeste':self._movement_probability_uniform_west_direction,
                               'Uniforme Direccion centro': self._movement_probability_uniform_center_direction,
                               'Uniforme Direccion este': self._movement_probability_uniform_east_direction,
                               'Uniforme Direccion suroeste': self._movement_probability_uniform_southWest_direction,
                               'Uniforme Direccion sur': self._movement_probability_uniform_south_direction,
                               'Uniforme Direccion sureste': self._movement_probability_uniform_southEast_direction,
                               'Uniforme Direccion 5split noroeste':self._movement_probability_uniform_northWest_direction,
                               'Uniforme Direccion 5split noreste': self._movement_probability_uniform_northEast_direction,
                               'Uniforme Direccion 5split suroeste': self._movement_probability_uniform_southWest_direction,
                               'Uniforme Direccion 5split sureste': self._movement_probability_uniform_southEast_direction,
                               'Uniforme Direccion 5split centro': self._movement_probability_uniform_center_direction
                               }
        self.switchCardinal[self.cardinalPointsProbability]()

    def _movement_predefinido(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)


    def _movement_probability_random(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)
                #self.randomWalk.probability.append(1/8)

    def _movement_probability_uniform(self):
        print 'movimiento uniforme'
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for _ in range(0, 8):
            self.randomWalk.probability.append(Decimal(1)/8)

    def  _movement_probability_uniform_north_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_northWest_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_northEast_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_west_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_center_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_east_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_southWest_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_south_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def _movement_probability_uniform_southEast_direction(self):
        self.randomWalk = Localizacion(self.point.pointX, self.point.pointY, self.time)
        for probability in np.random.dirichlet(np.ones(8), size=1):
            for x in probability:
                self.randomWalk.probability.append(x)

    def get_cell(self, grid):
        #print 'side cells : {}'.format(grid.cells[0].side)

        #print 'grid column: {}'.format(grid.width, self.point.pointX)
        #print 'user point: {},{}'.format(self.point.pointX, self.point.pointY)
        #print 'user in cell: {}'.format(int(math.floor(math.floor(self.point.pointX) / grid.cells[0].side) + (grid.width * math.floor(math.floor(self.point.pointY)/grid.cells[0].side))) )
        return grid.cells[int(math.floor(self.point.pointX / grid.cells[0].side) + (grid.width * math.floor(self.point.pointY/grid.cells[0].side)))]


    def obtener_consulta(self, grid):
        #EL CLIENTE, DECIDE SI GENERA UNA NUEVA CONSULTA
        #IEMPRE Y CUANDO LA ANTERIOR FUE COMPLETADA
        #EN UN DETERMINADO PORCENTAJE.

        if self._query_completed():
            if len(self.almacenes) < self.CUES_USUARIOS:
                self._generar_consulta(grid)


    def _generar_consulta(self, grid):
        cue=ConsultaEncubierta(self)
        cue.genetareCUETime = self.time.time
        #print 'Usuario: {} generando consulta'.format(self)

        cdr = ConsultaDeRango(self, grid, grid.cells[0].side * 2, cue)
        cdr.celdaDeUsuario = self.get_cell(grid)
        cdr.generar_consulta()

        anonimizador = Anonimizador(grid)
        anonimizador.cellOfUser = cdr.celdaDeUsuario
        cue.arriveInServer = False
        cue.consultas = anonimizador.anonimizar_consulta(self, cdr, cue)
        #se crea la consulta siempre y cuando contenga elementos de datos
        almacen = Almacen(cue, cue.consultas, grid)
        if len(almacen.elementosRequeridosReales)>0:
            self.consultaEncubierta = cue
            self.consultaDeRango = cdr
            self.almacenes.append(almacen)
            self.numeroCues -= 1




        #self.consultasDeRango.append(self.consultaDeRango)

        #os.system('pause')

    def is_waiting_response(self):
        print '-'*20
        print '{}'.format(self.almacenes[len(self.almacenes)-1].elementosRequeridosReales)
        print '{}'.format(self.almacenes[len(self.almacenes)-1].elementosEncontradosReales)
        print 'Server arrive query: {}'.format(self._server_arrive_query())
        print 'Query completed: {}'.format(self._query_completed())
        print 'Watch final of the schedule: {}'.format(self.consultaEncubierta.watchFinalSchedule)
        os.system('pause')

        if self._server_arrive_query():
            return True
        elif self._query_completed():
            return True
        elif self.consultaEncubierta.watchFinalSchedule == False:
            return True
        return False

    def _server_arrive_query(self):
        return self.consultaEncubierta.arriveInServer

    def _query_completed(self):
        if self.almacenes[len(self.almacenes)-1].is_completed():
            return True
        return False

    def observar_item(self, item):

        if len(self.almacenes)>0:
            if item.puntoDeInteres in self.almacenes[len(self.almacenes)-1].elementosRequeridosReales:
                if item.puntoDeInteres not in self.almacenes[len(self.almacenes)-1].elementosEncontradosReales:
                    self.almacenes[len(self.almacenes) - 1].elementosEncontradosReales.append(item.puntoDeInteres)
                    self.almacenes[len(self.almacenes) - 1].tiempoElementosEncontradosReales.append(self.time.time)
            if item.puntoDeInteres in self.almacenes[len(self.almacenes)-1].elementosRequeridosArtificiales:
                if item.puntoDeInteres not in self.almacenes[len(self.almacenes)-1].elementosEncontradosArtificiales:
                    self.almacenes[len(self.almacenes) - 1].elementosEncontradosArtificiales.append(item.puntoDeInteres)
                    self.almacenes[len(self.almacenes) - 1].tiempoElementosEncontradosArtificiales.append(self.time.time)


    def caminar(self, grid):
        #painter.canvas.move(self.oval, 1, 1)
        self.grid = grid
        self.switchCollision = {'Random': self._collision_probability_random, 'Uniforme': self._collision_probability_uniform,
                                'Direccion Predefinida': self._direccion_predefinida,
                                'Uniforme Direccion Norte': self._collision_probability_uniform_north_zone,
                                'Uniforme Direccion Noroeste':self._collision_probability_uniform_northWest_zone,
                                'Uniforme Direccion Noreste':self._collision_probability_uniform_northEast_zone,
                                'Uniforme Direccion oeste':self._collision_probability_uniform_west_zone,
                                'Uniforme Direccion centro':self._collision_probability_uniform_center_zone,
                                'Uniforme Direccion este': self._collision_probability_uniform_east_zone,
                                'Uniforme Direccion suroeste': self._collision_probability_uniform_southWest_zone,
                                'Uniforme Direccion sur': self._collision_probability_uniform_south_zone,
                                'Uniforme Direccion sureste': self._collision_probability_uniform_southEast_zone,
                                'Uniforme Direccion 5split noroeste': self._collision_probability_uniform_one_noroeste_zone,
                                'Uniforme Direccion 5split noreste': self._collision_probability_uniform_one_noreste_zone,
                                'Uniforme Direccion 5split suroeste': self._collision_probability_uniform_one_suroeste_zone,
                                'Uniforme Direccion 5split sureste': self._collision_probability_uniform_one_sureste_zone,
                                'Uniforme Direccion 5split centro': self._collision_probability_uniform_one_center_zone}
        self.switchCollision[self.cardinalPointsProbability]()

    def _direccion_predefinida(self):
        posicion = self.randomWalk.obtener_psicion_rastro()
        self.point.pointX = posicion[0]#posicion x
        self.point.pointY = posicion[1]#posicion y
        #self.painter.canvas.coords(self.oval, self.point.pointX - 2, self.point.pointY - 2, self.point.pointX + 2, self.point.pointY + 2)


    def _collision_probability_random(self):
        self.randomWalk.mover_cuatro_direcciones_colision_random(user=self, grid=self.grid)

    def _collision_probability_uniform(self):
        self.randomWalk.mover_cuatro_direcciones_colision_uniform(user=self, grid=self.grid)

    def _collision_probability_uniform_north_zone(self):
        #print 'Direccion Norte'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_north(user=self, grid=self.grid)

    def _collision_probability_uniform_northWest_zone(self):
        #print 'Direccion Noroeste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_northWest(user=self, grid=self.grid)

    def _collision_probability_uniform_northEast_zone(self):
        #print 'Direccion Noreste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_northEast(user=self, grid=self.grid)

    def _collision_probability_uniform_west_zone(self):
        #print 'Direccion oeste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_west(user=self, grid=self.grid)

    def _collision_probability_uniform_center_zone(self):
        #print 'Direccion central'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_center(user=self, grid=self.grid)

    def _collision_probability_uniform_east_zone(self):
        # print 'Direccion este'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_east(user=self, grid=self.grid)

    def _collision_probability_uniform_southWest_zone(self):
        # print 'Direccion suroeste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_southWest(user=self, grid=self.grid)

    def _collision_probability_uniform_south_zone(self):
        # print 'Direccion sur'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_south(user=self, grid=self.grid)

    def _collision_probability_uniform_southEast_zone(self):
        # print 'Direccion sureste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_southEast(user=self, grid=self.grid)

    def _collision_probability_uniform_one_noroeste_zone(self):
        # print 'Direccion sureste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_one_noroeste(user=self, grid=self.grid)

    def _collision_probability_uniform_one_noreste_zone(self):
        # print 'Direccion sureste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_one_noreste(user=self, grid=self.grid)

    def _collision_probability_uniform_one_suroeste_zone(self):
        # print 'Direccion sureste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_one_suroeste(user=self, grid=self.grid)

    def _collision_probability_uniform_one_sureste_zone(self):
        # print 'Direccion sureste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_one_sureste(user=self, grid=self.grid)
    def _collision_probability_uniform_one_center_zone(self):
        # print 'Direccion sureste'
        self.randomWalk.mover_cuatro_direcciones_colision_uniform_one_centro(user=self, grid=self.grid)

    def isNorthWest(self):
        return self.grid.collision_northWest(self.point.pointX, self.point.pointY)

    def isNorth(self):
        return self.grid.collision_north(self.point.pointX, self.point.pointY)

    def isNorthEast(self):
        return self.grid.collision_northEast(self.point.pointX, self.point.pointY)

    def isWest(self):
        return self.grid.collision_west(self.point.pointX, self.point.pointY)

    def isCenter(self):
        return self.grid.collision_center(self.point.pointX, self.point.pointY)

    def isEast(self):
        return self.grid.collision_east(self.point.pointX, self.point.pointY)

    def isSouthWest(self):
        return self.grid.collision_southWest(self.point.pointX, self.point.pointY)

    def isSouth(self):
        return self.grid.collision_south(self.point.pointX, self.point.pointY)

    def isSouthEast(self):
        return self.grid.collision_southEast(self.point.pointX, self.point.pointY)

    def is_one_noroeste(self):
        return self.grid.collision_one_split_five(self.point.pointX, self.point.pointY)

    def is_one_noreste(self):
        return self.grid.collision_two_split_five(self.point.pointX, self.point.pointY)

    def is_one_suroeste(self):
        return self.grid.collision_three_split_five(self.point.pointX, self.point.pointY)

    def is_one_sureste(self):
        return self.grid.collision_four_split_five(self.point.pointX, self.point.pointY)

    def is_one_center(self):
        return self.grid.collision_five_split_five(self.point.pointX, self.point.pointY)

    @property
    def point(self):
        return self.__point

    @point.setter
    def point(self, point):
        self.__point = point

    @property
    def oval(self):
        return self.__oval

    @oval.setter
    def oval(self, oval):
        self.__oval = oval

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def painter(self):
        return self.__painter

    @painter.setter
    def painter(self, painter):
        self.__painter = painter