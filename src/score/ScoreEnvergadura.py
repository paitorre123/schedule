import os


class ScoreEnvergadura(object):
    grid = None
    def __init__(self, consultaEncubierta):
        self.consultaEncubierta = consultaEncubierta
        self.elementos, self.puntuacion = self._obtener_score()


    def _obtener_score(self):
        elementos = []
        for q in self.consultaEncubierta.consultas:
            elementos += self._obtener_puntos_de_interes(q)
        return elementos, len(elementos)

    def obtener_score_probabilista(self):
        self.puntuacion = float(1)/len(self.elementos)

    def normalizar(self, scoreTotal):
        self.puntuacion = float(self.puntuacion)/scoreTotal

    def _obtener_puntos_de_interes(self, subconsulta):
        elementos = []
        for cell in self.grid.cells:
            for poi in cell.pointsInterest:
                if subconsulta.contain(poi.point.pointX, poi.point.pointY):
                    elementos.append(poi.dato)
        return elementos

    def obtener_tiempo_espera_mayor(self, time):
        tiemposDeEspera = []
        tiemposDeEspera.append(time.time-self.consultaEncubierta.arriveInServer)
        return max(tiemposDeEspera)

