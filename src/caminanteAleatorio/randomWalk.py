from random import choice
import matplotlib.pyplot as plt
from src.client.cliente import Usuario
import numpy as np


class RandomWalk():
    # class to generate a random walk
    def __init__(self, user):

        # start from(0,0)
        self.x = user.point.pointX
        self.y = user.point.pointY
        print '{}'.format(np.concatenate((np.arange(1, 0, -0.1), np.arange(0, -1.1, -0.1)), axis=0))
        self.direccion = ['norte', 'sur', 'este', 'oeste', 'noreste', 'noroeste', 'sureste', 'suroeste']
        self.paso = 0
        self.velocidad = 0
        self.rastro[:, 0] = [self.x, self.y]


    def random_walk(self):
        pass


if __name__=='__main__':
    u = Usuario()
    u.point.pointX = 350
    u.point.pointY = 220

    rw = RandomWalk()
    #plt.scatter(rw.x, rw.y, s=1)
    #plt.plot(rw.x, rw.y)
    #plt.show()