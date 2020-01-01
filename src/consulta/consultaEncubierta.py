

class ConsultaEncubierta(object):
    def __init__(self, usuario):
        self.arriveInServer = False
        self.consultas = []
        self.usuario = usuario
        self.arriveInServerTime = 0
        self.genetareCUETime = 0
        self.watchFinalSchedule = False
    def __str__(self):
        return "{}:{}:{}".format(self.usuario, self.genetareCUETime, self.arriveInServerTime)

