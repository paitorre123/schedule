from src.consulta.elemento import ElementoFinBroadcast
import os

class Ajuste(object):
    EFECTIVIDAD = 3
    conAjuste = True
    def __init__(self):
        #self.maximoLargoPrograma = 500 # valor M
        self.numeroDeTransmisiones =  0 # valor A : efectividad del programa
        self.consultasRespondidas = []
        self.consultasAResponder = []
        self.consultasNuevas = []
        self.cronogramaPendiente = []
        self.programaActual = []
        self.historialDeProgramas = []


    def iniciar_planificacion_ajustada(self, planificador, function, methodScheduler ):
        #print 'DATOS INICIO'
        #self.imprimir(planificador)
        print ':::::::::::::::::::::::::::::::::::::'
        print '::: INICIO PLANIFICACION AJUSTADA :::'

        print'::::::::::::::::::::::::::'
        print'HAY {} CUEs EN EL AJUSTE'.format(len(self.consultasNuevas))
        print'::::::::::::::::::::::::::'
        #os.system('pause')

        if len(self.consultasNuevas) > 0 and self.numeroDeTransmisiones < 1:
            print 'INGRESO 1'
            if self.conAjuste:
                self.incorporar(planificador, function, methodScheduler)

            else:
                self.reemplazar(planificador, function, methodScheduler)

            self.numeroDeTransmisiones = self.EFECTIVIDAD
            #fase de actualizacion de los datos
            if len(self.cronogramaPendiente) > planificador.sizeCronograma:
                planificador.cronograma.items = self.programaActual[0: planificador.sizeCronograma]
                self.cronogramaPendiente = self.programaActual[planificador.sizeCronograma: len(self.programaActual)]
            else:
                planificador.cronograma.items = self.programaActual[0: len(self.programaActual)]
                self.numeroDeTransmisiones -=1
                ##LLEGAMOS AL FINAL DEL CRONOGRAMA
                planificador.cronograma.items.append(ElementoFinBroadcast())
                #:::::INDETIFICAR DE ALGUNA FORMA:::::
                #os.system('pause')
                if self.numeroDeTransmisiones == 0:
                    self.cronogramaPendiente = []
                    #self.numeroDeTransmisiones = self.EFECTIVIDAD
                else:
                    self.cronogramaPendiente = self.programaActual

            # os.system('pause')
        else:
            print 'INGRESO 2'
            if len(self.cronogramaPendiente) > planificador.sizeCronograma:
                print 'MAYOR'
                planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
                self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]
            else:
                print 'MENOR IGUAL'
                planificador.cronograma.items = self.cronogramaPendiente[0: len(self.cronogramaPendiente)]
                self.numeroDeTransmisiones -=1
                ##LLEGAMOS AL FINAL DEL CRONOGRAMA
                planificador.cronograma.items.append(ElementoFinBroadcast())
                #:::::INDETIFICAR DE ALGUNA FORMA:::::
                #os.system('pause')
                if self.numeroDeTransmisiones == 0:
                    self.cronogramaPendiente = []
                    #self.numeroDeTransmisiones = self.EFECTIVIDAD
                else:
                    self.cronogramaPendiente = self.programaActual

        #print ':::::::::::::::::::::::::::::::::::::'
        #print 'DATOS FINAL'
        #self.imprimir(planificador)

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
        programaAnterior = self.programaActual
        # 2. pasar consultas nuevas al planificador
        planificador.consultasNuevas = self.consultasNuevas
        # 3.seleccion del metodo de planificacion
        if function != None:
            methodScheduler(function)
        else:
            methodScheduler()
        # 4. reinicio de las consulta nuevas del ajustador
        self.consultasNuevas = []


        #self.programaActual.append(ElementoFinBroadcast())
        #programa actual es mayor que el anterior y tiene mas que el limite

        if len(self.programaActual) > len(programaAnterior) and len(programaAnterior) <= planificador.sizeCronograma and len(self.programaActual) > planificador.sizeCronograma:

            # . se deja el cronograma como pendiente
            self.cronogramaPendiente = self.programaActual
            # . asignamcion de elementos pendientes en el cronograma
            planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
            # . asignacion como cronograma pendiente de la parte que no puede entrar en el cronograma
            self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]




        elif len(self.programaActual) < len(programaAnterior) and len(programaAnterior) > planificador.sizeCronograma and len(self.programaActual) <= planificador.sizeCronograma:

            tallaProgramaAnterior = len(programaAnterior)
            # .
            for e in self.programaActual:
                if e in programaAnterior:
                    programaAnterior.remove(e)
            # .

            # .
            if len(programaAnterior) > tallaProgramaAnterior - len(self.programaActual):
                self.programaActual = list(programaAnterior[0: tallaProgramaAnterior - len(self.programaActual)]) + list(self.programaActual)
            else:
                 self.programaActual = list(programaAnterior) + list(self.programaActual)
            # . se deja el cronograma como pendiente
            self.cronogramaPendiente = self.programaActual
            # . asignamcion de elementos pendientes en el cronograma
            planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
            # . asignacion como cronograma pendiente de la parte que no puede entrar en el cronograma
            self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]


        elif len(self.programaActual) < len(programaAnterior) and len(programaAnterior) > planificador.sizeCronograma and len(self.programaActual) > planificador.sizeCronograma:

            # . se deja el cronograma como pendiente
            self.cronogramaPendiente = self.programaActual
            # . asignamcion de elementos pendientes en el cronograma
            planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
            # . asignacion como cronograma pendiente de la parte que no puede entrar en el cronograma
            self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]

        elif len(self.programaActual) < len(programaAnterior) and len(programaAnterior) < planificador.sizeCronograma:
            # . se deja el cronograma como pendiente
            if len(self.programaActual) + len(programaAnterior) <= planificador.sizeCronograma:
                # .
                for e in self.programaActual:
                    if e in programaAnterior:
                        programaAnterior.remove(e)
                self.programaActual = list(programaAnterior) + list(self.programaActual)

                self.cronogramaPendiente = self.programaActual
                # . asignamcion de elementos pendientes en el cronograma
                planificador.cronograma.items = self.cronogramaPendiente[0: len(self.cronogramaPendiente)]

            else:
                # . se deja el cronograma como pendiente
                self.cronogramaPendiente = self.programaActual
                # . asignamcion de elementos pendientes en el cronograma
                planificador.cronograma.items = self.cronogramaPendiente[0: len(self.cronogramaPendiente)]



        elif len(self.programaActual) > len(programaAnterior) and len(programaAnterior) > planificador.sizeCronograma:
            # . se deja el cronograma como pendiente
            self.cronogramaPendiente = self.programaActual
            # . asignamcion de elementos pendientes en el cronograma
            planificador.cronograma.items = self.cronogramaPendiente[0: planificador.sizeCronograma]
            # . asignacion como cronograma pendiente de la parte que no puede entrar en el cronograma
            self.cronogramaPendiente = self.cronogramaPendiente[planificador.sizeCronograma: len(self.cronogramaPendiente)]
        #x.




    def imprimir(self, planificador):
        print 'AJUSTE'
        print 'Programa actual: {}'.format(len(self.programaActual))
        print 'tamanio del cronograma: {}'.format(len(planificador.cronograma.items))
        print 'Consultas Respondidas: {}'.format(len(self.consultasRespondidas))
        print 'Consultas A Responder: {}'.format(len(self.consultasAResponder))
        print 'Consultas Nuevas: {}'.format(len(self.consultasNuevas))
        print 'Elementos Pendientes: {}'.format(len(self.cronogramaPendiente ))
        os.system('pause')

