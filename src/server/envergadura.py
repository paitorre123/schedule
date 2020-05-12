import random
from random import randint
from src.server.cronograma import Cronograma
import numpy as np
from decimal import Decimal
from src.server.clasificador import Clasificador
import math
from src.server.planificador import Planificador
from src.score.ScoreEnvergadura import ScoreEnvergadura
from src.ordenamiento.quicksort import QuickSort
from src.ordenamiento.probabilista import Probabilista
from src.truncado.truncado import TruncadorDeCronograma
from operator import attrgetter
import os
from src.manejoDeDatos.ManejoDeDatos import ManejoDeDatos

class Envergadura(Planificador):
    numeroRepeticiones = 10
    ajusteTemporal = True
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Planificador.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)

        ##elementos para la evaluacion
        self.evaluacionPorEnvergadura = []
        self.swithEnvergadura = {'Envergadura Determinista': self._cronograma_por_respuesta_mas_corta_determinista,
                                'Envergadura Probabilista': self._cronograma_por_respuesta_mas_corta_probabilista,
                                'Envergadura X Tiempo': self._cronograma_por_respuesta_mas_corta_probabilista_tiempo_espera}

    def activar_planificador(self, function, tipoPlanificacion):
        #print "'ORDENAR POR MENOR ENVERGADURA'"

        if self.ajusteTemporal:
            self._ajuste_temporal(function,  self.swithEnvergadura[tipoPlanificacion])
        else:
            self.ajuste.conAjuste = False
            self.ajuste.EFECTIVIDAD = 1
            self._ajuste_temporal(function,  self.swithEnvergadura[tipoPlanificacion])

    def _ajuste_temporal(self, functionSelectionCriteria, methodScheduler):
        for _ in self.consultasNuevas:
            self.ajuste.consultasNuevas.append(_)
        self.ajuste.iniciar_planificacion_ajustada(self, functionSelectionCriteria, methodScheduler)

    def _cronograma_por_respuesta_mas_corta_determinista(self):
        """
            en este primer ciclo se guarda
            la consulta encubierta en un
            objeto evaluador
        """
        ## atributo de la clase [atributo estatico, constante de la clase]
        print '::ENVERGADURA DETERMINISTA:::'
        ScoreEnvergadura.grid = self.grid
        for Q in self.consultasNuevas:
            s = ScoreEnvergadura(Q)
            self.evaluacionPorEnvergadura.append(s)

        """
            ordenar la lista de mayor a menor,
            ya que en el cronograma se pueden
            contestar mas consultas, mientras
            estas son de menor talla
        """

        QuickSort.menorAMayor(self.evaluacionPorEnvergadura, 0, len(self.evaluacionPorEnvergadura)-1)

        """
            ASIGNACION DE LOS ELEMENTOS DE 
            LAS CONSULTA ENCUBIERTAS, AL
            CRONOGRAMA.
        """
        self.cronograma.agregar_consulta_encubierta(self.evaluacionPorEnvergadura)
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
        if len(self.evaluacionPorEnvergadura)>self.cronograma.size:#si existen elementos pendientes
            #obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_envergadura(self.evaluacionPorEnvergadura[self.cronograma.size: len(self.evaluacionPorEnvergadura) ])



        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma




    def _cronograma_por_respuesta_mas_corta_probabilista(self, metodoCriterio):
        """
            en este primer ciclo se guarda
            la consulta encubierta en un
            objeto evaluador
        """
        ## atributo de la clase [atributo estatico, constante de la clase]
        print '::ENVERGADURA PROBABILISTA:::'
        ScoreEnvergadura.grid = self.grid
        for Q in self.consultasNuevas:
            s = ScoreEnvergadura(Q)
            self.evaluacionPorEnvergadura.append(s)

        scoreTotal = float(0)
        for s in self.evaluacionPorEnvergadura:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion

        # NORMALIZAR LAS PROBABILIDADES/score
        for s in self.evaluacionPorEnvergadura:
            s.normalizar(scoreTotal)

        conjuntoCronogramas = []
        for _ in range(0, self.numeroRepeticiones):
            #1. aplicar ordenamiento probabilista
            self.evaluacionPorEnvergadura = Probabilista.ordenarProbabilista(self.evaluacionPorEnvergadura)
            #2.asignar elementos de las consultas encubiertas al cronograma
            self.cronograma.agregar_consulta_encubierta(self.evaluacionPorEnvergadura)
            for __ in self.cronograma.items:
                self.cronograma.programa.append(__)
            # 2.1 asignar elemetos resultantes antes del truncado
            #self.ajuste.programaActual = self.cronograma.items
            #3. truncado del cronograma
            truncado = TruncadorDeCronograma(self.cronograma)
            truncado.truncar()
            # 3.1 asignar elementos pendientes
            #self.ajuste.cronogramaPendiente = truncado.elementosPendientes

            # 5. aplicar criterio de seleccion
            self.cronograma.puntos = metodoCriterio(self.cronograma, self.consultasNuevas, self)
            conjuntoCronogramas.append(self.cronograma)
            self.cronograma = Cronograma(self.sizeCronograma)

        # 6. seleccion del cronograma segun el criterio de seleccion
        if metodoCriterio.__name__ == 'criterio_por_stretch':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            ManejoDeDatos.escribir_valor_seleccion_cronograma(self.cronograma.puntos, len(self.cronograma.programa))
            print 'Menor criterio stretch es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_jitter':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            ManejoDeDatos.escribir_valor_seleccion_cronograma(self.cronograma.puntos, len(self.cronograma.programa))
            print 'Menor criterio jitter es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_carga_de_trabajo':
            self.cronograma = max(conjuntoCronogramas, key=attrgetter('puntos'))
            ManejoDeDatos.escribir_valor_seleccion_cronograma(self.cronograma.puntos, len(self.cronograma.programa))
            print 'Mayor criterio carcara de trabajo es: {}'.format(self.cronograma.puntos)

        self.ajuste.programaActual = self.cronograma.programa
        truncado = TruncadorDeCronograma(self.cronograma)
        truncado.truncar()
        self.ajuste.cronogramaPendiente = truncado.elementosPendientes

        # 4. extraccion de las consultas pendientes
        if len(self.evaluacionPorEnvergadura) > self.cronograma.size:
            self.consultasPendientes = truncado.obtener_consulta_pendientes_envergadura(
                self.evaluacionPorEnvergadura)

        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma

    def _cronograma_por_respuesta_mas_corta_probabilista_tiempo_espera(self, metodoCriterio):
        """
            en este primer ciclo se guarda
            la consulta encubierta en un
            objeto evaluador
        """
        ## atributo de la clase [atributo estatico, constante de la clase]

        print '::ENVERGADURA X TIEMPO:::'

        ScoreEnvergadura.grid = self.grid
        for Q in self.consultasNuevas:
            s = ScoreEnvergadura(Q)
            self.evaluacionPorEnvergadura.append(s)

        # NORMALIZAR LAS PROBABILIDADES/score
        scoreTotal = float(0)
        for s in self.evaluacionPorEnvergadura:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion

        # NORMALIZAR
        for s in self.evaluacionPorEnvergadura:
            s.normalizar(scoreTotal)

        # evaluacion del tiempo-1 de espera
        scoreTotalNormalConTiempo = float(0)
        for s in self.evaluacionPorEnvergadura:
            s.puntuacion = s.puntuacion * s.obtener_tiempo_espera_mayor(self.time)
            scoreTotalNormalConTiempo += s.puntuacion

        # NORMALIZAR LAS PROBABILIDADES/score
        for s in self.evaluacionPorEnvergadura:
            s.normalizar(scoreTotalNormalConTiempo)

        conjuntoCronogramas = []
        for _ in range(0, self.numeroRepeticiones):
            # 1. aplicar ordenamiento probabilista
            self.evaluacionPorEnvergadura = Probabilista.ordenarProbabilista(self.evaluacionPorEnvergadura)
            # 2.asignar elementos de las consultas encubiertas al cronograma
            self.cronograma.agregar_consulta_encubierta(self.evaluacionPorEnvergadura)
            for __ in self.cronograma.items:
                self.cronograma.programa.append(__)
            # 2.1 asignar elemetos resultantes antes del truncado
            #self.ajuste.programaActual = self.cronograma.items
            # 3. truncado del cronograma
            truncado = TruncadorDeCronograma(self.cronograma)
            truncado.truncar()
            # 3.1 asignar elementos pendientes
            #self.ajuste.cronogramaPendiente = truncado.elementosPendientes
            # 5. aplicar criterio de seleccion
            self.cronograma.puntos = metodoCriterio(self.cronograma, self.consultasNuevas, self)
            conjuntoCronogramas.append(self.cronograma)
            self.cronograma = Cronograma(self.sizeCronograma)

        # 6. seleccion del cronograma segun el criterio de seleccion
        if metodoCriterio.__name__ == 'criterio_por_stretch':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            ManejoDeDatos.escribir_valor_seleccion_cronograma(self.cronograma.puntos, len(self.cronograma.programa))
            print 'Menor criterio stretch es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_jitter':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            ManejoDeDatos.escribir_valor_seleccion_cronograma(self.cronograma.puntos, len(self.cronograma.programa))
            print 'Menor criterio jitter es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_carga_de_trabajo':
            self.cronograma = max(conjuntoCronogramas, key=attrgetter('puntos'))
            ManejoDeDatos.escribir_valor_seleccion_cronograma(self.cronograma.puntos, len(self.cronograma.programa))
            print 'Mayor criterio carcara de trabajo es: {}'.format(self.cronograma.puntos)

        self.ajuste.programaActual = self.cronograma.programa
        truncado = TruncadorDeCronograma(self.cronograma)
        truncado.truncar()
        self.ajuste.cronogramaPendiente = truncado.elementosPendientes

        # 4. extraccion de las consultas pendientes
        if len(self.evaluacionPorEnvergadura) > self.cronograma.size:
            self.consultasPendientes = truncado.obtener_consulta_pendientes_envergadura(
                self.evaluacionPorEnvergadura)




        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma