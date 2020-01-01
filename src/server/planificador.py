from src.server.cronograma import Cronograma



class Planificador(object):
    ajuste = None
    def __init__(self, time, grid, consultasNuevas, consultasPendientes, size):
        self.time = time
        self.grid = grid
        self.consultasNuevas = consultasNuevas
        self.consultasPendientes = consultasPendientes
        self.sizeCronograma = size + 1
        self.cronograma = Cronograma(size)

    def _obtener_cantidad_puntos_de_interes(self, consulta):
        elementos = []
        for cell in self.grid.cells:
            for poi in cell.pointsInterest:
                if consulta.contain(poi.point.pointX, poi.point.pointY):
                    elementos.append(poi.dato)
        return len(elementos)

    def _obtener_elementos(self, consulta):
        elementos = []
        for cell in self.grid.cells:
            for poi in cell.pointsInterest:
                if consulta.contain(poi.point.pointX, poi.point.pointY):
                    elementos.append(poi.dato)
        return elementos

    def obtener_puntos_interes_consultas_encubiertas(self, consultasEncubiertas):
        elementos = []
        for ce in consultasEncubiertas:
            for sq in ce.consultas:
                poi = self._obtener_elementos(sq)
                for e in poi:
                    elementos.append(e)
        return elementos

    def obtener_elementos_desde_consulta_encubierta(self, consultaEncubierta):
        elementos = []
        for sq in consultaEncubierta.consultas:
            poi = self._obtener_elementos(sq)
            for e in poi:
                elementos.append(e)
        return elementos

    def obtener_elementos_desde_subconsulta(self, subConsulta):
        elementos = []
        poi = self._obtener_elementos(subConsulta)
        for e in poi:
            elementos.append(e)

        return elementos


