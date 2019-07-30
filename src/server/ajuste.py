from src.consulta.elemento import ElementoFinBroadcast
import os

class Ajuste(object):
    EFECTIVIDAD = 3
    conAjuste = True
    def __init__(self):
        self.maximoLargoPrograma = 500 # valor M
        self.numeroDeTransmisiones = self.EFECTIVIDAD # valor A : efectividad del programa
        self.consultasRespondidas = []
        self.consultasAResponder = []
        self.consultasNuevas = []
        self.cronogramaPendiente = []
        self.programaActual = []
        self.historialDeProgramas = []


    def iniciar_planificacion_ajustada(self, planificador, function, methodScheduler ):
        self.imprimir()
        if len(self.cronogramaPendiente)>0 and self.numeroDeTransmisiones > 0:
            if len(self.cronogramaPendiente)> 0:
                if len(self.cronogramaPendiente) > planificador.sizeCronograma:
                    planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
                    self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]
                else:
                    planificador.cronograma.items = self.cronogramaPendiente[0: len(self.cronogramaPendiente)]
                    self.numeroDeTransmisiones -=1
                    ##LLEGAMOS AL FINAL DEL CRONOGRAMA
                    planificador.cronograma.items.append(ElementoFinBroadcast())
                    #:::::INDEICAR DE ALGUNA FORMA:::::
                    #os.system('pause')
                    if self.numeroDeTransmisiones == 0:
                        self.cronogramaPendiente = []
                        self.numeroDeTransmisiones = self.EFECTIVIDAD
                    else:
                        self.cronogramaPendiente = self.programaActual
        else:
            if self.conAjuste:
                self.incorporar(planificador, function, methodScheduler)
            else:
                self.reemplazar(planificador, function, methodScheduler)
            #os.system('pause')
        self.imprimir()

    def reemplazar(self, planificador, function, methodScheduler ):
        # 2. pasar consultas nuevas al planificador
        planificador.consultasNuevas = self.consultasNuevas
        # 3.seleccion del metodo de planificacion
        if function != None:
              methodScheduler(function)
        else:
            methodScheduler()
        # 4. reinicio de las consulta nuevas del ajustador
        self.consultasNuevas = []
        # 5. se deja el cronograma como pendiente
        self.cronogramaPendiente = self.programaActual
        # 6. asignamcion de elementos pendientes en el cronograma
        planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
        # 7. asignacion como cronograma pendiente de la parte que no puede entrar en el cronograma
        self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]


    def incorporar(self, planificador, function, methodScheduler ):
        # 1. rescate del cronograma anterior a la planificacion
        programaAnteior = self.programaActual
        # 2. pasar consultas nuevas al planificador
        planificador.consultasNuevas = self.consultasNuevas
        # 3.seleccion del metodo de planificacion
        if function != None:
            methodScheduler(function)
        else:
            methodScheduler()
        # 4. reinicio de las consulta nuevas del ajustador
        self.consultasNuevas = []
        # 5. elementos de las consultas nuevas que no estan en el cronograma
        delta = list(set(self.programaActual) - set(programaAnteior))
        # 6. cuento el largo de delta es menor al cronogrma anterior se sustituyen alguna de las consultas
        if len(delta) < programaAnteior:
            # 6.1 se actualiza el progrma actual con el parte de cronograma aneterior
            self.programaActual = programaAnteior[0:len(programaAnteior) - len(self.programaActual)] + self.programaActual
            # 6.2 se deja el cronograma como pendiente
            self.cronogramaPendiente = self.programaActual
            # 6.3 asignamcion de elementos pendientes en el cronograma
            planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
            # 6.4 asignacion como cronograma pendiente de la parte que no puede entrar en el cronograma
            self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]

    def imprimir(self):
        print 'AJUSTE'
        print 'Consultas Respondidas: {}'.format(len(self.consultasRespondidas))
        print 'Consultas A Responder: {}'.format(len(self.consultasAResponder))
        print 'Consultas Nuevas: {}'.format(len(self.consultasNuevas))
        print 'Elementos Pendientes: {}'.format(len(self.cronogramaPendiente ))

