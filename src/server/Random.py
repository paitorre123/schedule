import random
from random import randint
from src.server.cronograma import Cronograma
import numpy as np
from decimal import Decimal
from src.server.clasificador import Clasificador
import math
from src.server.planificador import Planificador
from src.score.ScoreFifo import ScoreFifo
from src.ordenamiento.quicksort import QuickSort
from src.truncado.truncado import TruncadorDeCronograma
from src.ordenamiento.probabilista import Probabilista
from operator import attrgetter
import os
from src.manejoDeDatos.ManejoDeDatos import ManejoDeDatos
import sys
from src.server.Fifo import Fifo


class Random(Fifo):
    ajusteTemporal = False
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Fifo.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)


        self.swithRandom = {'Random': self._cronograma_aleatorio}

    def activar_planificador(self, function, tipoPlanificacion):
        #print "Palnificacion por Poluaridad"
        if self.ajusteTemporal:
            self._ajuste_temporal(function, self.swithRandom[tipoPlanificacion])
        else:
            self.ajuste.conAjuste = False
            self.ajuste.EFECTIVIDAD = 1
            self._ajuste_temporal(function, self.swithRandom[tipoPlanificacion])


    def _cronograma_aleatorio(self):
        self._cronograma_por_orden_de_llegada()
        for i in range(0, 10):
            random.shuffle(self.cronograma.items)
        return self.cronograma

    def _swap_random(self):
        idx = range(len(self.cronograma.items))
        i1, i2 = random.sample(idx, 2)
        self.cronograma.items[i1], self.cronograma.items[i2] = self.cronograma.items[i2], self.cronograma.items[i1]