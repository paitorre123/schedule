import random
from random import randint
from src.server.cronograma import Cronograma
import numpy as np
from decimal import Decimal
from src.server.clasificador import Clasificador
import math
from src.server.planificador import Planificador


class CargaDeTrabajo(Planificador):
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Planificador.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)
        self._cronogramaAnterior = Cronograma(size)

    def activar_planificador(self, tipe):
        #self._cronograma_por_talla_consulta_determinista_tiempo_de_espera(self.time)
        self._cronograma_por_talla_consulta_probabilista(self.time)
        #self._cronograma_por_talla_consulta_determinista()

    def _cronograma_por_talla_consulta_determinista(self):
        self.clasificador = Clasificador()
        self.puntosDeInteres = []

        while len(self.consultasNuevas) > 0:
            inversos = self._calcular_inversos()
            normalizaciones = self._probabilidad_normalizada(inversos)
            consultaSeleccionada = self._seleccion_mayor_score(normalizaciones)

            if len(list(set(self.cronograma.items) | set(self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada))))<= self.cronograma.size:
                # print 'Consulta seleccionada cabe en cronogrma'
                self.cronograma.agregar_consulta(self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada))
                self.consultasNuevas.remove(consultaSeleccionada[0])
                # os.system('pause')
            else:
                # print 'Consulta seleccionada no cabe en cronogrma'
                # os.system('pause')
                self.cronograma.agregar_fraccion_consulta(
                    self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada))
                for q in self.consultasNuevas:
                    self.consultasPendientes.append(q)
                self.consultasNuevas = []


    def _cronograma_por_talla_consulta_determinista_tiempo_de_espera(self, time):
        self.clasificador = Clasificador()
        self.puntosDeInteres = []
        #print 'GENERARNDO CRONOGRAMA DETERMINISTA POR TALLA DE LA CONSULTA'
        subconsultas = []
        #i=1
        for consultaEncubierta in self.consultasNuevas:
            #print 'Consulta encubierta: {}'.format(i)
            for subConsulta in consultaEncubierta:
                #print 'Id sub consulta: {}'.format(subConsulta)
                subconsultas.append(subConsulta)
            #i+=1

        for q_a in subconsultas:
            for q_b in subconsultas:
                if q_a.pointA.pointX == q_b.pointA.pointX and q_a.pointA.pointY == q_b.pointA.pointY \
                        and q_a.pointB.pointX == q_b.pointB.pointX and q_a.pointB.pointY == q_b.pointB.pointY \
                        and q_a.pointC.pointX == q_b.pointC.pointX and q_a.pointC.pointY == q_b.pointC.pointY \
                        and q_a.pointD.pointX == q_b.pointD.pointX and q_a.pointD.pointY == q_b.pointD.pointY:
                    subconsultas.remove(q_b)
            subconsultas.append(q_a)

        print 'Numero Sub Consultas: {}'.format(len(subconsultas))

        for q in subconsultas:
            numero_de_elementos = self._obtener_cantidad_puntos_de_interes(q)
            #print '->Id sub consulta: {}'.format(q)
            #print 'numero elementos: {} '.format(numero_de_elementos)
            if numero_de_elementos>0:
                self.clasificador.crear_evaluador(q, float(1) / numero_de_elementos)
                #print 'score: {}'.format(float(1) / numero_de_elementos)

        suma_puntuaciones = 0
        for c in self.clasificador.evaluadores:
            suma_puntuaciones=suma_puntuaciones+c.puntuacion

        #print 'suma de scores: {}'.format(suma_puntuaciones)

        for c in self.clasificador.evaluadores:
            if c.puntuacion > 0.0:
                #print 'Subconsulta: {}'.format(c.consulta)
                #print 'Division: {}/{}'.format(c.puntuacion, suma_puntuaciones)
                #c.puntuacion = Decimal(c.puntuacion)/Decimal(suma_puntuaciones)
                c.puntuacion = c.puntuacion / suma_puntuaciones
                #print 'score: {}'.format(c.puntuacion)
        #print 'Tiempo actual: {}'.format(time.time)
        #for c in self.clasificador.evaluadores:
            #print '->Subconsulta: {}'.format(c.consulta)
            #print '  Tiempo Llegada: {}'.format(c.consulta.tiempoLlegadaServidor)
            #print '  Tiempo espera: {}'.format(time.time-c.consulta.tiempoLlegadaServidor)
        #os.system('pause')

        '''
        INCORPORAR A LA PUNTUACION 
        EL TIEMPO DE ESPERA.
        '''
        for c in self.clasificador.evaluadores:
        # print '->Subconsulta: {}'.format(c.consulta)
        # print '  Tiempo Llegada: {}'.format(c.consulta.tiempoLlegadaServidor)
        # print '  Tiempo espera: {}'.format(time.time-c.consulta.tiempoLlegadaServidor)
            c.puntuacion = c.puntuacion * time.time-c.consulta.tiempoLlegadaServidor

        self.clasificador.quicksort(0, len(self.clasificador.evaluadores)-1)

        #for c in self.clasificador.evaluadores:
            #print '->Id consulta: {}'.format(c.consulta)
            #print 'score: {}'.format(c.puntuacion)

        for c in self.clasificador.evaluadores:
            elementos= self._obtener_elementos(c.consulta)
            for e in elementos:
                if e not in self.puntosDeInteres:
                    self.puntosDeInteres.append(e)

        #print 'Elementos de Datos'
        #for e in self.puntosDeInteres:
            #print 'Elemento: {}'.format(e.puntoDeInteres)

        print 'Cantidad de elementos: {}'.format(len(self.puntosDeInteres))

    def _cronograma_por_talla_consulta_probabilista(self, time):
        self.clasificador = Clasificador()
        self.puntosDeInteres = []
        # print 'GENERARNDO CRONOGRAMA  PROBILILISTA POR TALLA DE LA CONSULTA'
        subconsultas = []
        #auxConsultas = []
        # i=1
        #for consultaEncubierta in self.consultasNuevas:
            #auxConsultas.append(consultaEncubierta)

        #print 'Consulta nuevas: {}'.format(len(self.consultasNuevas))
        #os.system('pause')

        for _ in range(0,10):
            self.cronograma = Cronograma(self.cronograma.size)
            while len(self.consultasNuevas) > 0:
                inversos = self._calcular_inversos()
                normalizaciones = self._probabilidad_normalizada(inversos)
                consultaSeleccionada = self._seleccion_probabilista(normalizaciones)
                if len(list(set(self.cronograma.items) | set(self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada)))) <= self.cronograma.size:
                    # print 'Consulta seleccionada cabe en cronogrma'
                    self.cronograma.agregar_consulta(
                        self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada))
                    self.consultasNuevas.remove(consultaSeleccionada[0])
                    # os.system('pause')
                else:
                    # print 'Consulta seleccionada no cabe en cronogrma'
                    # os.system('pause')
                    self.cronograma.agregar_fraccion_consulta(
                        self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada))
                    for q in self.consultasNuevas:
                        self.consultasPendientes.append(q)
                    self.consultasNuevas = []

            if self.cronograma.len() > self._cronogramaAnterior.len():
                self._cronogramaAnterior = self.cronograma

        self.cronograma = self._cronogramaAnterior

    def _calcular_inversos(self):
        inversos = []
        for cq in self.consultasNuevas:
            poiCq = 0
            for sq in cq.consultas:
                poiCq+=self._obtener_cantidad_puntos_de_interes(sq)
            #print 'Valores Inverso: {}/{}'.format(1, poiCq)
            #print 'Inversos: {}'.format(float(1)/poiCq)
            inversos.append(float(1)/poiCq)
        return inversos

    def _probabilidad_normalizada(self, inversos):
        normalizaciones = []
        sumaTotalInversos = 0
        for i in inversos:
            sumaTotalInversos+=i

        for i in inversos:
            normalizaciones.append(float(i)/sumaTotalInversos)

        return normalizaciones

    def _seleccion_probabilista(self, normalizaciones):
        return np.random.choice(self.consultasNuevas, 1, p=normalizaciones, replace=False).tolist()

    def _seleccion_mayor_score(self, normalizaciones):
       mayor=max(normalizaciones)
       choice = []
       for i in range(0, len(normalizaciones)):
            if normalizaciones[i] == mayor:
                choice.append(self.consultasNuevas[i])
                return choice
       return None

