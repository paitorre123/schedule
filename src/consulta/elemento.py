

class Elemento(object):
    def __init__(self, puntoDeInteres):
        self.score = 0
        self.puntoDeInteres = puntoDeInteres

class ElementoFinBroadcast(object):
    def __init__(self):
        self.identificador = 'Fin de broadcast'