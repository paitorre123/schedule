

class Elemento(object):
    def __init__(self, puntoDeInteres):
        self.score = 0
        self.puntoDeInteres = puntoDeInteres

    def __str__(self):
        return 'Elemento {}'.format(self.puntoDeInteres.name)

class ElementoFinBroadcast(object):
    def __init__(self):
        self.identificador = 'Fin de broadcast'
    def __str__(self):
        return 'Elemento {}'.format(self.identificador)