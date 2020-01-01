from src.criterioDeSeleccion.scoreCriterio import ScoreConsultaEncubierta
from src.criterioDeSeleccion.scoreCriterio import ScoreElemento
from src.criterioDeSeleccion.scoreCriterio import ScoreSubConsulta


class Criterio(object):

    @classmethod
    def criterio_por_carga_de_trabajo(cls, cronograma, consultasEncubiertas, planificador):
        print "SELECCION POR CARAGA DE TRABAJO"
        datosDeConsultasEncubiertas = cls._obetener_datos_consultas_encubiertas(consultasEncubiertas, planificador)
        datosElementos = cls._obetener_datos_elementos_consultas_encubiertas(consultasEncubiertas, planificador)
        valorCargaDetrabajo = float(0)
        for e in cronograma.items:
            #print "Elemento: {}".format(e.puntoDeInteres)
            datoElemento = filter(lambda x: x.elemento == e, datosElementos)
            for Q in datoElemento[0].consultasEncubiertas:
                #print "      Q:{}".format(Q)
                tallaConsultaEcubiertaDeElemento = float(1)/ len(Q.consultas)
                datoConsultaEncubierta = filter(lambda x: x.consultaEncubierta==Q, datosDeConsultasEncubiertas)
                valorCargaDeTrabajoEnConsultaEncubierta = float(0)
                for q in datoConsultaEncubierta[0].subconsultas:
                    #print "          q:{}".format(q.subConsulta)
                    if e in q.elementos:
                        valorCargaDeTrabajoEnConsultaEncubierta +=  (float(1)/len(q.elementos))
                valorCargaDeTrabajoEnConsultaEncubierta = tallaConsultaEcubiertaDeElemento * valorCargaDeTrabajoEnConsultaEncubierta
                valorCargaDetrabajo += valorCargaDeTrabajoEnConsultaEncubierta
        #print "Puntos por CDT: {}".format(valorCargaDetrabajo)
        return valorCargaDetrabajo

    @classmethod
    def criterio_por_stretch(cls, cronograma, consultasEncubiertas, planificador):
        print "SELECCION POR STRETCH"
        datosSubconsultas= cls._obetener_datos_subconsultas(cronograma, consultasEncubiertas, planificador)
        valorMaximoStretch = float(0)
        #las sub consultas contienen los elementos presentes en el cronograma
        mayorPuntuacion = 0
        for dsc in datosSubconsultas:
            if len(dsc.elementos) > 0:
                index = []
                for e in dsc.elementos:
                    index.append(cronograma.items.index(e))
                mayor = max(index)
                tiempoEspera = mayor
                #print 'Tiempo de espera: {}'.format(tiempoEspera)
                tiempoServicio = len(dsc.elementos)
                dsc.putntuacion = float(tiempoEspera) / tiempoServicio
                if mayorPuntuacion < dsc.putntuacion:
                    mayorPuntuacion = dsc.putntuacion
        #print 'Mayor Stretch: {}'.format(mayorPuntuacion)
        return mayorPuntuacion


    @classmethod
    def criterio_por_jitter(cls, cronograma, consultasEncubiertas, planificador):
        print "SELECCION POR JITTER"
        datosSubconsultas = cls._obetener_datos_subconsultas(cronograma, consultasEncubiertas, planificador)
        valorMaximoJitter = float(0)
        # las sub consultas contienen los elementos presentes en el cronograma
        mayorPuntuacion = 0
        for dsc in datosSubconsultas:
            if len(dsc.elementos) > 1:
                index = []
                for e in dsc.elementos:
                    index.append(cronograma.items.index(e))
                #ordenar de menor a mayor
                index.sort()
                #calcular la sumatoria de las distancias de los indices
                sumatoriaDistancias = 0
                anterior = 0
                for d in index:
                    sumatoriaDistancias += (d - anterior)
                    anterior = d
                #numero de itemes que responden a la sub consulta y estan en el cronograma
                elementosEnCronograma = len(dsc.elementos)
                dsc.puntuacion = float(sumatoriaDistancias) / (elementosEnCronograma-1)
                if mayorPuntuacion < dsc.puntuacion:
                    mayorPuntuacion = dsc.puntuacion
        #print 'Mayor Jitter: {}'.format(mayorPuntuacion)
        return mayorPuntuacion

    @classmethod
    def _obetener_datos_consultas_encubiertas(cls, consultasEncubiertas, planificador):
        datosDeConsultasEncubiertas = []
        for Q in consultasEncubiertas:
            scoreConsultaEncubierta = ScoreConsultaEncubierta(Q)
            for q in Q.consultas:
                scoreSubConsulta = ScoreSubConsulta(q)
                scoreConsultaEncubierta.subconsultas.append(scoreSubConsulta)
                scoreSubConsulta.elementos += planificador.obtener_elementos_desde_subconsulta(q)
            datosDeConsultasEncubiertas.append(scoreConsultaEncubierta)
        return datosDeConsultasEncubiertas

    @classmethod
    def _obetener_datos_elementos_consultas_encubiertas(cls, consultasEncubiertas, planificador):
        datosElementos = []
        for Q in consultasEncubiertas:
            for e in planificador.obtener_elementos_desde_consulta_encubierta(Q):
                # comprobacion de que el elemento no se repita en el evaluador
                my_filter_iter = filter(lambda s: s.elemento == e, datosElementos)
                if len(my_filter_iter) == 1: #si el elemento se repite en el evaluador solo guarda la consulta
                    my_filter_iter[0].consultasEncubiertas.append(Q)
                if len(my_filter_iter) == 0:#se el elemento no esta en el evaluados se guarda el elemento y la consulta
                    s = ScoreElemento(e)
                    s.consultasEncubiertas.append(Q)
                    datosElementos.append(s)
        return datosElementos

    @classmethod
    def _obetener_datos_subconsultas(cls, cronograma, consultasEncubiertas, planificador):
        datosSubconsultas = []
        for Q in consultasEncubiertas :
            for q in Q.consultas:
                my_filter_iter = filter(lambda s: s.subConsulta == q, datosSubconsultas)
                if len(my_filter_iter) == 0:
                    s = ScoreSubConsulta(q)
                    s.elementos += planificador.obtener_elementos_desde_subconsulta(q)
                    datosSubconsultas.append(s)

        for s in datosSubconsultas:
            s.elementos = list(set(s.elementos) & set(cronograma.items))


        return datosSubconsultas