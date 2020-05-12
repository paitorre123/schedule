import random
from random import randint
import os
from src.server.cronograma import Cronograma
import numpy as np
from decimal import Decimal
from src.server.clasificador import Clasificador
import math
from src.server.cargaDeTrabajo import CargaDeTrabajo
from src.server.ecuanimidad import Ecuanimidad
from src.server.relevancia import Relevancia
from src.server.envergadura import Envergadura
from src.server.popularidad import Popularidad
from src.server.Fifo import Fifo
from src.criterioDeSeleccion.criterio import Criterio
from src.server.planificador import Planificador
from src.consulta.elemento import ElementoFinBroadcast
from src.manejoDeDatos.ManejoDeDatos import ManejoDeDatos


class Servidor(object):
    def __init__(self, grid, size,planificador, ajuste, criterio):
        self.consultasPendientes = []
        self.consultasNuevas = []
        self.usuarios = []
        self.grid = grid
        self.waitTime = 10
        self.size = size
        self.algoritmoPlanificador= planificador
        self.ajuste = ajuste
        self.criterio = criterio
        '''
        EL  HISTORIAL DE CONSULTA
        MANTIENE REGISTRO DE LAS 
        CONSULTAS QUE SE HAN HECHO 
        EN EL PASADO.
        '''
        self.historialDeElementos = []
        self.historialDeCUEs = []


    def generar_cronograma_inicial(self):
        print 'Generando cronograma inicial'
        self.cronograma = Cronograma(self.size)

        self.dataPointInterest = []
        for cell in self.grid.cells:
            for poi in cell.pointsInterest:
                self.dataPointInterest.append(poi.dato)

        probability = []
        for _ in self.dataPointInterest:
            probability.append(Decimal(1) / len(self.dataPointInterest))
        try:
            self.puntosDeInteres = np.random.choice(self.dataPointInterest, self.size, p=probability, replace=False)
        except ValueError:
            self.puntosDeInteres = np.random.choice(self.dataPointInterest, len(self.dataPointInterest), p=probability, replace=False)
        self.consultasPendientes = []


        self.cronograma.asignar_elementos(self.puntosDeInteres, self.consultasPendientes)
        self.cronograma.items.append(ElementoFinBroadcast())
        #os.system('pause')

    def generar_cronograma(self, time, algoritmoAjuste):
        previousScheduleSize = len(self.cronograma.items)
        self.cronograma = Cronograma(self.size)
        self.consultasNuevas = []

        for usuario in self.usuarios:
            #print '->Servidor recibe consulta de usuario: {}'.format(usuario)
            usuario.consultaEncubierta.arriveInServer = True
            usuario.consultaEncubierta.arriveInServerTime =  time.time
            #arriveTime = randint(time.time-previousScheduleSize, time.time)
            arriveTime = time.time
            #print '      ->time: {}'.format(arriveTime)
            for q in usuario.consultaEncubierta.consultas:
                if not q.tiempoLlegadaServidor:
                    q.tiempoLlegadaServidor = arriveTime
            self.consultasNuevas.append(usuario.consultaEncubierta)

        ManejoDeDatos.escribir_server_cues(self.consultasNuevas, time.time)
        print'::::::::::::::::::::::::::'
        print'Llegan {} CUEs al servidor'.format(len(self.consultasNuevas))
        print'::::::::::::::::::::::::::'

        #os.system('pause')
        if len(self.consultasNuevas) > 0:
            self.historialDeCUEs.append([len(self.consultasNuevas), time.time])


        Planificador.ajuste = algoritmoAjuste
        self.planificador = self._retornar_planificador(time)
        self.planificador.ajusteTemporal = self.ajuste
        self.planificador.activar_planificador(self._retornar_criterio(),self._rotornar_tipo_planificacion())

        #self.planificador = Relevancia(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        #self.planificador = Envergadura(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)


        self._depurar_historial()
        self.cronograma = self.planificador.cronograma
        self.usuarios = []

    def _retornar_criterio(self):
        if self.criterio == 'Carga de trabajo':
            return Criterio.criterio_por_carga_de_trabajo
        if self.criterio == 'Stretch':
            return Criterio.criterio_por_stretch
        if self.criterio == 'Jitter':
            return Criterio.criterio_por_jitter


    def _retornar_planificador(self, time):
        if self.algoritmoPlanificador == 'Algoritmo Fifo':
            return Fifo(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo de Envergadura determinista':
            return Envergadura(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo de Envergadura probabilista':
            return Envergadura(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo de Envergadura probabilista con tiempo de espera':
           return Envergadura(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo de popularidad determinista':
            return Popularidad(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo de popularidad probabilista':
            return Popularidad(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo de popularidad probabilista con tiempo de espera':
            return Popularidad(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo relevancia determinista':
            return Relevancia(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo relevancia probabilista':
            return Relevancia(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)
        if self.algoritmoPlanificador == 'Algoritmo relevancia probabilista con tiempo de espera':
            return Relevancia(time, self.grid, self.consultasNuevas, self.consultasPendientes, self.size)

    def _rotornar_tipo_planificacion(self):
        if self.algoritmoPlanificador == 'Algoritmo Fifo':
            return 'Fifo'
        if self.algoritmoPlanificador == 'Algoritmo de Envergadura determinista':
            return 'Envergadura Determinista'
        if self.algoritmoPlanificador == 'Algoritmo de Envergadura probabilista':
            return 'Envergadura Probabilista'
        if self.algoritmoPlanificador == 'Algoritmo de Envergadura probabilista con tiempo de espera':
           return 'Envergadura X Tiempo'
        if self.algoritmoPlanificador == 'Algoritmo de popularidad determinista':
            return 'Popularidad Determinista'
        if self.algoritmoPlanificador == 'Algoritmo de popularidad probabilista':
            return'Popularidad Probabilista'
        if self.algoritmoPlanificador == 'Algoritmo de popularidad probabilista con tiempo de espera':
            return 'Popularidad X Tiempo'
        if self.algoritmoPlanificador == 'Algoritmo relevancia determinista':
            return 'Relevancia Determinista'
        if self.algoritmoPlanificador == 'Algoritmo relevancia probabilista':
            return 'Relevancia Probabilista'
        if self.algoritmoPlanificador == 'Algoritmo relevancia probabilista con tiempo de espera':
            return 'Relevancia X Tiempo'

    def _depurar_historial(self):
        print 'DEPURACION  HISTORIAL'
        self.historialDeElementos = []
        '''
        EN ESTE METODO SE DEBE APLICAR
        UN ALGORITMOS QUE COLECCIONA 
        LAS CONSULTAS REALIZADAS POR LOS
        USUARIOS.
        '''
        #print 'HISTORIAL'
        for data in self.puntosDeInteres:
            #print 'POI: {}'.format(data.puntoDeInteres)
            self.historialDeElementos.append(data)
        '''
        1. QUIZAS EL HISTORIAL DE CONSULTAS
        DEBE SER ALMACENADO.
        '''
        #os.system('pause')

    def _eliminar_consultas_repetidas(self):
        for query in self.actualQuery:
            #print 'id consulta: {}'.format(query)
            for q in self.actualQuery:
                if query.pointA.pointX == q.pointA.pointX and  query.pointA.pointY == q.pointA.pointY \
                        and query.pointB.pointX == q.pointB.pointX and  query.pointB.pointY == q.pointB.pointY \
                        and query.pointC.pointX == q.pointC.pointX and query.pointC.pointY == q.pointC.pointY \
                        and query.pointD.pointX == q.pointD.pointX and query.pointD.pointY == q.pointD.pointY:
                    self.actualQuery.remove(q)
            self.actualQuery.append(query)
        print 'Consultas de rango: {}'.format(len(self.actualQuery))


    def _extraer_puntos_de_interes(self):
        for cell in self.grid.cells:
            for poi in cell.pointsInterest:
                for query in self.actualQuery:
                    if query.contain(poi.point.pointX, poi.point.pointY):
                        if poi.dato not in self.puntosDeInteres:
                            self.puntosDeInteres.append(poi.dato)
        print 'Elementos de datos: {}'.format(len(self.puntosDeInteres))
