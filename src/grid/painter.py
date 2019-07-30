

class Painter(object):
    def __init__(self, frame):
        self.points = []
        self.canvas = frame.canvas

    def __paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        # print "Position: {},{}".format(event.x, event.y)
        colorval = "#%02x%02x%02x" % (255, 165, 51)
        oval_id = self.__canvas.create_oval(x1, y1, x2, y2, fill=colorval)
        #self.__points[self.__points.__len__()] = Point(oval_id)
        # self.myCanvas.tag_bind('id', '<B3-Motion>', self.__move)
        self.__canvas.bind('<Button-3>', self.__move)

    def paintUsers(self, grid):

        for user in grid.users:
            x1, y1 = (int(user.point.pointX) - 2), (int(user.point.pointY) - 2)
            x2, y2 = (int(user.point.pointX)  + 2), (int(user.point.pointY) + 2)
            # print "Position: {},{}".format(event.x, event.y)
            colorval = "#%02x%02x%02x" % (186, 245, 0)
            user.oval = self.canvas.create_oval(x1, y1, x2, y2, fill=colorval, tags='user')



    def move(self, oval):
        print self.canvas.coords(oval)
        # move selected item
        #self.canvas.coords(oval, event.x - 2, event.y - 2, event.x + 2, event.y + 2)
        print 'move'
        self.canvas.move(oval, 1, 1)

    @property
    def canvas(self):
        return self.__canvas

    @canvas.setter
    def canvas(self, canvas):
        self.__canvas = canvas