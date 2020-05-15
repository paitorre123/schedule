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
        """
                   en este primer ciclo se guarda
                   la consulta encubierta en un
                   objeto evaluador
               """
        ## atributo de la clase [atributo estatico, constante de la clase]
        """
        print "#" * 30
        for Q in self.consultasNuevas:
            sys.stdout.write("Q: "+str(Q)+" ->")
            for q in Q.consultas:
                for i in q.elementosRequeridos:
                    sys.stdout.write(" |"+ str(i))
            print ""
        print "#" * 30
        os.system('pause')
        """



        print '::: FIFO :::'
        ScoreFifo.grid = self.grid
        position = 1
        for Q in self.consultasNuevas:
            s = ScoreFifo(Q, position)
            position += 1
            self.evaluacionPorFifo.append(s)

        """
            ordenar la lista de mayor a menor,
            segun su orden de llegada
        """

        QuickSort.mayorAMenor(self.evaluacionPorFifo, 0, len(self.evaluacionPorFifo) - 1)

        """
            ASIGNACION DE LOS ELEMENTOS DE 
            LAS CONSULTA ENCUBIERTAS, AL
            CRONOGRAMA.
        """
        self.cronograma.agregar_consulta_encubierta(self.evaluacionPorFifo)
        for _ in self.cronograma.items:
            self.cronograma.programa.append(_)
        # 2.1 asignar elemetos resultantes antes del truncado
        self.ajuste.programaActual = self.cronograma.items



        """
            Truncado del cronograma.
            obteniendo la parte a tranmitir
            y la parte pendiente
        """
        truncado = TruncadorDeCronograma(self.cronograma)
        truncado.truncar()
        # 3.1 asignar elementos pendientes
        self.ajuste.cronogramaPendiente = truncado.elementosPendientes
        """
            Obtener las consultas pendiente
            correspondientes. A partir de la
            parte del cronograma que  esta
            pendiente.
        """
        if len(self.evaluacionPorFifo) > self.cronograma.size:  # si existen elementos pendientes
            # obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_envergadura(
                self.evaluacionPorFifo[self.cronograma.size: len(self.evaluacionPorFifo)])

        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []



        return self.cronograma