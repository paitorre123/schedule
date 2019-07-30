from src.score.scoreSubConsulta import ScoreSubConsulta


class ScoreRelevancia(object):
    def __init__(self, elemento):
        self.elemento = elemento
        self.scoreSubConsultas = []
        self.puntuacion = float(0.0)

    def agregar_score_subconsulta(self, Q, q):
        self.scoreSubConsultas.append(ScoreSubConsulta(q,Q))

    def obtener_score(self):
        for ssq in self.scoreSubConsultas:
            k = len(ssq.consultasEncubierta.consultas)
            self.puntuacion += float(1)/k

    def obtener_score_probabilista(self):
        self.puntuacion = float(1)/self.puntuacion

    def normalizar(self, scoreTotal):
        self.puntuacion = float(self.puntuacion)/scoreTotal

    def obtener_tiempo_espera_mayor(self, time):
        tiemposDeEspera = []
        for ssq in self.scoreSubConsultas:
            tiemposDeEspera.append(time.time-ssq.consultasEncubierta.arriveInServer)
        return max(tiemposDeEspera)