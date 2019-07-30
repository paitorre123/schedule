


class ScoreConsultaEncubierta(object):
    def __init__(self, consultaEncubierta):
        self.consultaEncubierta = consultaEncubierta
        self.subconsultas = []

class ScoreSubConsulta(object):
    def __init__(self, subConsulta):
        self.subConsulta = subConsulta
        self.elementos = []
        self.putntuacion = 0

class ScoreElemento(object):
    def __init__(self, elemento):
        self.elemento = elemento
        self.consultasEncubiertas = []