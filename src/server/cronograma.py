

class Cronograma(object):
    def __init__(self, size):
        self.size = size
        self.items = []
        self.puntos = 0
        self.isEnd = False
        self.programa = []

    def asignar_elementos(self, items, outstandingItems):
        try:
            for x in range(0,self.size):
                self.items.append(items[x])
        except IndexError:
            print 'out of range item schedule'
        try:
            for x in range(self.size, len(items)):
                    outstandingItems.append(items[x])
        except IndexError:
            print 'out of range outstanding item'

    def len(self):
        return len(self.items)

    def agregar_consulta(self, elementosDeConsultaEncubieta):
        for ece in elementosDeConsultaEncubieta:
            if ece not in self.items:
                self.items.append(ece)


    def agregar_fraccion_consulta(self, elementosDeConsultaEncubieta):
        i = 0
        while len(self.items)<100 and i<len(elementosDeConsultaEncubieta):
            if elementosDeConsultaEncubieta[i] not in self.items:
                self.items.append(elementosDeConsultaEncubieta[i])
            i+=1

    def agregar_consulta_encubierta(self, scoreConsultasEncubiertasOrdenadas):
        for score in scoreConsultasEncubiertasOrdenadas:
            for e in score.elementos:
                if e not in self.items:
                    self.items.append(e)

    def is_end_schedule(self):
        return self.isEnd




