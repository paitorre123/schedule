import random
from random import randint
from src.server.cronograma import Cronograma
import numpy as np
from decimal import Decimal
from src.server.clasificador import Clasificador
import math
from src.server.planificador import Planificador
from src.score.scorePopularidad import ScorePopularidad
from src.ordenamiento.quicksort import QuickSort
from src.truncado.truncado import TruncadorDeCronograma
from src.ordenamiento.probabilista import Probabilista
from operator import attrgetter
import os
from src.manejoDeDatos.ManejoDeDatos import ManejoDeDatos


class Fifo(Planificador):
    ajusteTemporal = True
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Planificador.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)
        self.evaluacionPorFifo = []
        self.swithFifo = {'Fifo': self._cronograma_por_orden_de_llegada}

    def activar_planificador(self, function, tipoPlanificacion):
        #print "Palnificacion por Poluaridad"
        if self.ajusteTemporal:
            self._ajuste_temporal(function, self.swithFifo[tipoPlanificacion])
        else:
            self.ajuste.conAjuste = False
            self.ajuste.EFECTIVIDAD = 1
            self._ajuste_temporal(function, self.swithFifo[tipoPlanificacion])

    def _ajuste_temporal(self, functionSelectionCriteria, methodScheduler):
        for _ in self.consultasNuevas:
            self.ajuste.consultasNuevas.append(_)
        self.ajuste.iniciar_planificacion_ajustada(self, functionSelectionCriteria, methodScheduler)

    def _cronograma_por_orden_de_llegada(self):
        print "mostrar orden en que estan las CUEs en la cola de espera"
        for CUE in self.consultasNuevas:
            print CUE