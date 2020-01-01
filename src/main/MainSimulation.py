from src.gui.windowGrid import GridWindow
from src.master.simulator import Simulator
from src.pruebas.manejoExcel import ManejoExcel
from src.grid.point import Point
from src.puntoDeInteres.puntosDeInteres import PuntosDeInteres
from src.manejoDeDatos.ManejoDeDatos import ManejoDeDatos
from src.client.anonimizador import Anonimizador
from src.client.cliente import Usuario
from src.timer.timer import Timer
import os.path
from pathlib import Path


class MainSimulation():


    def __init__(self):
        self.time = Timer()
        self.percentage = '100%'
        self.selectSizeSchedule = 50
        self.algoritmoDePlanificacionSeleccionado = ''
        self.ajusteTemporalSeleccionado = True
        self.criterioDeSeleccionSeleccionado = ''
        self.urlFile = None
        self.selectAnonymity = 4
        self.selectSizeCell = 40
        self.selectNumberCellInColumn = 20
        self.selectNumberCellInRow = 20
        self.selectCardinalPointsProbability = 'Direccion Predefinida'

    def createWindow(self):
        print 'creando ventana'
        # print 'Talla de la Celda:{}'.format(self.__selectSizeCell)
        # print 'Numero de celdas en las columnas: {}'.format(self.__selectNumberCellInColumn)
        # print 'Numero de celdas en las filas: {}'.format(self.__selectNumberCellInRow)
        self.gridWindow = GridWindow(self.selectSizeCell, self.selectNumberCellInColumn, self.selectNumberCellInRow)
        # self.__gridWindow.getRoot().mainloop()
        # self.__operator = self.__gridWindow.getOperator()

    def chooseFile_user_position(self, url):
        print 'seleccionando usuarios'
        self.urlFile = url
        # 1. abrir archivo
        # 2. leer y almacenar posiciones
        # 3. entregar posiciones

        # self.gridWindow.paintUsers()
        ManejoExcel.urlRead = self.urlFile
        archivoLectura = ManejoExcel.abrir_archivo_excel()
        rastroUsuarios = ManejoExcel.leer_datos_usuarios(archivoLectura, 'Pocision usuarios')
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
                u.randomWalk.rastro.append([ps[0], ps[1], timeUser])
                timeUser += 1
            numberUser += 1
        self.selectUserNumber = numberUser
        #self.gridWindow.paintUsers()


    def readPointsInterest(self, url):
        print 'seleccionando puntos'
        self.urlFile = url
        #print self.urlFile
        # 1. abrir archivo
        # 2. leer y almacenar posiciones
        # 3. entregar posiciones
        ManejoExcel.urlRead = self.urlFile
        archivoLectura = ManejoExcel.abrir_archivo_excel()
        rastroPois = ManejoExcel.leer_datos_usuarios(archivoLectura, 'posicion poi')
        self.selectPointsInterestNumber = 0
        for r in rastroPois:
            for s in r:
                # print '{}'.format(s)
                poi = PuntosDeInteres()
                poi.name = str(s[2])
                p = Point()
                p.pointX = s[0]
                p.pointY = s[1]
                poi.point = p
                self.gridWindow.grid.addPoi(poi)
                self.selectPointsInterestNumber += 1
        #self.gridWindow.paintPointsInterest()

    def simulate(self):
        print 'simulando'
        ManejoDeDatos.NOMBRE_ARCHIVO = '[' + ''.join(
            x for x in self.algoritmoDePlanificacionSeleccionado.title() if not x.isspace()) + '][' + ''.join(
            x for x in self.criterioDeSeleccionSeleccionado.title() if not x.isspace()) + '][USER=' + str(
            self.selectUserNumber) + '][POI=' + str(self.selectPointsInterestNumber) + '][k=' + str(
            self.selectAnonymity) + ']'
        Anonimizador.ANONIMATO = self.selectAnonymity
        self.simulator = Simulator(self.gridWindow.grid, self.time, self.selectSizeSchedule,
                                   self.algoritmoDePlanificacionSeleccionado, self.ajusteTemporalSeleccionado,
                                   self.criterioDeSeleccionSeleccionado)
        self.simulator.painter = self.gridWindow.operator
        for user in self.gridWindow.grid.users:
            user.painter = self.gridWindow.operator
            self.simulator.users.append(user)
        # print 'Percentage: {}'.format(self.percentage)
        # print 'Size schedule: {}'.format(self.selectSizeSchedule)
        self.simulator.percentage = self.percentage
        self.simulator.start()
        '''try:
            if self.selectTypeMovement == 'Caminanate Aleatorio Hacia Hotspot':
                ZonasPopulares(self.gridWindow.grid, self.gridWindow.canvas)
        except AttributeError:
            pass
        '''

if __name__ == '__main__':
    os.chdir('..')
    os.chdir('manejoDeDatos')
    os.chdir('datosExcel')
    d = os.getcwd()
    os.chdir('..')
    ManejoDeDatos.PATH_ARCHIVO = os.getcwd()+ '/'

    algoritmoSeleccionDeterminista = ['Algoritmo de Envergadura determinista'#,
                                        #'Algoritmo de popularidad determinista',
                                      #'Algoritmo relevancia determinista'
                    ]
    algoritmoSeleccionProbabilista = ['Algoritmo de Envergadura probabilista'
                  #'Algoritmo de Envergadura probabilista con tiempo de espera',
                   #'Algoritmo de popularidad probabilista',
                  #Algoritmo de popularidad probabilista con tiempo de espera',
                   #'Algoritmo relevancia probabilista',
                  #'Algoritmo relevancia probabilista con tiempo de espera'
                  ]
    criterioSeleccio = [
                        'Carga de trabajo'
                        #'Stretch',
                        #'Jitter'
                       ]
    urlMovement = [
                    #d + '/Simulacion[500][20x20]FINAL.xlsx'
                   #d + '/Simulacion[400][20x20]FINAL.xlsx'
                  #d + '/Simulacion[300][20x20]FINAL.xlsx',
                   d + '/Simulacion[200][20x20]FINAL.xlsx'
                    ]
    urlPoi = [
              #d + '/PosicionPuntosDeInteres[4000].xlsx',
              #d + '/PosicionPuntosDeInteres[3200].xlsx',
              #d + '/PosicionPuntosDeInteres[2400].xlsx',
              d + '/PosicionPuntosDeInteres[1600].xlsx'
              ]

    for urlm in urlMovement:
        for urlp in urlPoi:
            '''for als in algoritmoSeleccionDeterminista:
                ms = MainSimulation()
                ms.createWindow()
                ms.chooseFile_user_position(urlm)
                ms.readPointsInterest(urlp)
                ms.algoritmoDePlanificacionSeleccionado = als
                ms.criterioDeSeleccionSeleccionado = 'None'
                ms.simulate()
                del ms'''
            for als in algoritmoSeleccionProbabilista:
                for cs in criterioSeleccio:
                    ms = MainSimulation()
                    ms.createWindow()
                    ms.chooseFile_user_position(urlm)
                    ms.readPointsInterest(urlp)
                    ms.algoritmoDePlanificacionSeleccionado = als
                    ms.criterioDeSeleccionSeleccionado = cs
                    ms.simulate()
                    del ms
    print 'Termino la cosa'