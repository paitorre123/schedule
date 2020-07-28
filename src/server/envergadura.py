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
from collections import OrderedDict
from src.score.scorePopularidad import ScorePopularidad
from src.score.ScoreIgualEnvergaduraConPopularidad import ScoreIgualEnvergaduraConPopularidad


class Envergadura(Planificador):
    numeroRepeticiones = 10
    ajusteTemporal = True
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Planificador.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)

        ##elementos para la evaluacion
        self.evaluacionPorEnvergadura = []
        self.evaluacionPorPopularidad = []
        self.swithEnvergadura = {'Envergadura Determinista': self._cronograma_por_respuesta_mas_corta_determinista,
                                'Envergadura Probabilista': self._cronograma_por_respuesta_mas_corta_probabilista,
                                'Envergadura X Tiempo': self._cronograma_por_respuesta_mas_corta_probabilista_tiempo_espera,
                                'Envergadura X Tiempo X Popularidad Aleatoria':self._cronograma_por_respuesta_mas_corta_probabilista_tiempo_espera_popularidad_promedio_aleatoria,
                                'Envergadura X Tiempo X Popularidad Aleatoria Maxima':self._cronograma_por_respuesta_mas_corta_probabilista_tiempo_espera_popularidad_maximo_aleatoria,}

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

    def _cronograma_por_respuesta_mas_corta_probabilista_tiempo_espera_popularidad_promedio_aleatoria(self, metodoCriterio):
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

            # 1.1 Agrupar CUEs segun puntaje
            conjuntoDeCUESPorPuntaje = OrderedDict()
            for screnv in self.evaluacionPorEnvergadura:
                if screnv.puntuacion in conjuntoDeCUESPorPuntaje:
                    conjuntoDeCUESPorPuntaje[screnv.puntuacion].append(screnv)
                else:
                    conjuntoDeCUESPorPuntaje[screnv.puntuacion] = []
                    conjuntoDeCUESPorPuntaje[screnv.puntuacion].append(screnv)
            # 1.2 Eliminar los conjuntos que solo tiene una CUE
            conjuntoDeCUESPorPuntaje = {k: v for k, v in conjuntoDeCUESPorPuntaje.items() if len(v) > 1}

            #print '-'*20
            #print'CONJUNTO DE CUES POR PUNTAJE'
            #totalCUES = 0
            #for k, v in conjuntoDeCUESPorPuntaje.items():
                #print '{}->{}'.format(k, len(v))
                #totalCUES += len(v)
            #print'CONJUNTO DE CUES: {}'.format(totalCUES)
            #print '-' * 20

            #1.3 calcular para cada elemento su nivel de popularidad
            #print '::POPULARIDAD PROBABILISTA:::'
            ScorePopularidad.grid = self.grid
            diccionarioPopularidadElementos = OrderedDict()
            for k, v in conjuntoDeCUESPorPuntaje.items():
                for Q in v:
                    for e in self.obtener_elementos_desde_consulta_encubierta(Q.consultaEncubierta):
                        # comprobacion que el elemento no se repita en el evaluador
                        my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorPopularidad)
                        if len(my_filter_iter) == 1:  # si el elemento se repite en el evaluador solo guarda la consulta
                            my_filter_iter[0].agregar_consulta(Q.consultaEncubierta)
                        if len(
                            my_filter_iter) == 0:  # se el elemento no esta en el evaluados se guarda el elemento y la consulta
                            s = ScorePopularidad(e)
                            s.agregar_consulta(Q.consultaEncubierta)
                            self.evaluacionPorPopularidad.append(s)


            for s in self.evaluacionPorPopularidad:
                s.obtener_score()

            scoreTotal = float(0)
            for s in self.evaluacionPorPopularidad:
                s.obtener_score_probabilista()
                scoreTotal += s.puntuacion

            # NORMALIZAR LAS PROBABILIDADES/score
            scoreTotalNormal = float(0)
            for s in self.evaluacionPorPopularidad:
                s.normalizar(scoreTotal)
                scoreTotalNormal += s.puntuacion
                diccionarioPopularidadElementos[s.elemento] = s.puntuacion

            #print '-' * 20
            #print'POPULARIDAD ITEMES'
            #totalCUES = 0
            #for score in self.evaluacionPorPopularidad:
                #print '{}->{}'.format(score.elemento, score.puntuacion)
                #totalCUES += len(v)
            #print'CONJUNTO DE CUES: {}'.format(totalCUES)
            #print '-' * 20

            #1.4 calcular para cada CUE su nivel de popularidad
            popularidadPromedioCUE = OrderedDict()
            for k, v in conjuntoDeCUESPorPuntaje.items():
                for Q in v:
                    elementosCue = []
                    for e in self.obtener_elementos_desde_consulta_encubierta(Q.consultaEncubierta):
                        if diccionarioPopularidadElementos[e] not in elementosCue:
                            elementosCue.append(diccionarioPopularidadElementos[e])
                    popularidadPromedioCUE[Q.consultaEncubierta] = np.mean(elementosCue)
            #print '-' * 20
            #for k, v in popularidadPromedioCUE.items():
                #print '{}-->{}'.format(k, v)
            #print '-' * 20

            grupoDeCUESConPopularidad = []
            for k, v in conjuntoDeCUESPorPuntaje.items():
                cues = OrderedDict()
                for Q in v:
                    #print popularidadPromedioCUE[Q.consultaEncubierta]
                    cues[Q.consultaEncubierta] = popularidadPromedioCUE[Q.consultaEncubierta]


                scr = ScoreIgualEnvergaduraConPopularidad(cues)
                grupoDeCUESConPopularidad.append(scr)

            for gccp in grupoDeCUESConPopularidad:
                #gccp.imprimir()
                gccp.normalizar_popularidades()
                #gccp.imprimir()
                gccp.orden_probabilista()
                #gccp.imprimir()
                gccp.ordenarEnvergadura(self.evaluacionPorEnvergadura)
                #os.system('pause')

            #os.system('pause')

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

    def _cronograma_por_respuesta_mas_corta_probabilista_tiempo_espera_popularidad_maximo_aleatoria(self, metodoCriterio):
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

            # 1.1 Agrupar CUEs segun puntaje
            conjuntoDeCUESPorPuntaje = OrderedDict()
            for screnv in self.evaluacionPorEnvergadura:
                if screnv.puntuacion in conjuntoDeCUESPorPuntaje:
                    conjuntoDeCUESPorPuntaje[screnv.puntuacion].append(screnv)
                else:
                    conjuntoDeCUESPorPuntaje[screnv.puntuacion] = []
                    conjuntoDeCUESPorPuntaje[screnv.puntuacion].append(screnv)
            # 1.2 Eliminar los conjuntos que solo tiene una CUE
            conjuntoDeCUESPorPuntaje = {k: v for k, v in conjuntoDeCUESPorPuntaje.items() if len(v) > 1}

            #print '-'*20
            #print'CONJUNTO DE CUES POR PUNTAJE'
            #totalCUES = 0
            #for k, v in conjuntoDeCUESPorPuntaje.items():
                #print '{}->{}'.format(k, len(v))
                #totalCUES += len(v)
            #print'CONJUNTO DE CUES: {}'.format(totalCUES)
            #print '-' * 20

            #1.3 calcular para cada elemento su nivel de popularidad
            #print '::POPULARIDAD PROBABILISTA:::'
            ScorePopularidad.grid = self.grid
            diccionarioPopularidadElementos = OrderedDict()
            for k, v in conjuntoDeCUESPorPuntaje.items():
                for Q in v:
                    for e in self.obtener_elementos_desde_consulta_encubierta(Q.consultaEncubierta):
                        # comprobacion que el elemento no se repita en el evaluador
                        my_filter_iter = filter(lambda s: s.elemento == e, self.evaluacionPorPopularidad)
                        if len(my_filter_iter) == 1:  # si el elemento se repite en el evaluador solo guarda la consulta
                            my_filter_iter[0].agregar_consulta(Q.consultaEncubierta)
                        if len(
                            my_filter_iter) == 0:  # se el elemento no esta en el evaluados se guarda el elemento y la consulta
                            s = ScorePopularidad(e)
                            s.agregar_consulta(Q.consultaEncubierta)
                            self.evaluacionPorPopularidad.append(s)


            for s in self.evaluacionPorPopularidad:
                s.obtener_score()

            scoreTotal = float(0)
            for s in self.evaluacionPorPopularidad:
                s.obtener_score_probabilista()
                scoreTotal += s.puntuacion

            # NORMALIZAR LAS PROBABILIDADES/score
            scoreTotalNormal = float(0)
            for s in self.evaluacionPorPopularidad:
                s.normalizar(scoreTotal)
                scoreTotalNormal += s.puntuacion
                diccionarioPopularidadElementos[s.elemento] = s.puntuacion

            #print '-' * 20
            #print'POPULARIDAD ITEMES'
            #totalCUES = 0
            #for score in self.evaluacionPorPopularidad:
                #print '{}->{}'.format(score.elemento, score.puntuacion)
                #totalCUES += len(v)
            #print'CONJUNTO DE CUES: {}'.format(totalCUES)
            #print '-' * 20

            #1.4 calcular para cada CUE su nivel de popularidad
            popularidadPromedioCUE = OrderedDict()
            for k, v in conjuntoDeCUESPorPuntaje.items():
                for Q in v:
                    elementosCue = []
                    for e in self.obtener_elementos_desde_consulta_encubierta(Q.consultaEncubierta):
                        if diccionarioPopularidadElementos[e] not in elementosCue:
                            elementosCue.append(diccionarioPopularidadElementos[e])
                    popularidadPromedioCUE[Q.consultaEncubierta] = np.max(elementosCue)
            #print '-' * 20
            #for k, v in popularidadPromedioCUE.items():
                #print '{}-->{}'.format(k, v)
            #print '-' * 20

            grupoDeCUESConPopularidad = []
            for k, v in conjuntoDeCUESPorPuntaje.items():
                cues = OrderedDict()
                for Q in v:
                    #print popularidadPromedioCUE[Q.consultaEncubierta]
                    cues[Q.consultaEncubierta] = popularidadPromedioCUE[Q.consultaEncubierta]


                scr = ScoreIgualEnvergaduraConPopularidad(cues)
                grupoDeCUESConPopularidad.append(scr)

            for gccp in grupoDeCUESConPopularidad:
                #gccp.imprimir()
                gccp.normalizar_popularidades()
                #gccp.imprimir()
                gccp.orden_probabilista()
                #gccp.imprimir()
                gccp.ordenarEnvergadura(self.evaluacionPorEnvergadura)
                #os.system('pause')

            #os.system('pause')

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