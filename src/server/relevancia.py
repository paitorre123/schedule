import random
from random import randint
import numpy as np
from decimal import Decimal
from src.server.clasificador import Clasificador
import math
from src.server.planificador import Planificador
from src.score.scoreRelevancia import ScoreRelevancia
from src.ordenamiento.quicksort import QuickSort
from src.truncado.truncado import TruncadorDeCronograma
from src.ordenamiento.probabilista import Probabilista
from operator import attrgetter
from src.server.cronograma import Cronograma
from src.criterioDeSeleccion.criterio import Criterio



class Relevancia(Planificador):
    numeroRepeticiones = 20
    ajusteTemporal = True
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Planificador.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)
        self.evaluacionPorRelevancia = []
        self.swithRelavancia = {'Relevancia Determinista': self._cronograma_mayor_relevancia_determinista,
                                'Relevancia Probabilista': self._cronograma_mayor_relevancia_probabilista,
                                'Relevancia X Tiempo':self._cronograma_mayor_relevancia_probabilista_tiempo_espera}



    def activar_planificador(self, function, tipoPlanificacion):
        print "Planificacion por relevancia"
        if self.ajusteTemporal:
            print '{}'.format(tipoPlanificacion)
            self._ajuste_temporal(function,  self.swithRelavancia[tipoPlanificacion])
        else:
            self.ajuste.conAjuste = False
            self.ajuste.EFECTIVIDAD = 1
            self._ajuste_temporal(function,  self.swithRelavancia[tipoPlanificacion])



    def _ajuste_temporal(self, functionSelectionCriteria, methodScheduler):
        self.ajuste.consultasNuevas += self.consultasNuevas
        self.ajuste.iniciar_planificacion_ajustada(self, functionSelectionCriteria, methodScheduler)


    def _cronograma_mayor_relevancia_determinista(self):
        """
            en este primer ciclo se guarda
            el elemento, las subconsulas que
            lo contienen y las consultas encubiertas
            en un objeto evaluador
        """
        for Q in self.consultasNuevas:
            for q in Q.consultas:
                for e in self.obtener_elementos_desde_subconsulta(q):
                    my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorRelevancia)
                    if len(my_filter_iter) == 1:
                        my_filter_iter[0].agregar_score_subconsulta(Q,q)
                    if len(my_filter_iter) == 0:
                        s = ScoreRelevancia(e)
                        s.agregar_score_subconsulta(Q,q)
                        self.evaluacionPorRelevancia.append(s)

        for s in self.evaluacionPorRelevancia:
            s.obtener_score()

        """
            ordenar la lista de mayor a menor,
            ya que en el cronograma se pueden
            contestar consultas mas relevantes.
        """
        QuickSort.mayorAMenor(self.evaluacionPorRelevancia, 0, len(self.evaluacionPorRelevancia) - 1)

        """
            ASIGNACION DE LOS ELEMENTOS DE 
            LAS CONSULTA ENCUBIERTAS, AL
            CRONOGRAMA.
        """
        for e in self.evaluacionPorRelevancia:
            self.cronograma.items.append(e.elemento)
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
        if len(self.evaluacionPorRelevancia)>self.cronograma.size:#si existen elementos pendientes
            #obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_relevancia(self.evaluacionPorRelevancia[self.cronograma.size: len(self.evaluacionPorRelevancia) ])


        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma


    def _cronograma_mayor_relevancia_probabilista(self, metodoCriterio):
        """
            en este primer ciclo se guarda
            el elemento, las subconsulas que
            lo contienen y las consultas encubiertas
            en un objeto evaluador
        """
        for Q in self.consultasNuevas:
            for q in Q.consultas:
                for e in self.obtener_elementos_desde_subconsulta(q):
                    my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorRelevancia)
                    if len(my_filter_iter) == 1:
                        my_filter_iter[0].agregar_score_subconsulta(Q, q)
                    if len(my_filter_iter) == 0:
                        s = ScoreRelevancia(e)
                        s.agregar_score_subconsulta(Q, q)
                        self.evaluacionPorRelevancia.append(s)

        for s in self.evaluacionPorRelevancia:
            s.obtener_score()

        scoreTotal = float(0)
        for s in self.evaluacionPorRelevancia:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion

        # NORMALIZAR LAS PROBABILIDADES/score
        scoreTotalNormal = float(0)
        for s in self.evaluacionPorRelevancia:
            s.normalizar(scoreTotal)
            scoreTotalNormal += s.puntuacion

        conjuntoCronogramas = []
        for _ in range(0,self.numeroRepeticiones):
            # 1. ordenamiento probabilista
            self.evaluacionPorRelevancia = Probabilista.ordenarProbabilista(self.evaluacionPorRelevancia)
            # 2.asignacion de elementos
            for e in self.evaluacionPorRelevancia:
                self.cronograma.items.append(e.elemento)
            # 2.1 asignar elemetos resultantes antes del truncado
            self.ajuste.programaActual = self.cronograma.items
            # 3. truncado del programa
            truncado = TruncadorDeCronograma(self.cronograma)
            truncado.truncar()
            # 3.1 asignar elementos pendientes
            self.ajuste.cronogramaPendiente = truncado.elementosPendientes
            # 5. aplicacion del criterio de seleccion
            self.cronograma.puntos = metodoCriterio(self.cronograma, self.consultasNuevas, self)
            conjuntoCronogramas.append(self.cronograma)
            self.cronograma = Cronograma(self.sizeCronograma)

        #6. seleccion del cronograma segun el criterio de seleccion
        if metodoCriterio.__name__ == 'criterio_por_stretch':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio stretch es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_jitter':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio jitter es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_carga_de_trabajo':
            self.cronograma = max(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Mayor criterio carcara de trabajo es: {}'.format(self.cronograma.puntos)

        #4. seleccion de consultas pendiente
        if len(self.evaluacionPorRelevancia) > self.cronograma.size:  # si existen elementos pendientes
            # obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_relevancia(
                self.evaluacionPorRelevancia[self.cronograma.size: len(self.evaluacionPorRelevancia)])

        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma


    def _cronograma_mayor_relevancia_probabilista_tiempo_espera(self, metodoCriterio):
        """
            en este primer ciclo se guarda
            el elemento, las subconsulas que
            lo contienen y las consultas encubiertas
            en un objeto evaluador
        """
        for Q in self.consultasNuevas:
            for q in Q.consultas:
                for e in self.obtener_elementos_desde_subconsulta(q):
                    my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorRelevancia)
                    if len(my_filter_iter) == 1:
                        my_filter_iter[0].agregar_score_subconsulta(Q, q)
                    if len(my_filter_iter) == 0:
                        s = ScoreRelevancia(e)
                        s.agregar_score_subconsulta(Q, q)
                        self.evaluacionPorRelevancia.append(s)

        for s in self.evaluacionPorRelevancia:
            s.obtener_score()

        # NORMALIZAR LAS PROBABILIDADES/score
        scoreTotal = float(0)
        for s in self.evaluacionPorRelevancia:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion
        scoreTotalNormal = float(0)
        for s in self.evaluacionPorRelevancia:
            s.normalizar(scoreTotal)
            scoreTotalNormal += s.puntuacion

        # evaluacion del tiempo de espera
        for s in self.evaluacionPorRelevancia:
            s.puntuacion = s.puntuacion + s.obtener_tiempo_espera_mayor(self.time)

        # NORMALIZAR LAS PROBABILIDADES/score
        scoreTotal = float(0)
        for s in self.evaluacionPorRelevancia:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion
        scoreTotalNormal = float(0)
        for s in self.evaluacionPorRelevancia:
            s.normalizar(scoreTotal)
            scoreTotalNormal += s.puntuacion
        conjuntoCronogramas = []
        for _ in range(0, self.numeroRepeticiones):

            # 1. ordenamiento probabilista
            self.evaluacionPorRelevancia = Probabilista.ordenarProbabilista(self.evaluacionPorRelevancia)
            # 2.asignacion de elementos
            for e in self.evaluacionPorRelevancia:
                self.cronograma.items.append(e.elemento)
            #2.1 asignar elemetos resultantes antes del truncado
            self.ajuste.programaActual = self.cronograma.items
            # 3. truncado del programa
            truncado = TruncadorDeCronograma(self.cronograma)
            truncado.truncar()
            #3.1 asignar elementos pendientes
            self.ajuste.cronogramaPendiente = truncado.elementosPendientes

            # 5. aplicacion del criterio de seleccion
            self.cronograma.puntos = metodoCriterio(self.cronograma, self.consultasNuevas, self)
            conjuntoCronogramas.append(self.cronograma)
            self.cronograma = Cronograma(self.sizeCronograma)

        if metodoCriterio.__name__ == 'criterio_por_stretch':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio stretch es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_jitter':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio jitter es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_carga_de_trabajo':
            self.cronograma = max(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Mayor criterio carcara de trabajo es: {}'.format(self.cronograma.puntos)




        # 4. seleccion de consultas pendiente
        if len(self.evaluacionPorRelevancia) > self.cronograma.size:  # si existen elementos pendientes
            # obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_relevancia(
                self.evaluacionPorRelevancia[self.cronograma.size: len(self.evaluacionPorRelevancia)])

        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma
