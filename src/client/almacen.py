import os
from src.consulta.consultaDeRango import ConsultaDeRango
from src.consulta.consultaDeRangoArtificial import ConsultaDeRangoArtificial

class Almacen(object):
    def __init__(self, consultaEncubierta, subConsultasDeRango, grid):

        self.consultaEncubierta = consultaEncubierta
        self.subConsultasDeRango = subConsultasDeRango
        self.grid = grid

        self.subconsultaReal = 0
        self.elementosRequeridosReales = []
        self.elementosEncontradosReales = []
        self.tiempoElementosEncontradosReales = []

        self.idSubconsultasArtificiales = []
        self.elementosRequeridosArtificiales = []
        self.elementosEncontradosArtificiales = []
        self.tiempoElementosEncontradosArtificiales = []

        self._obtener_elementos_necesarios()

    def _obtener_elementos_necesarios(self):
        #print 'Perimetro contines los siguienetes elementos'
        #print 'OBTENIENDO PUNTOS DE INTERES DE CONSULTA ENCUBIERTA'
        for subconsulta in self.subConsultasDeRango:
            if isinstance(subconsulta, ConsultaDeRango):
                self.subconsultaReal = subconsulta
                #print 'Id subconsulta real: {}'.format(subconsulta)
                #print '-->Punto A: {},{}'.format(subconsulta.pointA.pointX, subconsulta.pointA.pointY)
                #print '-->Punto B: {},{}'.format(subconsulta.pointB.pointX, subconsulta.pointB.pointY)
                #print '-->Punto C: {},{}'.format(subconsulta.pointC.pointX, subconsulta.pointC.pointY)
                #print '-->Punto D: {},{}'.format(subconsulta.pointD.pointX, subconsulta.pointD.pointY)
                for cell in self.grid.cells:
                    for item in cell.pointsInterest:
                        if subconsulta.contain(item.point.pointX, item.point.pointY):
                            #print '--->Item: {}'.format(item)
                            self.elementosRequeridosReales.append(item)
            if isinstance(subconsulta, ConsultaDeRangoArtificial):
                self.idSubconsultasArtificiales.append(subconsulta)
                #print 'Id subconsulta artificial: {}'.format(subconsulta)
                #print '-->Punto A: {},{}'.format(subconsulta.pointA.pointX, subconsulta.pointA.pointY)
                #print '-->Punto B: {},{}'.format(subconsulta.pointB.pointX, subconsulta.pointB.pointY)
                #print '-->Punto C: {},{}'.format(subconsulta.pointC.pointX, subconsulta.pointC.pointY)
                #print '-->Punto D: {},{}'.format(subconsulta.pointD.pointX, subconsulta.pointD.pointY)
                for cell in self.grid.cells:
                    for item in cell.pointsInterest:
                        if subconsulta.contain(item.point.pointX, item.point.pointY):
                            #print '--->Item: {}'.format(item)
                            self.elementosRequeridosArtificiales.append(item)
        #os.system('pause')

    def is_completed(self):
        return len(self.elementosRequeridosReales) == len(self.elementosEncontradosReales)