import os

class ScorePopularidad():
    grid = None
    def __init__(self, elemento):
        self.elemento = elemento
        self.consultas = []
        self.puntuacion = float(0.0)

    def agregar_consulta(self, Q):
        self.consultas.append(Q)

    def obtener_score(self):
        self.puntuacion = len(self.consultas)

    def obtener_score_probabilista(self):
        self.puntuacion = float(1)/self.puntuacion

    def normalizar(self, scoreTotal):
        self.puntuacion = float(self.puntuacion)/scoreTotal


    def _obtener_puntos_de_interes(self, subconsulta):
        elementos = []
        for cell in self.grid.cells:
            for poi in cell.pointsInterest:
                if subconsulta.contain(poi.point.pointX, poi.point.pointY):
                    elementos.append(poi)
        return elementos

    def obtener_tiempo_espera_mayor(self, time):
        tiemposDeEspera = []
        for Q in self.consultas:
            tiemposDeEspera.append(time.time-Q.arriveInServer)
        return max(tiemposDeEspera)
