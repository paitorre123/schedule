

class ConsultaEncubierta(object):
    def __init__(self, usuario):
        self.arriveInServer = False
        self.consultas = []
        self.usuario = usuario
        self.arriveInServerTime = 0
        self.genetareCUETime = 0
    def __str__(self):
        return "Consulta encubierta del usuario {}".format(self.usuario )

