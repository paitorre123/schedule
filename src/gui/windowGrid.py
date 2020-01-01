from Tkinter import *
from src.grid.painter import Painter
from src.grid.point import Point
from src.grid.grid import Grilla


class GridWindow(object):
    def __init__(self, lado, cellColumn, cellRow):
        self.root = None #Tk()
        #self.root.title("Grilla")
        self.width = None
        self.height = None
        self.lado = lado
        self.cellColumn = cellColumn
        self.cellRow = cellRow
        self.margen = 0
        self.row = 0
        self.column = 0
        self.grid = Grilla()
        self._frameDrawable()
        '''
        CREACION DE OPERACIONES
        '''
        self.operator = Painter(frame=self)
        #self._centeredWindow()
        #self.root.resizable(False, False)


    def _frameDrawable(self):
        self.cells = []

        self.grid.width = self.cellColumn
        self.grid.height = self.cellRow

        #self.frame = Frame(self.__root)
        #self.frame.pack(expand=YES, fill=BOTH)
        #self.canvas = Canvas(self.frame, bg='grey')
        #self.canvas.pack(expand=YES, fill=BOTH)

        #self.myCanvas.bind("", self.__move)

        for j in range(0, self.cellRow):
            for i in range(0, self.cellColumn):
                '''
                EL ORDEN DE LOS PUNTOS EN LA RECTANGULO DEL CANVAS
                ES EL SIGUIENTE:
                (X1,Y1)-(X2,Y2)
                EN EL METODO : create_rectangle 
                LA FORMA DEL RECTANGULO FORMADO POR LOS PUNTOS ES LA 
                SIGUIENTE:
                
                A              C
                o--------------o
                |              |
                |              |
                |              |
                o--------------o
                B              D '''
                rectangle = None #self.canvas.create_rectangle(self.column, self.row, self.column+self.lado, self.row+self.lado, width=0.5, outline='black')

                #Point x1,y1
                point1 = Point()
                point1.pointX = self.column
                point1.pointY = self.row
                # Point x1,y2
                point2 = Point()
                point2.pointX = self.column
                point2.pointY = self.row+self.lado
                # Point x2,y1
                point3 = Point()
                point3.pointX = self.column+self.lado
                point3.pointY = self.row
                # Point x2,y2
                point4 = Point()
                point4.pointX = self.column+self.lado
                point4.pointY = self.row+self.lado
                #agregar celda a la grilla
                self.grid.addCell(point1, point2, point3, point4, self.lado, rectangle)
                self.column = self.column + self.lado
            self.column = 0
            self.row = self.row + self.lado

        self.width = (self.cellColumn*self.lado) + self.margen
        self.height = (self.cellRow*self.lado) + self.margen

        self.grid.create_zones()

    def _centeredWindow(self):
        # type: () -> GridWindow
        x = self.root.winfo_screenwidth() // 2 - self.width // 2
        y = self.root.winfo_screenheight() // 2 - self.height // 2
        self.root.geometry('{}x{}+{}+{}'.format(self.width, self.height, x, y))
        self.root.deiconify()

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, root):
        self.__root = root

    @property
    def canvas(self):
        return self.__canvas

    @canvas.setter
    def canvas(self, canvas):
        self.__canvas = canvas

    @property
    def grid(self):
        return self.__grid

    @grid.setter
    def grid(self, grid):
        self.__grid = grid

    def paintUsers(self):
        self.operator.paintUsers(self.grid)

    def paintPointsInterest(self):
        for cell in self.grid.cells:
            for poi in cell.pointsInterest:
                poi.paintPointsOfInterest(self.canvas)