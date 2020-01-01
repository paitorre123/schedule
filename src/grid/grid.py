from src.grid.gridCell import Cell
from src.grid.regionDelPlano import CellRegion
from src.grid.point import Point


class Grilla(object):
    def __init__(self):
        self.width = None
        self.height = None
        self.cells = []
        self.users = []
        self.zones = []


    def addCell(self,  point1, point2, point3, point4, side, rectangle):
        c = Cell(id=len(self.cells))
        c.pointA = point1
        c.pointB = point2
        c.pointC = point3
        c.pointD = point4
        c.side = side
        c.rectangle = rectangle
        self.cells.append(c)

    def removeCell(self, cell):
        self.cells.remove(cell)

    def cellOfUser(self, x, y):
        for cell in self.cells:
            # print 'number cells: {}'.format(i)
            if cell.contain(x, y):
                return cell
        assert 'El usuaruario no esta en ninguna celda'

    def collision(self, x, y):
        '''#i=1
        for cell in self.cells:
            #print 'number cells: {}'.format(i)
            if cell.contain(x, y):
                return True
            #i+=1'''
        if self.zones[0].contain(x, y):
            return True
        if self.zones[1].contain(x, y):
            return True
        if self.zones[2].contain(x, y):
            return True
        if self.zones[3].contain(x, y):
            return True
        if self.zones[4].contain(x, y):
            return True
        if self.zones[5].contain(x, y):
            return True
        if self.zones[6].contain(x, y):
            return True
        if self.zones[7].contain(x, y):
            return True
        if self.zones[8].contain(x, y):
            return True
        if self.zones[9].contain(x,y):
            return True
        if self.zones[10].contain(x,y):
            return True
        if self.zones[11].contain(x,y):
            return True
        if self.zones[12].contain(x,y):
            return True
        if self.zones[13].contain(x,y):
            return True
        return False

    def collision_northWest(self, x, y):
        #i=1
        #print '{}'.format(self.zones[0])
        if self.zones[0].contain(x, y):
            return True
            #i+=1
        return False

    def collision_north(self, x, y):

        if self.zones[1].contain(x, y):
            return True
            #i+=1
        return False

    def collision_northEast(self, x, y):

        if self.zones[2].contain(x, y):
            return True
            #i+=1
        return False

    def collision_west(self, x, y):
        if self.zones[3].contain(x, y):
                return True

        return False

    def collision_center(self, x, y):
        if self.zones[4].contain(x, y):
            return True

        return False

    def collision_east(self, x, y):

        if self.zones[5].contain(x, y):
            return True

        return False

    def collision_southWest(self, x, y):

        if self.zones[6].contain(x, y):
            return True

        return False

    def collision_south(self, x, y):

        if self.zones[7].contain(x, y):
            return True

        return False

    def collision_southEast(self, x, y):

        if self.zones[8].contain(x, y):
            return True
            #i+=1
        return False

    def collision_one_split_five(self, x, y):

        if self.zones[9].contain(x, y):
            return True
            #i+=1
        return False

    def collision_two_split_five(self, x, y):

        if self.zones[10].contain(x, y):
            return True
            #i+=1
        return False

    def collision_three_split_five(self, x, y):

        if self.zones[11].contain(x, y):
            return True
            #i+=1
        return False

    def collision_four_split_five(self, x, y):

        if self.zones[12].contain(x, y):
            return True
            #i+=1
        return False

    def collision_five_split_five(self, x, y):

        if self.zones[13].contain(x, y):
            return True
            #i+=1
        return False


    def create_zones(self):
        #print 'Celda 1'
        region = CellRegion(0)
        point = Point()
        point.pointX = 0
        point.pointY = 0
        region.pointA = point

        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * (self.height/3)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width/3)
        point.pointY = 0
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height/3)
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 2'
        region = CellRegion(1)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = 0
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = 0
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 3'
        region = CellRegion(2)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = 0
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = 0
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 4'
        region = CellRegion(3)
        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointA = point

        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 5'
        region = CellRegion(4)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 6'
        region = CellRegion(5)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = self.cells[0].side * (self.height / 3)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 7'
        region = CellRegion(6)
        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointA = point

        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * self.height
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side *  self.height
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 8'
        region = CellRegion(7)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * self.height
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * self.height
        region.pointD = point

        self.zones.append(region)

        #print 'Celda 9'
        region = CellRegion(8)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 3) + self.cells[0].side * (self.width / 3)
        point.pointY = self.cells[0].side * self.height
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = self.cells[0].side * (self.height / 3) + self.cells[0].side * (self.height / 3)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = self.cells[0].side * self.height
        region.pointD = point

        self.zones.append(region)

        '''
        nuevas regiones de desplazamiento
        '''

        #print 'Celda 10'
        region = CellRegion(9)
        point = Point()
        point.pointX = 0
        point.pointY = 0
        region.pointA = point

        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * (self.height / 2)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 2)
        point.pointY = 0
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 2)
        point.pointY = self.cells[0].side * (self.height / 2)
        region.pointD = point

        self.zones.append(region)

        # print 'Celda 11'
        region = CellRegion(10)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 2)
        point.pointY = 0
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 2)
        point.pointY = self.cells[0].side * (self.height / 2)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = 0
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side  * self.width
        point.pointY = self.cells[0].side * (self.height / 2)
        region.pointD = point

        self.zones.append(region)

        # print 'Celda 12'
        region = CellRegion(11)
        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * (self.height / 2)
        region.pointA = point

        point = Point()
        point.pointX = 0
        point.pointY = self.cells[0].side * self.height
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side *  self.width
        point.pointY = 0
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * self.width
        point.pointY = self.cells[0].side * self.height
        region.pointD = point

        self.zones.append(region)

        # print 'Celda 13'
        region = CellRegion(12)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 2)
        point.pointY = self.cells[0].side * (self.height / 2)
        region.pointA = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 2)
        point.pointY = self.cells[0].side * self.height
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side  * self.width
        point.pointY = self.cells[0].side * (self.height / 2)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side  * self.width
        point.pointY = self.cells[0].side * self.height
        region.pointD = point

        self.zones.append(region)



        # print 'Celda 14'
        region = CellRegion(13)
        point = Point()
        point.pointX = self.cells[0].side * (self.width / 4)
        point.pointY = self.cells[0].side * (self.height / 4)
        region.pointA = point

        point = Point()
        point.pointX =  self.cells[0].side * (self.width / 4)
        point.pointY = self.cells[0].side * (self.height / 4) + self.cells[0].side * (self.height / 4) + self.cells[0].side * (self.height / 4)
        region.pointB = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 4) + self.cells[0].side * (self.width / 4) + self.cells[0].side * (self.width / 4)
        point.pointY = self.cells[0].side * (self.height / 4)
        region.pointC = point

        point = Point()
        point.pointX = self.cells[0].side * (self.width / 4) + self.cells[0].side * (self.width / 4) + self.cells[0].side * (self.width / 4)
        point.pointY = self.cells[0].side * (self.height / 4) + self.cells[0].side * (self.height / 4) + self.cells[0].side * (self.height / 4)
        region.pointD = point

        self.zones.append(region)

        #os.system("pause")

    def addUser(self, user):
        self.users.append(user)

    def addPoi(self, poi):
        cell = self.cellOfUser(poi.point.pointX, poi.point.pointY)
        cell.addPointsInterest(poi)

    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        self.__cells = cells

    @property
    def users(self):
        return self.__users

    @users.setter
    def users(self, users):
        self.__users = users
