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


class Popularidad(Planificador):
    numeroRepeticiones = 20
    ajusteTemporal = True
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Planificador.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)
        self.evaluacionPorPopularidad = []
        self.swithPopularidad= {'Popularidad Determinista': self._cronograma_por_mayor_popularidad_determinista,
                                'Popularidad Probabilista': self._cronograma_por_mayor_popularidad_probabilista,
                                'Popularidad X Tiempo': self._cronograma_por_mayor_popularidad_probabilista_tiempo_espera}


    def activar_planificador(self, function, tipoPlanificacion):
        print "Palnificacion por Poluaridad"

        if self.ajusteTemporal:
            self._ajuste_temporal(function, self.swithPopularidad[tipoPlanificacion])
        else:
            self.ajuste.conAjuste = False
            self.ajuste.EFECTIVIDAD = 1
            self._ajuste_temporal(function, self.swithPopularidad[tipoPlanificacion])

    def _ajuste_temporal(self, functionSelectionCriteria, methodScheduler):
        self.ajuste.consultasNuevas += self.consultasNuevas
        self.ajuste.iniciar_planificacion_ajustada(self, functionSelectionCriteria, methodScheduler)

    def _cronograma_por_mayor_popularidad_determinista(self):
        """
            en este primer ciclo se guarda
            el elemento y las consultas encubiertas
            en un objeto evaluador
        """
        #
        ScorePopularidad.grid = self.grid
        for Q in self.consultasNuevas:
            for e in self.obtener_elementos_desde_consulta_encubierta(Q):
                #comprobacion de que el elemento no se repita en el evaluador
                my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorPopularidad)
                if len(my_filter_iter)==1:
                    my_filter_iter[0].agregar_consulta(Q)
                if len(my_filter_iter)==0:
                    s = ScorePopularidad(e)
                    s.agregar_consulta(Q)
                    self.evaluacionPorPopularidad.append(s)

        for s in self.evaluacionPorPopularidad:
            s.obtener_score()

        """
            ordenar la lista de mayor a menor,
            ya que en el cronograma se pueden
            contestar consultas mas usadas.
        """
        QuickSort.mayorAMenor(self.evaluacionPorPopularidad, 0, len(self.evaluacionPorPopularidad) - 1)

        """
            ASIGNACION DE LOS ELEMENTOS DE 
            LAS CONSULTA ENCUBIERTAS, AL
            CRONOGRAMA.
        """
        # 2.1 asignar elemetos resultantes antes del truncado
        self.ajuste.programaActual = self.cronograma.items

        """
            Truncado del cronograma.
            obteniendo la parte a tranmitir
            y la parte pendiente
        """

        for e in self.cronograma.items:
            self.elementosProgramaCompleto.append(e)

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

        if len(self.evaluacionPorPopularidad)>self.cronograma.size:#si existen elementos pendientes
            #obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_popularidad(self.evaluacionPorPopularidad[self.cronograma.size: len(self.evaluacionPorPopularidad) ])


        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma

    def _cronograma_por_mayor_popularidad_probabilista(self, metodoCriterio):
        """
            en este primer ciclo se guarda
            el elemento y las consultas encubiertas
            en un objeto evaluador
        """
        ScorePopularidad.grid = self.grid
        for Q in self.consultasNuevas:
            for e in self.obtener_elementos_desde_consulta_encubierta(Q):
                # comprobacion de que el elemento no se repita en el evaluador
                my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorPopularidad)
                if len(my_filter_iter) == 1: #si el elemento se repite en el evaluador solo guarda la consulta
                    my_filter_iter[0].agregar_consulta(Q)
                if len(my_filter_iter) == 0:#se el elemento no esta en el evaluados se guarda el elemento y la consulta
                    s = ScorePopularidad(e)
                    s.agregar_consulta(Q)
                    self.evaluacionPorPopularidad.append(s)

        for s in self.evaluacionPorPopularidad:
            s.obtener_score()

        scoreTotal = float(0)
        for s in self.evaluacionPorPopularidad:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion

        #NORMALIZAR LAS PROBABILIDADES/score
        scoreTotalNormal = float(0)
        for s in self.evaluacionPorPopularidad:
            s.normalizar(scoreTotal)
            scoreTotalNormal += s.puntuacion


        """
            En este ciclo se ordenan de forma 
            probabilista los elementos de datos
            Durante un determinado numero de 
            repeticiones se selecciona el 
            cronograma truncado segun 
            alguno de los reiterios de seleccion:
            1. Carga de trabajo
            2. Stretch
            3. Jitter
        """
        conjuntoCronogramas = []
        for _ in range(0, self.numeroRepeticiones):
            # 1. Seleccion de orden probabilista
            self.evaluacionPorPopularidad = Probabilista.ordenarProbabilista(self.evaluacionPorPopularidad)
            # 2. Asignar elementos en el cronograma
            for e in self.evaluacionPorPopularidad:
                if e not in self.cronograma.items:
                    self.cronograma.items.append(e.elemento)
            # 2.1 asignar elemetos resultantes antes del truncado
            self.ajuste.programaActual = self.cronograma.items
            # 3. Truncar el cronograma
            truncado = TruncadorDeCronograma(self.cronograma)
            truncado.truncar()
            # 3.1 asignar elementos pendientes
            self.ajuste.cronogramaPendiente = truncado.elementosPendientes
            # 5. aplicar criterio de seleccion
            self.cronograma.puntos = metodoCriterio(self.cronograma, self.consultasNuevas, self)
            conjuntoCronogramas.append(self.cronograma)
            self.cronograma = Cronograma(self.sizeCronograma)

        # 6. seleccion del cronograma segun el criterio de seleccion
        if metodoCriterio.__name__ == 'criterio_por_stretch':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio stretch es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_jitter':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio jitter es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_carga_de_trabajo':
            self.cronograma = max(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Mayor criterio carcara de trabajo es: {}'.format(self.cronograma.puntos)

        # 4. obtener las consultas pendientes
        if len(self.evaluacionPorPopularidad) > self.cronograma.size:  # si existen elementos pendientes
            # obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_popularidad(
                self.evaluacionPorPopularidad[self.cronograma.size: len(self.evaluacionPorPopularidad)])


        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma

    def _cronograma_por_mayor_popularidad_probabilista_tiempo_espera(self, metodoCriterio):
        """
            en este primer ciclo se guarda
            el elemento y las consultas encubiertas
            en un objeto evaluador
        """
        ScorePopularidad.grid = self.grid
        for Q in self.consultasNuevas:
            for e in self.obtener_elementos_desde_consulta_encubierta(Q):
                # comprobacion de que el elemento no se repita en el evaluador
                my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorPopularidad)
                if len(my_filter_iter) == 1:  # si el elemento se repite en el evaluador solo guarda la consulta
                    my_filter_iter[0].agregar_consulta(Q)
                if len(
                        my_filter_iter) == 0:  # se el elemento no esta en el evaluados se guarda el elemento y la consulta
                    s = ScorePopularidad(e)
                    s.agregar_consulta(Q)
                    self.evaluacionPorPopularidad.append(s)

        for s in self.evaluacionPorPopularidad:
            s.obtener_score()

        # NORMALIZAR LAS PROBABILIDADES/score
        scoreTotal = float(0)
        for s in self.evaluacionPorPopularidad:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion


        scoreTotalNormal = float(0)
        for s in self.evaluacionPorPopularidad:
            s.normalizar(scoreTotal)
            scoreTotalNormal += s.puntuacion

        # evaluacion del tiempo de espera
        for s in self.evaluacionPorPopularidad:
            s.puntuacion = s.puntuacion + s.obtener_tiempo_espera_mayor(self.time)

        # NORMALIZAR LAS PROBABILIDADES/score
        scoreTotal = float(0)
        for s in self.evaluacionPorPopularidad:
            s.obtener_score_probabilista()
            scoreTotal += s.puntuacion

        scoreTotalNormal = float(0)
        for s in self.evaluacionPorPopularidad:
            s.normalizar(scoreTotal)
            scoreTotalNormal += s.puntuacion

        """
            En este ciclo se ordenan de forma 
            probabilista los elementos de datos
            Durante un determinado numero de 
            repeticiones se selecciona el 
            cronograma truncado segun 
            alguno de los reiterios de seleccion:
            1. Carga de trabajo
            2. Stretch
            3. Jitter
        """

        conjuntoCronogramas = []
        for _ in range(0, self.numeroRepeticiones):
            # 1. Seleccion de orden probabilista
            self.evaluacionPorPopularidad = Probabilista.ordenarProbabilista(self.evaluacionPorPopularidad)
            # 2. Asignar elementos en el cronograma
            for e in self.evaluacionPorPopularidad:
                if e not in self.cronograma.items:
                    self.cronograma.items.append(e.elemento)
            # 2.1 asignar elemetos resultantes antes del truncado
            self.ajuste.programaActual = self.cronograma.items
            # 3. Truncar el cronograma
            truncado = TruncadorDeCronograma(self.cronograma)
            truncado.truncar()
            # 3.1 asignar elementos pendientes
            self.ajuste.cronogramaPendiente = truncado.elementosPendientes
            # 5. aplicar criterio de seleccion
            self.cronograma.puntos = metodoCriterio(self.cronograma, self.consultasNuevas, self)
            conjuntoCronogramas.append(self.cronograma)
            self.cronograma = Cronograma(self.sizeCronograma)

        # 6. seleccion del cronograma segun el criterio de seleccion
        if metodoCriterio.__name__ == 'criterio_por_stretch':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio stretch es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_jitter':
            self.cronograma = min(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Menor criterio jitter es: {}'.format(self.cronograma.puntos)
        if metodoCriterio.__name__ == 'criterio_por_carga_de_trabajo':
            self.cronograma = max(conjuntoCronogramas, key=attrgetter('puntos'))
            print 'Mayor criterio carcara de trabajo es: {}'.format(self.cronograma.puntos)

        # 4. obtener las consultas pendientes
        if len(self.evaluacionPorPopularidad) > self.cronograma.size:  # si existen elementos pendientes
            # obtencion de las consultas pendientes de los itemes pendientes
            self.consultasPendientes = truncado.obtener_consulta_pendientes_popularidad(
                self.evaluacionPorPopularidad[self.cronograma.size: len(self.evaluacionPorPopularidad)])

        # 4.1. asignar las consultas que faltan por responder y las consultas respondidas
        self.ajuste.consultasAResponder = self.consultasPendientes
        self.ajuste.consultasRespondidas = list(set(self.consultasNuevas) - set(self.consultasPendientes))
        self.consultasNuevas = []

        return self.cronograma