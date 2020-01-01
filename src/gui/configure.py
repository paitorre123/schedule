from Pmw import ComboBox
from Tkinter import *
import tkFileDialog
from Pmw.Pmw_1_3_3.lib.PmwNoteBook import NoteBook
from src.gui.windowGrid import GridWindow
from Pmw.Pmw_1_3_3.lib.PmwBase import alignlabels
from src.distribution.probabilityUsers import ProbabilityUsers
from src.distribution.probabilityPointsInterest import ProbabilityPointsInterest
from src.master.simulator import Simulator
from src.timer.timer import Timer
from src.pruebas.manejoExcel import ManejoExcel
import os
from src.client.cliente import Usuario
from src.caminanteAleatorio.localizacion import Localizacion
from src.grid.point import Point
from src.puntoDeInteres.puntosDeInteres import PuntosDeInteres
from src.manejoDeDatos.ManejoDeDatos import ManejoDeDatos
from src.client.anonimizador import Anonimizador

class ConfigureWindow(object):
    def __init__(self):
        self.root = Tk()
        self.time = Timer()
        self.root.wm_title('Configuracion de la pantalla pincipal')
        self.height = 300
        self.width = 800
        self.root.geometry('{}x{}'.format(self.width, self.height))
        self.percentage = '100%'
        self.selectSizeSchedule = 100
        self.algoritmoDePlanificacionSeleccionado = 'Algoritmo de Envergadura probabilista'
        self.ajusteTemporalSeleccionado = False
        self.criterioDeSeleccionSeleccionado = 'Carga de trabajo'
        self.urlFile = None
        self.selectAnonymity = 4

        '''
        EN PYTHON EL DICCIONARIO
        REEMPLAZA EL SWITH.
        A CONTINUACION UN EJEMPLO: 
        https://nideaderedes.urlansoft.com/2013/03/04/no-hay-switch-en-python/
        '''
        self.swithSizeCell = {'720x480': self.selectResolution, '1024x768': self.selectResolution, '1080x720': self.selectResolution, '1920x1080': self.selectResolution}
        self.noteBook = NoteBook(self.root)
        self.panelConfigurateFrame = self.noteBook.add('Configuracion  de Ventana')
        self.panelConfigureUser = self.noteBook.add('Configurar Usuarios en las Celdas')
        self.panelConfigurePointsInterest = self.noteBook.add('Configurar puntos de interes')
        self.panelConfigureSimulator = self.noteBook.add('Configurar Simulacion')
        self.noteBook.pack(padx=4, pady=4, fill=BOTH, expand=1)
        #metodos de la clase
        self._frameConfigure()
        self._clientConfigure()
        self._pointOfInterestConfigure()
        self._simulatorConfigure()
        self.root.mainloop()

    def _frameConfigure(self):
        self.resolution = ComboBox(self.panelConfigurateFrame, labelpos=W, label_text='Resolucion: ', selectioncommand=self.selectedResolution)

        for pixel in ('720x480', '1024x768', '1080x720', '1920x1080', 'Free'):
            self.resolution.insert(0, pixel)

        self.sizeCell = ComboBox(self.panelConfigurateFrame, labelpos=W, label_text='Talla Celda: ', selectioncommand=self.selectedSizeCell)
        self.numberCellInColumn = ComboBox(self.panelConfigurateFrame, labelpos=W, label_text='Celdas Por Columna: ', selectioncommand=self.selectedNumberCellInColumn)
        self.numberCellInRow = ComboBox(self.panelConfigurateFrame, labelpos=W, label_text='Celdas Por Fila: ', selectioncommand=self.selectedNumberCellInRow)
        self.build = Button(self.panelConfigurateFrame, text='BUILD WINDOW', command=self.createWindow, bg='grey', fg='black')

        '''ALINEACION DE LAS BARRAS DESPLEGABLES'''
        entries = (self.resolution, self.sizeCell, self.numberCellInColumn, self.numberCellInRow)

        for entry in entries:
            entry.pack(fill='x', expand=1, padx=10, pady=5)

        alignlabels(entries)
        self.build.pack(fill=X, expand=1)

    def _clientConfigure(self):

        self.userNumber = ComboBox(self.panelConfigureUser, labelpos=W, label_text='Numero usuarios: ', selectioncommand=self.selectedUserNumber)
        maxUsers=10000
        for user in range(1, maxUsers+1):
            self.userNumber.insert(0, user)

        self.typeDistributionCells = ComboBox(self.panelConfigureUser, labelpos=W, label_text='Distribucion Celdas: ',selectioncommand=self.selectedTypeDistributionCells)
        for distribution in ('Uniforme', 'Cuadratica', 'Zipf, S=2', 'Zipf, S=3', 'Zipf, S=4', 'Gamma Beta=2 y Alfa=2.0=K', 'Gamma  Beta=9 y Alfa=2.0=K','Gamma  Beta=7 y Alfa=3.0=K', 'Exponencial, Lambda=0.5', 'Exponencial, Lambda=1.0', 'Exponencial, Lambda=1.5'):
            self.typeDistributionCells.insert(0, distribution)

        self.cardinalPointsProbability = ComboBox(self.panelConfigureUser, labelpos=W, label_text='Probabilidad en puntos cardinales: ', selectioncommand=self.selectedCardinalPointsProbability)
        for move in ['Random', 'Uniforme', 'Direccion Predefinida', 'Uniforme Direccion Norte', 'Uniforme Direccion Noroeste', 'Uniforme Direccion Noreste',
                     'Uniforme Direccion oeste', 'Uniforme Direccion centro', 'Uniforme Direccion este', 'Uniforme Direccion suroeste',
                     'Uniforme Direccion sur', 'Uniforme Direccion sureste', 'Uniforme Direccion 5split noroeste', 'Uniforme Direccion 5split noreste',
                     'Uniforme Direccion 5split suroeste', 'Uniforme Direccion 5split sureste','Uniforme Direccion 5split centro']:
            self.cardinalPointsProbability.insert(0, move)

        self.createUser =  Button(self.panelConfigureUser, text='INSERT USERS', command=self.insertUsers, bg='grey', fg='black')
        self.createUserAndMovement = Button(self.panelConfigureUser, text='INSERT USERS AND MOVEMENT', command=self._chooseFile_user_position, bg='grey', fg='black')
        '''ALINEACION DE LAS BARRAS DESPLEGABLES'''
        entries = (self.userNumber, self.typeDistributionCells, self.cardinalPointsProbability)

        for entry in entries:
            entry.pack(fill='x', expand=1, padx=10, pady=5)

        alignlabels(entries)
        self.createUser.pack(fill=X, expand=1)
        self.createUserAndMovement.pack(fill=X, expand=1)

    def _chooseFile_user_position(self):
        self.urlFile = tkFileDialog.askopenfilename(parent=self.root, initialdir="/",title='Seleccionar Archivo')
        print self.urlFile
        #1. abrir archivo
        #2. leer y almacenar posiciones
        #3. entregar posiciones

        #self.gridWindow.paintUsers()
        ManejoExcel.urlRead = self.urlFile
        archivoLectura = ManejoExcel.abrir_archivo_excel()
        rastroUsuarios = ManejoExcel.leer_datos_usuarios(archivoLectura,'Pocision usuarios')
        numberUser = 0
        for r in rastroUsuarios:
            u = Usuario()
            u.name = numberUser
            u.time = self.time

            p = Point()
            p.pointX = r[0][0]
            p.pointY = r[0][1]
            u.point = p
            u.movement_probability(self.selectCardinalPointsProbability)
            self.gridWindow.grid.addUser(u)
            r.remove(r[0])
            timeUser = 1
            for ps in r:
                u.randomWalk.rastro.append([ps[0],ps[1],timeUser])
                timeUser += 1
            numberUser +=1
        self.selectUserNumber = numberUser
        self.gridWindow.paintUsers()




    def _pointOfInterestConfigure(self):
        self.pointsInterestNumber = ComboBox(self.panelConfigurePointsInterest, labelpos=W, label_text='Numero puntos de interes: ', selectioncommand=self.selectedPointsInterestNumber)
        maxUsers=10000
        for user in range(1, maxUsers+1):
            self.pointsInterestNumber.insert(0, user)

        self.typeDistributionPointsInterest = ComboBox(self.panelConfigurePointsInterest, labelpos=W, label_text='Distribucion Celdas: ',selectioncommand=self.selectedTypeDistributionPointsInterest)
        self.typeDistributionPointsInterest.insert(0, 'Uniforme')

        self.createPointsInterest =  Button(self.panelConfigurePointsInterest, text='INSERT POINTS OF INTEREST', command=self.insertPointsInterest, bg='grey', fg='black')

        self.readPointsInterest = Button(self.panelConfigurePointsInterest, text='READ POINTS OF INTEREST', command=self.readPointsInterest, bg='grey', fg='black')

        '''ALINEACION DE LAS BARRAS DESPLEGABLES'''
        entries = (self.pointsInterestNumber, self.typeDistributionPointsInterest)

        for entry in entries:
            entry.pack(fill='x', expand=1, padx=10, pady=5)

        alignlabels(entries)
        self.createPointsInterest.pack(fill=X, expand=1)
        self.readPointsInterest.pack(fill=X, expand=1)

    def _simulatorConfigure(self):
        self.algoritmoPlanificacion = ComboBox(self.panelConfigureSimulator, labelpos=W,
                                               label_text='Algoritmo de planificacion: ',
                                               selectioncommand=self.selectedAlgoritmoPlanificacion)
        for a in ['Algoritmo de Envergadura determinista', 'Algoritmo de Envergadura probabilista',
                  'Algoritmo de Envergadura probabilista con tiempo-1 de espera',
                  'Algoritmo de popularidad determinista', 'Algoritmo de popularidad probabilista',
                  'Algoritmo de popularidad probabilista con tiempo-1 de espera',
                  'Algoritmo relevancia determinista', 'Algoritmo relevancia probabilista',
                  'Algoritmo relevancia probabilista con tiempo-1 de espera']:
            self.algoritmoPlanificacion.insert(0, a)

        self.ajusteTemporal = ComboBox(self.panelConfigureSimulator, labelpos=W, label_text='Ajuste temporal: ',
                                       selectioncommand=self.selectedAjusteTemporal)
        for b in ['True', 'False']:
            self.ajusteTemporal.insert(0, b)

        self.criterioSeleccion = ComboBox(self.panelConfigureSimulator, labelpos=W,
                                          label_text='Criterio Seleccion: ',
                                          selectioncommand=self.selectedCriterio)
        for c in ['Carga de trabajo', 'Stretch', 'Jitter']:
            self.criterioSeleccion.insert(0, c)

        self.percentageC = ComboBox(self.panelConfigureSimulator , labelpos=W, label_text='Porcentaje de usaurios que consultan: ', selectioncommand=self.selectedPercentage)
        for percentage in ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%']:
            self.percentageC.insert(0, percentage)

        self.sizeSchedule = ComboBox(self.panelConfigureSimulator, labelpos=W, label_text='Talla del cronograma: ', selectioncommand=self.selectedSizeSchedule)
        for size in range(100, 10001):
            self.sizeSchedule.insert(0, size)

        self.anonymity = ComboBox(self.panelConfigureSimulator, labelpos=W, label_text='K de anonimato: ', selectioncommand=self.selectedAnonymity)
        for anonymity in range(2, 11):
            self.anonymity.insert(0, anonymity)

        self.startSimulation = Button(self.panelConfigureSimulator, text='START SIMULATION', command=self.simulate, bg='grey',   fg='black')

        entries = (self.algoritmoPlanificacion, self.ajusteTemporal,self.criterioSeleccion, self.percentageC, self.sizeSchedule, self.anonymity)

        for entry in entries:
            entry.pack(fill='x', expand=1, padx=10, pady=5)

        alignlabels(entries)

        self.startSimulation.pack(fill=X, expand=1)


    def selectedAlgoritmoPlanificacion(self, entry):
        self.algoritmoDePlanificacionSeleccionado = entry
        if entry != 'Algoritmo de Envergadura determinista' and entry !='Algoritmo de popularidad determinista' and entry != 'Algoritmo relevancia determinista':
            self.criterioSeleccion.clear()
            for c in ['Carga de trabajo', 'Stretch', 'Jitter']:
                self.criterioSeleccion.insert(0, c)
        else:
            self.criterioSeleccion.clear()
            self.criterioSeleccion.insert(0, 'None')

    def selectedAjusteTemporal(self, entry):
        if entry == 'True':
            self.ajusteTemporalSeleccionado = True
        else:
            self.ajusteTemporalSeleccionado = False

    def selectedCriterio(self,entry):
        self.criterioDeSeleccionSeleccionado = entry


    def selectedResolution(self, entry):
        if entry == 'Free':
            self.sizeCell.clear()
            self.numberCellInColumn.clear()
            self.numberCellInRow.clear()
            self.resolutionFree = True

            for cell in range(10, 41):
                self.sizeCell.insert(0, cell)
        else:
            try:
                self.resolutionWidth = entry.split('x', 1)[0]
                self.resolutionHeight = entry.split('x', 1)[1]
                #print 'Size select: {}x{}'.format(self.__resolutionWidth, self.__resolutionHeight)
                self.swithSizeCell[entry]()
            except KeyError:
                print 'KeyError: There is no such resolution'

    def selectedSizeCell(self, entry):
        if self.resolutionFree:
            for x in range(9, 22):
                self.numberCellInColumn.insert(END, x)
            for x in range(9, 22):
                self.numberCellInRow.insert(END, x)
            self.selectSizeCell = entry
        else:
            column = int(self.resolutionWidth)/entry
            row = int(self.resolutionHeight)/entry
            self.numberCellInColumn.clear()
            self.numberCellInRow.clear()
            for x in range(column/2, column+1):
                self.numberCellInColumn.insert(END, x)
            for x in range(row/2, row+1):
                self.numberCellInRow.insert(END, x)
            self.selectSizeCell = entry
            # print 'Selecion talla: {}'.format(entry)
            # print 'Maximas columnas: {}'.format(column)
            # print 'Maximas filas: {}'.format(row)

    def selectedNumberCellInColumn(self, entry):
        self.selectNumberCellInColumn = entry

    def selectedNumberCellInRow(self, entry):
        self.selectNumberCellInRow = entry

    def selectResolution(self):
        for cell in range(10, 41):
            self.sizeCell.insert(0, cell)

    def selectedUserNumber(self, entry):
        self.selectUserNumber = entry

    def selectedTypeDistributionCells(self, entry):
        self.selectTypeDistributionCells = entry

    def selectedAnonymity(self, entry):
        self.selectAnonymity = entry

    def selectedPercentage(self, entry):
        self.percentage = entry

    def selectedSizeSchedule(self, entry):
        self.selectSizeSchedule = entry

    def selectedCardinalPointsProbability(self, entry):
        self.selectCardinalPointsProbability = entry

    def selectedPointsInterestNumber(self, entry):
        self.selectPointsInterestNumber= entry

    def selectedTypeDistributionPointsInterest(self, entry):
        self.selectTypeDistributionPointsInterest = entry


    def createWindow(self):
        #print 'Talla de la Celda:{}'.format(self.__selectSizeCell)
        #print 'Numero de celdas en las columnas: {}'.format(self.__selectNumberCellInColumn)
        #print 'Numero de celdas en las filas: {}'.format(self.__selectNumberCellInRow)
        self.gridWindow = GridWindow( self.selectSizeCell, self.selectNumberCellInColumn, self.selectNumberCellInRow)
        #self.__gridWindow.getRoot().mainloop()
        #self.__operator = self.__gridWindow.getOperator()



    def insertUsers(self):
        #print 'Numero Usuarios: {}'.format(self.__selectUserNumber)
        #print  'Distribucion de Celdas: {}'.format(self.__selectTypeDistributionCells)
        #print "Celdas: {}".format(self.__gridWindow.getCells())
        probability = ProbabilityUsers(self.selectUserNumber, self.gridWindow.grid, self.time)
        probability.generateDistributionCells(self.selectTypeDistributionCells)
        probability.generateDistributionUser(self.selectCardinalPointsProbability)
        self.gridWindow.paintUsers()


    def insertPointsInterest(self):
        '''CREACION DE LOS PUNTOS DE INTERES EN LAS
        CELDAS CREADAS.'''
        #print '{}'.format(self.selectPointsInterestNumber)
        #print '{}'.format(self.selectTypeDistributionPointsInterest)
        probability = ProbabilityPointsInterest(self.selectPointsInterestNumber, self.gridWindow.grid)
        probability.generateDistributionPointsInterest(self.selectTypeDistributionPointsInterest)
        probability.distribute_points_interest()
        self.gridWindow.paintPointsInterest()

    def readPointsInterest(self):
        self.urlFile = tkFileDialog.askopenfilename(parent=self.root, initialdir="/", title='Seleccionar Archivo')
        print self.urlFile
        # 1. abrir archivo
        # 2. leer y almacenar posiciones
        # 3. entregar posiciones
        ManejoExcel.urlRead = self.urlFile
        archivoLectura = ManejoExcel.abrir_archivo_excel()
        rastroPois = ManejoExcel.leer_datos_usuarios(archivoLectura, 'posicion poi')
        self.selectPointsInterestNumber = 0
        for r in rastroPois:
            for s in r:
                #print '{}'.format(s)
                poi = PuntosDeInteres()
                poi.name = str(s[2])
                p = Point()
                p.pointX = s[0]
                p.pointY = s[1]
                poi.point = p
                self.gridWindow.grid.addPoi(poi)
                self.selectPointsInterestNumber += 1
        self.gridWindow.paintPointsInterest()


    def simulate(self):
        ManejoDeDatos.NOMBRE_ARCHIVO = '['+''.join(x for x in self.algoritmoDePlanificacionSeleccionado.title() if not x.isspace()) +']['+ ''.join(x for x in self.criterioDeSeleccionSeleccionado .title() if not x.isspace())+'][USER='+ str(self.selectUserNumber) +'][POI='+ str(self.selectPointsInterestNumber) +'][k='+ str(self.selectAnonymity) +']'
        Anonimizador.ANONIMATO = self.selectAnonymity
        self.simulator = Simulator(self.gridWindow.grid, self.time, self.selectSizeSchedule, self.algoritmoDePlanificacionSeleccionado,self.ajusteTemporalSeleccionado, self.criterioDeSeleccionSeleccionado )
        self.simulator.painter = self.gridWindow.operator
        for user in self.gridWindow.grid.users:
            user.painter = self.gridWindow.operator
            self.simulator.users.append(user)
        #print 'Percentage: {}'.format(self.percentage)
        #print 'Size schedule: {}'.format(self.selectSizeSchedule)
        self.simulator.percentage = self.percentage
        self.simulator.start()
        '''try:
            if self.selectTypeMovement == 'Caminanate Aleatorio Hacia Hotspot':
                ZonasPopulares(self.gridWindow.grid, self.gridWindow.canvas)
        except AttributeError:
            pass
        '''
