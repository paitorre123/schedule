


class TruncadorDeCronograma(object):
    def __init__(self, cronograma):
        self.cronograma = cronograma
        self.elementosTransmitidos = []
        self.elementosPendientes = []

    def truncar(self):
        if len(self.cronograma.items) > self.cronograma.size:#hay desborde
            self.elementosTransmitidos = self.cronograma.items[0:self.cronograma.size]
            self.elementosPendientes = self.cronograma.items[self.cronograma.size : len(self.cronograma.items)-1]
        else:
            self.elementosTransmitidos = self.cronograma.items
        """
            Asignar elementos de datos nuevos
        """
        self.cronograma.items = self.elementosTransmitidos

    def obtener_consulta_pendientes_envergadura(self, evalucion):
        consultasPendientes = []
        for s in evalucion:
            if len(set(s.elementos).intersection(self.elementosPendientes)) > 0:
                consultasPendientes.append(s.consultaEncubierta)
        return consultasPendientes

    def obtener_consulta_pendientes_popularidad(self, evaluacion):
        consultasPendientes = []
        for s in evaluacion:
            for Q in s.consultas:
                if Q not in consultasPendientes:
                    consultasPendientes.append(Q)
        return consultasPendientes

    def obtener_consulta_pendientes_relevancia(self, evaluacion):
        consultasPendientes = []
        for s in evaluacion:
            for ssq in s.scoreSubConsultas:
                if ssq.consultasEncubierta not in consultasPendientes:
                    consultasPendientes.append(ssq.consultasEncubierta )
        return consultasPendientes

