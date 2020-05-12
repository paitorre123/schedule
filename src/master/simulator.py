from src.server.servidor import Servidor
import time
import matplotlib.pyplot as plt
import os
import numpy as np
from decimal import Decimal
from src.server.ajuste import Ajuste
from src.pruebas.manejoExcel import ManejoExcel
import math
import pylab
from src.manejoDeDatos.ManejoDeDatos import ManejoDeDatos


class Simulator(object):
    ALL_SCHEDULE = False
    CICLOS = 4000
    def __init__(self, grid, time, size, planificador, ajuste, criterio):
        self.grid = grid
        self.time = time
        self.schedule = None
        self.painter = None
        self.users = []
        self.percentage = 1
        self.size = size
        self.historialDeCronogramas = []
        self.ajuste = Ajuste()
        print 'inicio de simulacion'
        self._generarServidor(planificador, ajuste, criterio)
        self._generarUsuarios()


    def start(self):
        self._construir_consultas()
        self._generar_cronograma_inicial()
        self._difundirCronograma()
        print 'Fase inicial terminada'
        while self.time.time < self.CICLOS:
            #self._construir_consultas()
            self.servidor.generar_cronograma(self.time, self.ajuste)
            self._difundirCronograma()

        while self._clientes_todas_sus_cues_respondidas() == False:
            #self._construir_consultas()
            self.servidor.generar_cronograma(self.time, self.ajuste)
            self._difundirCronograma()
        print 'Los clientes tiene todas sus cues respondidas'

        while self.ALL_SCHEDULE == False:
            self.servidor.generar_cronograma(self.time, self.ajuste)
            self._difundirCronograma()
        print 'se transmitiron todos los programas completos'




        #time.sleep(1)
        '''
        #PRUEBA 1
        if self.time.time>3000 and secuencia == 1:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion Norte'
            secuencia+=1
        if self.time.time>6000 and secuencia == 2:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion Noroeste'
            secuencia += 1
        if self.time.time>9000 and secuencia == 3:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion Noreste'
            secuencia += 1
        if self.time.time>12000 and secuencia == 4:
            for user in self.users:
                user.cardinalPointsProbability = 'Random'
            secuencia += 1
        '''

        '''
        # PRUEBA 2
        if self.time.time > 3000 and secuencia == 1:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion Noroeste'
            secuencia += 1
        if self.time.time > 6000 and secuencia == 2:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion centro'
            secuencia += 1
        if self.time.time > 9000 and secuencia == 3:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion sureste'
            secuencia += 1
        if self.time.time > 12000 and secuencia == 4:
            for user in self.users:
                user.cardinalPointsProbability = 'Random'
            secuencia += 1
        '''

        '''
        # PRUEBA 3.1
        if self.time.time > 3000 and secuencia == 1:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion Noroeste'
            secuencia += 1
        if self.time.time > 6000 and secuencia == 2:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion Norte'
            secuencia += 1
        if self.time.time > 9000 and secuencia == 3:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion centro'
            secuencia += 1
        if self.time.time > 12000 and secuencia == 4:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion sur'
            secuencia += 1
        '''
        '''
        # PRUEBA 3.2
        if self.time.time > 3000 and secuencia == 1:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion Noreste'
            secuencia += 1
        if self.time.time > 6000 and secuencia == 2:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion este'
            secuencia += 1
        if self.time.time > 9000 and secuencia == 3:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion sureste'
            secuencia += 1
        if self.time.time > 12000 and secuencia == 4:
            for user in self.users:
                user.cardinalPointsProbability = 'Uniforme Direccion sur'
            secuencia += 1
        '''

        '''ManejoExcel.fileName = 'DatosSimulacion1.4'
        file=ManejoExcel.crear_archivo_excel()
        hojaUser=ManejoExcel.crear_hoja_en_archivo(file, 'Pocision usuarios')
        ManejoExcel.escribir_datos_usuarios(hojaUser, self.users)
        file.close()'''


        '''
        ManejoExcel.fileName = 'PosicionPuntosDeInteres'
        file = ManejoExcel.crear_archivo_excel()
        hojaPoi = ManejoExcel.crear_hoja_en_archivo(file, 'posicion poi')
        ManejoExcel.escribir_datos_poi(hojaPoi, self.grid)
        file.close()
        '''
        '''
        x = []
        y = []
        for user in self.users:
            print 'user position: {},{}'.format(user.point.pointX, user.point.pointY)
            for data in user.randomWalk.rastro:
                print '{}'.format(data)
                x.append(data[0])
                y.append(data[1])
        plt.scatter(x, y, s=1)
        plt.plot(x, y)
        plt.show()
        '''


        #datos para la carga de trabajo
        #1.numero de cues respondidas
        # en tiempo-1: [1000- 5000]
        #self._numero_cues_respondidas()
        #2.numero de cues que arriban
        #en tiempo-1: [1000-5000]
        #self._cues_arrivan_servidor()

        #self._tiempo_de_espera_servidor()
        #self._tiempo_de_espera_cliente()
        #self._carga_de_trabajo_cliente()
        #self._carga_de_trabajo_servidor()

        #self._utilidad_total_elementos()
        #self._utilidad_total_elementos_exactos()
        #self._obsolecencia_cliente()
        #self._numero_cues_enviadas()
        #self._numero_cues_no_enviadas()
        #self._anonimato_cues()

        #1- guardar las cues que crearon los usuarios
        ManejoDeDatos.escribir_user_created_cues(self.users)
        print 'cues de usuarios'
        ManejoDeDatos.escribir_item_cues(self.users)
        print 'elementos de cues'
        ManejoDeDatos.escribir_item_subconsultas(self.users)
        print 'elementos de sub consultas'
        ManejoDeDatos.numero_cues_respondidas(self.users, self.historialDeCronogramas)
        print 'cues respondidas'
        ManejoDeDatos.tiempo_de_espera_cues_exactas(self.users)
        print 'tiempo de espera de consultas'
        ManejoDeDatos.tiempo_de_espera_cues_virtuales(self.users)
        print 'tiempo de espera cues'
        ManejoDeDatos.numero_elementos_exactos_cues(self.users)
        print 'numero elementos exactos'
        ManejoDeDatos.numero_elementos_virtuales_cues(self.users)
        print 'numero elementos virtuales'
        ManejoDeDatos.cues_exactas_que_usan_elementos(self.users, self.historialDeCronogramas)
        print 'cues exactas que usan elementos'
        ManejoDeDatos.cues_obsoletas(self.users, self.grid)
        print 'cues obsoletas'

        print '::::::::::::::::::::::::::::::FINALIZADO::::::::::::::::::::::::::::::'


        #os.system('pause')

    def _clientes_todas_sus_cues(self):
        for user in self.users:
            if len(user.almacenes) < user.CUES_USUARIOS:
                return False
        return True
    def _clientes_todas_sus_cues_respondidas(self):
        #todos los clientes crearon sus x consultas
        if self._clientes_todas_sus_cues() == True:
            for user in self.users:
                if  user.almacenes[user.CUES_USUARIOS - 1].is_completed() == False:
                        #un cliente no respondio su ultima consulta
                        return False
            #todos los clientes respondieron su ultima consulta
            return True
        #hay clientes que aun no completan sus x consultas
        return False

    def _numero_cues_respondidas(self):
        print 'CUES RESPONDIDAS'
        ncr = []
        total = 0
        nSubcronograma = 1
        time = 1
        for subCronograma in self.historialDeCronogramas:
            # print 'Subcronograma: {}'.format(nSubcronograma)
            numeroRespondidas = 0
            for elemento in subCronograma.items:
                if elemento.__class__.__name__ is not 'ElementoFinBroadcast':
                    # print '    ->Elemento: {} time: {}'.format(elemento.puntoDeInteres, time)
                    # print '        ->numero CUEs que responde: {}'.format(self._numeroCUESQueResponde(time))
                    numeroRespondidas += self._numeroCUESQueResponde(time)
                time += 1
            #print '({},{})'.format(nSubcronograma, numeroRespondidas)
            ncr.append([nSubcronograma, numeroRespondidas])
            nSubcronograma += 1
        for numero in ncr:
            total += numero[1]
            if numero[0] == 10 or numero[0] == 20 or numero[0] == 30 or numero[0] == 40 or numero[0] == 50:
                print '({},{})'.format(numero[0]*100, total)



    def _tiempo_de_espera_cliente(self):
        print 'TIEMPO ESPERA CLIENTE'
        for user in self.users:
            #print 'Usuario: {}'.format(user)
            #print '-->numero CUEs: {}'.format(len(user.almacenes))
            cueId = 0
            #print 'CUE: {}'.format(cueId)
            tiempoPromedioEspera = 0
            for q in user.almacenes:
                #print  'tiempo-1 de llegada al servidor: {}'.format(q.consultaEncubierta.arriveInServerTime)
                if len(q.elementosEncontradosReales) > 0 and len(q.tiempoElementosEncontradosArtificiales):
                    #print '-->Elementos por el cliente'
                    tiempoPrimerElementoReal = q.tiempoElementosEncontradosReales[0]
                    tiempoUltimoElementoReal = q.tiempoElementosEncontradosReales[
                        len(q.tiempoElementosEncontradosReales) - 1]
                    #print '   ->primer elemento: {}'.format(tiempoPrimerElementoReal)
                    #print '   ->ultimo elemento: {}'.format(tiempoUltimoElementoReal)
                    #print '   <tiempo-1 de espera cliente>{}'.format(tiempoUltimoElementoReal - tiempoPrimerElementoReal)
                    tiempoPromedioEspera += tiempoUltimoElementoReal - tiempoPrimerElementoReal

                cueId += 1
            tiempoPromedioEspera /= len(user.almacenes)
            print "({},{})".format(user,tiempoPromedioEspera )

    def _tiempo_de_espera_servidor(self):
        print 'TIEMPO ESPERA SERVIDOR'
        for user in self.users:
            #print 'Usuario: {}'.format(user)
            #print '-->numero CUEs: {}'.format(len(user.almacenes))
            cueId = 0
            #print 'CUE: {}'.format(cueId)
            tiempoPromedioEspera = 0
            for q in user.almacenes:
                #print  'tiempo-1 de llegada al servidor: {}'.format(q.consultaEncubierta.arriveInServerTime)
                if len(q.elementosEncontradosReales) > 0 and len(q.tiempoElementosEncontradosArtificiales):
                    #print '-->Elementos por el cliente'
                    tiempoPrimerElementoReal = q.tiempoElementosEncontradosReales[0]
                    tiempoUltimoElementoReal = q.tiempoElementosEncontradosReales[
                        len(q.tiempoElementosEncontradosReales) - 1]
                    #print '   ->primer elemento: {}'.format(tiempoPrimerElementoReal)
                    #print '   ->ultimo elemento: {}'.format(tiempoUltimoElementoReal)
                    #print '   <tiempo-1 de espera cliente>{}'.format(tiempoUltimoElementoReal - tiempoPrimerElementoReal)

                    #print '-->Elementos por el servidor'
                    tiempoPrimerElementoVirtual = q.tiempoElementosEncontradosArtificiales[0]
                    tiempoUltimoElementoVirtual = q.tiempoElementosEncontradosArtificiales[
                        len(q.tiempoElementosEncontradosArtificiales) - 1]
                    tiemposPrimero = []
                    tiemposPrimero.append(tiempoPrimerElementoReal)
                    tiemposPrimero.append(tiempoPrimerElementoVirtual)
                    tiemposUltimo = []
                    tiemposUltimo.append(tiempoUltimoElementoReal)
                    tiemposUltimo.append(tiempoUltimoElementoVirtual)
                    #print '   ->primer elemento: {}'.format(min(tiemposPrimero))
                    #print '   ->ultimo elemento: {}'.format(max(tiemposUltimo))
                    #print '   <tiempo-1 de espera servidor>{}'.format(max(tiemposUltimo) - min(tiemposPrimero))
                    tiempoPromedioEspera += max(tiemposUltimo) - min(tiemposPrimero)
                cueId += 1
            tiempoPromedioEspera /= len(user.almacenes)
            print "({},{})".format(user,tiempoPromedioEspera )

    def _carga_de_trabajo_servidor(self):
        print 'CARGA DE TRABAJO SERVIDOR'
        nSubcronograma = 1
        time = 1
        for subCronograma in self.historialDeCronogramas:
            #print 'Subcronograma: {}'.format(nSubcronograma)
            numeroRespondidas = 0
            for elemento in subCronograma.items:
                if elemento.__class__.__name__ is not 'ElementoFinBroadcast':
                    #print '    ->Elemento: {} time: {}'.format(elemento.puntoDeInteres, time)
                    #print '        ->numero CUEs que responde: {}'.format(self._numeroCUESQueResponde(time))
                    numeroRespondidas += self._numeroCUESQueResponde(time)
                time+=1
            print '({},{})'.format(nSubcronograma, numeroRespondidas)
            nSubcronograma+=1

    def _cues_arrivan_servidor(self):
        print 'CUES QUE LLEGAN AL SERVIDOR'
        for datos in self.servidor.historialDeCUEs:
            print '({},{})'.format(datos[1], datos[0])

    def _carga_de_trabajo_cliente(self):
        print 'CARGA DE TRABAJO CLIENTE'
        nSubcronograma = 1
        time = 1
        for subCronograma in self.historialDeCronogramas:
            #print 'Subcronograma: {}'.format(nSubcronograma)
            numeroRespondidas = 0
            for elemento in subCronograma.items:
                if elemento.__class__.__name__ is not 'ElementoFinBroadcast':
                    #print '    ->Elemento: {} time: {}'.format(elemento.puntoDeInteres, time)
                    #print '        ->numero CUEs que responde: {}'.format(self._numeroConsultasExactasQueResponde(time))
                    numeroRespondidas += self._numeroConsultasExactasQueResponde(time)
                time += 1
            print '({},{})'.format(nSubcronograma, numeroRespondidas)
            nSubcronograma += 1

    def _utilidad_total_elementos(self):
        print 'UTILIDAD TOTAL'
        print '(cronograma, numero cues que usan al cronograma)'
        nSubcronograma = 1
        time = 1
        for subCronograma in self.historialDeCronogramas:
            #print 'Subcronograma: {}'.format(nSubcronograma)
            numeroDeUso = 0
            for elemento in subCronograma.items:
                if elemento.__class__.__name__ is not 'ElementoFinBroadcast':
                    #print '    ->Elemento: {} time: {}'.format(elemento.puntoDeInteres, time)
                    #print '        ->numero CUEs que la usan: {}'.format(self._numeroCUESQueLoUsan(time))
                    numeroDeUso += self._numeroCUESQueLoUsan(time)
                time += 1
            print '({},{})'.format(nSubcronograma, numeroDeUso)
            nSubcronograma += 1

    def _utilidad_total_elementos_exactos(self):
        print 'UTILIDAD DE ELEMENTOS EXATCTOS'
        print '(cronograma, numero consultas exactas que usan al cronograma)'
        nSubcronograma = 1
        time = 1
        for subCronograma in self.historialDeCronogramas:
            #print 'Suncronograma: {}'.format(nSubcronograma)
            numeroDeUso = 0
            for elemento in subCronograma.items:
                if elemento.__class__.__name__ is not 'ElementoFinBroadcast':
                    #print '    ->Elemento: {} time: {}'.format(elemento.puntoDeInteres, time)
                    #print '        ->numero CUEs que la usan: {}'.format(self._numeroCUESExactasQueLoUsan(time))
                    numeroDeUso += self._numeroCUESExactasQueLoUsan(time)
                time += 1
            print '({},{})'.format(nSubcronograma, numeroDeUso)
            nSubcronograma += 1

    def _obsolecencia_cliente(self):
        print 'OBSOLECENCIA CLIENTE RESPECTO A LA REGION DE ENCUBRIMIENTO'
        #CONSULTAS EN LAS QUE EL CLIENTE SE SALIO DE LA REGION DE ENCUBRIMIENTO
        for user in self.users:
            #print 'Usuario: {}'.format(user)
            #print '    -->numero CUEs: {}'.format(len(user.almacenes))
            cueId = 0
            numeroObsoletas = 0
            for q in user.almacenes:
                #print '        CUE: {}'.format(cueId)
                #print  '           tiempo-1 de llegada al servidor: {}'.format(q.consultaEncubierta.arriveInServerTime)
                if len(q.elementosEncontradosReales) > 0:
                    tiempoPrimerElementoReal = int(q.tiempoElementosEncontradosReales[0])
                    tiempoUltimoElementoReal = int(q.tiempoElementosEncontradosReales[
                        len(q.tiempoElementosEncontradosReales) - 1])
                    xInicial = user.randomWalk.obtener_psicion_en_tiempo(tiempoPrimerElementoReal-1)[0]
                    yInicial = user.randomWalk.obtener_psicion_en_tiempo(tiempoPrimerElementoReal-1)[1]
                    #print '            posicion inicial: {},{}'.format(xInicial,yInicial)
                    xFinal = user.randomWalk.obtener_psicion_en_tiempo(tiempoUltimoElementoReal-1)[0]
                    yFinal = user.randomWalk.obtener_psicion_en_tiempo(tiempoUltimoElementoReal-1)[1]
                    #print '            posicion final: {},{}'.format(xFinal, yFinal)
                    distancia = math.sqrt( math.pow((xFinal-xInicial), 2) + math.pow((yFinal-yInicial), 2) )
                    #print '            distancia entre posiciones: {}'.format(distancia)
                    pasos = tiempoUltimoElementoReal - tiempoPrimerElementoReal
                    #print '            numero de pasos: {}'.format(pasos)
                    #celdaInicial = self.grid.cellOfUser(xInicial, yInicial)
                    #print '            celda inicial: {}'.format(celdaInicial)
                    celdaFinal = self.grid.cellOfUser(xFinal, yFinal)
                    #print '            celda final: {}'.format(celdaFinal)
                    if distancia > celdaFinal.side*3:
                        numeroObsoletas += 1
                cueId += 1
            print '({},{})'.format(user, numeroObsoletas)

    def _numero_cues_enviadas(self):
        print 'CUES ENVIADAS AL SERVIDOR Y RESPONDIDAS'
        enviadas = 0
        for user in self.users:
            for q in user.almacenes:
                if q.consultaEncubierta.arriveInServer:
                    if len(q.elementosEncontradosReales) > 0:
                        enviadas += 1
        print '|enviadas y respondidas|: {}'.format(enviadas)

    def _numero_cues_no_enviadas(self):
        print 'CUES NO ENVIADAS AL SERVIDOR Y RESPONDIDAS'
        noenviadas = 0
        for user in self.users:
            for q in user.almacenes:
                if not q.consultaEncubierta.arriveInServer:
                    if len(q.elementosEncontradosReales) > 0:
                        noenviadas += 1
        print '|no enviadas y respondidas|: {}'.format(noenviadas)

    def _anonimato_cues(self):
        print 'K ANONIMATO DE CUES'
        cue = 0
        for user in self.users:
            for q in user.almacenes:
                if q.consultaEncubierta.arriveInServer:
                    if len(q.elementosEncontradosReales) > 0:
                        print '({},{})'.format(cue, len(q.consultaEncubierta.consultas))
                        cue += 1

    def _numeroCUESExactasQueLoUsan(self, time):
        numeroDeUsadas = 0
        for user in self.users:
            for q in user.almacenes:
                if time in q.tiempoElementosEncontradosReales:
                    numeroDeUsadas += 1
                    break
        return numeroDeUsadas

    def _numeroCUESQueLoUsan(self, time):
        numeroDeUsadas = 0
        for user in self.users:
            for q in user.almacenes:
                if time in q.tiempoElementosEncontradosReales:
                    numeroDeUsadas += 1
                    break
                if time in q.tiempoElementosEncontradosArtificiales:
                    numeroDeUsadas += 1
                    break
        return numeroDeUsadas

    def _numeroCUESQueResponde(self, time):
        numeroDeRespondidas = 0
        for user in self.users:

            for q in user.almacenes:

                if len(q.elementosEncontradosReales) > 0:

                    tiempoPrimerElementoReal = q.tiempoElementosEncontradosReales[0]
                    tiempoUltimoElementoReal = q.tiempoElementosEncontradosReales[len(q.tiempoElementosEncontradosReales) - 1]
                    if len(q.tiempoElementosEncontradosArtificiales)>0:
                        tiempoPrimerElementoVirtual = q.tiempoElementosEncontradosArtificiales[0]
                        tiempoUltimoElementoVirtual = q.tiempoElementosEncontradosArtificiales[len(q.tiempoElementosEncontradosArtificiales) - 1]

                    tiemposPrimero = []
                    tiemposPrimero.append(tiempoPrimerElementoReal)
                    tiemposPrimero.append(tiempoPrimerElementoVirtual)
                    tiemposUltimo = []
                    tiemposUltimo.append(tiempoUltimoElementoReal)
                    tiemposUltimo.append(tiempoUltimoElementoVirtual)

                    if time == max(tiemposUltimo):
                        numeroDeRespondidas+=1
        return numeroDeRespondidas

    def _numeroConsultasExactasQueResponde(self, time):
        numeroDeRespondidas = 0
        for user in self.users:

            for q in user.almacenes:

                if len(q.elementosEncontradosReales) > 0:
                    tiempoUltimoElementoReal = q.tiempoElementosEncontradosReales[len(q.tiempoElementosEncontradosReales) - 1]
                    if time == tiempoUltimoElementoReal:
                        numeroDeRespondidas+=1

        return numeroDeRespondidas

    def _generar_cronograma_inicial(self):
        self.servidor.generar_cronograma_inicial()

    def _construir_consultas(self):
        '''
            LOS USUARIOS  FORMAN SUS CONSULTAS
            DE MODO QUE, TODOS, TIENEN UNA,
            SIN EMBARGO, NO TODOS LA SOLICITAN
            AL SERVIDOS LBS.
        '''
        for user in self.users:
            user.obtener_consulta(self.grid)

    def _enviar_CUE_servidor(self):
        probability = []
        for _ in self.users:
            probability.append(Decimal(1) / len(self.users))
            # SELECCIONAR UN PORCENTAJE
            # DE CLIENTES QUE CONSULTAN
        self.servidor.usuarios = None
        self.servidor.usuarios = np.random.choice(self.users, int(len(self.users) * self.percentage), p=probability, replace=False).tolist()
        # print 'SELECCION DE USUARIOS'
        usuariosMeta = []
        for x in self.servidor.usuarios:
            usuariosMeta.append(x)

        for usuario in usuariosMeta:
            #print 'Usuario: {}'.format(usuario)
            if usuario.is_waiting_response():#or usuario._anterior_consulta_completada()
                # print 'Removiendo Usuario: {}'.format(usuario)
                self.servidor.usuarios.remove(usuario)
        print ':::::::::::::::::::::::::::::::'
        print 'Se enviaron {} CUEs al servidor'.format(len(self.servidor.usuarios))
        print ':::::::::::::::::::::::::::::::'

    def _generarServidor(self, planificador, ajuste, criterio):
        self.servidor = Servidor(grid=self.grid, size=self.size,planificador= planificador, ajuste=ajuste,criterio=criterio)


    def _generarUsuarios(self):
        for user in self.users:
            #print '{},{}'.format(user.point.pointX, user.point.pointY)
            user.randomWalk.rastro = [[user.point.pointX, user.point.pointY]]
            user.randomWalk.pasos = 0

    def _difundirCronograma(self):
        print ':::::::::::::::::::::::::'
        print 'TRANSMITIENDO CRONOGRAMA'
        print 'TALLA: {}'.format(len(self.servidor.cronograma.items))

        #GUARDANDO CRONOGRAMA
        self.historialDeCronogramas.append(self.servidor.cronograma)

        for item in self.servidor.cronograma.items:
            self.time.time += 1
            if item.__class__.__name__ is 'ElementoFinBroadcast':
                print '::: FIN DE CRONOGRAMA :::'
                self.ALL_SCHEDULE = True
                for usuario in self.users:
                    usuario.consultaEncubierta.watchFinalSchedule = True
                #os.system('pause')
                self._construir_consultas()
                self._enviar_CUE_servidor()
                #self._construir_consultas()
                print ':::::::::::::::::::::::::'
                break
                #os.system('pause')
            #print "Time : {}".format(self.time.time)
            #print '{}'.format(item)2
            for usuario in self.users:
                usuario.caminar(self.grid)
                #self.painter.canvas.after(50)
                #Borrada para sacar entorno grafico#self.painter.canvas.update()
            #self.historialDeCronogramas.append([item, self.time.time])
            for usuario in self.users:
                usuario.observar_item(item)
            #llevar a cabo la tarea del usuario
            #1. nueva consulta
            #time.sleep(1)
            self.ALL_SCHEDULE = False

        '''
        for user in self.users:
            print '-->Usuario: {}'.format(user)
            for almacen in user.almacenes:
                print '          ID Consulta Encubierta: {}, Momento de llegada: {}'.format(almacen.subconsultaReal, almacen.subconsultaReal.tiempoLlegadaServidor)
                print '                  Volumen de datos encontrados: {} de {}'.format(len(almacen.elementosEncontradosReales), len(almacen.elementosRequeridosReales))
        '''
        #os.system("pause")

    def _info_datos_usuarios(self):
        print "---->CRONOGRAMA-TRANSMITIDO<----"
        for user in self.users:
            print '-->User: {}'.format(user)
            #print 'Posicion: {},{}'.format(user.point.pointX, user.point.pointY)
            for q in user.consultasDeRangoRecibidas:
                print 'Consulta: {}'.format(q)
                for item in q.foundItems:
                    print 'Item: {} - Time: {}'.format(item[0], item[1])

        #for step in self.users[0].randomWalk.rastro:
            #print "Position: {},{} Time: {}".format(step[0], step[1], step[2])
        #os.system("pause")


    '''
    ESTA ES LA FORMA DE CREAR
    EL GETTER Y SETTER DE LA 
    FORMA PYTHONISTA.
    ENLACE:https://www.python-course.eu/python3_properties.php
    YA QUE AL MODIFICAR
    EL CODIGO NO CAMBIA LA
    INTERFACE.
    '''
    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, grid):
        self.__grid = grid

    @grid.deleter
    def grid(self):
        del self.__grid

    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, schedule):
        self.__schedule = schedule

    @property
    def percentage(self):
        return self.__percentage

    @percentage.setter
    def percentage(self, percentage):
        if percentage == '10%':
            self.__percentage = 0.1
        if percentage == '20%':
            self.__percentage = 0.2
        if percentage == '30%':
            self.__percentage = 0.3
        if percentage == '40%':
            self.__percentage = 0.4
        if percentage == '50%':
            self.__percentage = 0.5
        if percentage == '60%':
            self.__percentage = 0.6
        if percentage == '70%':
            self.__percentage = 0.7
        if percentage == '80%':
            self.__percentage = 0.8
        if percentage == '90%':
            self.__percentage = 0.9
        if percentage == '100%':
            self.__percentage = 1
