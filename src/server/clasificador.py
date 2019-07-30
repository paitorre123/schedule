from src.server.evaluador import Evaluador

class Clasificador(object):
    def __init__(self):
        self.evaluadores = []

    def crear_evaluador(self, consulta, puntuacion):
        e = Evaluador()
        e.consulta = consulta
        e.puntuacion = puntuacion
        self.evaluadores.append(e)

    def quicksort(self, izq, der):
        i = izq
        j = der
        x = self.evaluadores[(izq + der) / 2].puntuacion

        while (i <= j):
            while self.evaluadores[i].puntuacion > x and j <= der:
                i = i + 1
            while x > self.evaluadores[j].puntuacion and j > izq:
                j = j - 1
            if i <= j:
                aux = self.evaluadores[i]
                self.evaluadores[i] = self.evaluadores[j]
                self.evaluadores[j] = aux
                i = i + 1
                j = j - 1

            if izq < j:
                self.quicksort(izq, j)
        if i < der:
            self.quicksort(i, der)