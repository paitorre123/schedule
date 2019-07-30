import random
from random import randint
import numpy as np
from decimal import Decimal
from src.server.clasificador import Clasificador
import math
from src.server.planificador import Planificador

class Ecuanimidad(Planificador):
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        Planificador.__init__(self, time, grid, consultasNuevas, consultasPendientes, size)

    def activar_planificador(self, tipe):
        self._cronograma_por_region_de_encubrimiento()

    def _cronograma_por_region_de_encubrimiento(self):

        while len(self.consultasNuevas) > 0:
            inversos = self._calcular_inverso_region()
            consultaSeleccionada = self._seleccion_menor_score(inversos)
            if len(list(set(self.cronograma.items) | set(self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada)))) <= self.cronograma.size:
                # print 'Consulta seleccionada cabe en cronogrma'
                self.cronograma.agregar_consulta(self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada))
                self.consultasNuevas.remove(consultaSeleccionada[0])
                # os.system('pause')
            else:
                # print 'Consulta seleccionada no cabe en cronogrma'
                # os.system('pause')
                self.cronograma.agregar_fraccion_consulta( self.obtener_puntos_interes_consulta_encubierta(consultaSeleccionada))
                for q in self.consultasNuevas:
                    self.consultasPendientes.append(q)
                self.consultasNuevas = []


    def _calcular_inverso_region(self):
        inversos = []
        for q in self.consultasNuevas:
            inversos.append(float(1)/len(q.consultas))
        return inversos

    def _seleccion_menor_score(self, inversos):
        minimo = min(inversos)
        for i in range(0, len(inversos)):
            if minimo == inversos[i]:
                lst = []
                lst.append(self.consultasNuevas[i])
                return lst