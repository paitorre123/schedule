import numpy as np
from decimal import Decimal


#https://plot.ly/python/random-walk/
class Localizacion(object):
    def __init__(self, x, y, time):
        self.probability = []
        self.sample = []
        self.sample.append('norte')
        self.sample.append('sur')
        self.sample.append('este')
        self.sample.append('oeste')
        self.sample.append('noroeste')
        self.sample.append('noreste')
        self.sample.append('suroeste')
        self.sample.append('sureste')
        self.rastro = [[x, y, time.time]]
        self.time = time
        self.pasos = 0

    '''
        PUNTOS CARDINALES
         NO  N  NE
            \|/
          O -|- E
            /|\
         SO  S  SE
        
        POSICION EN ARREGLO
        SEGUN LA CARDINALIDAD EN self.sample[]
          4  0  5
            \|/
          3 -|- 2
            /|\
          6  1  7
    '''

    def mover_cuatro_direcciones_colision_random(self, user, grid):
        #print 'movimiento'
        #print '{}'.format(len(self.sample))
        #print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)

        if direction == 'norte':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
            if  grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1):
                self._move(user, 0, -1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[0]=sample2[0]
                self.probability[4] = sample2[1]
                self.probability[5] = sample2[2]
                self.probability[1] = sample1[0]
                self.probability[2] = sample1[1]
                self.probability[3] = sample1[2]
                self.probability[6] = sample1[3]
                self.probability[7] = sample1[4]
                #sys.exit("Error message")

        if direction == 'sur':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                self._move(user, 0, 1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[1] = sample2[0]
                self.probability[6] = sample2[1]
                self.probability[7] = sample2[2]
                self.probability[0] = sample1[0]
                self.probability[2] = sample1[1]
                self.probability[3] = sample1[2]
                self.probability[4] = sample1[3]
                self.probability[5] = sample1[4]

        if  direction == 'este':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
            if grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]):
                self._move(user, 1, 0)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[2] = sample2[0]
                self.probability[5] = sample2[1]
                self.probability[7] = sample2[2]
                self.probability[0] = sample1[0]
                self.probability[1] = sample1[1]
                self.probability[3] = sample1[2]
                self.probability[4] = sample1[3]
                self.probability[6] = sample1[4]
        if direction == 'oeste':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1]):
                self._move(user, -1, 0)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[3] = sample2[0]
                self.probability[4] = sample2[1]
                self.probability[6] = sample2[2]
                self.probability[0] = sample1[0]
                self.probability[1] = sample1[1]
                self.probability[2] = sample1[2]
                self.probability[5] = sample1[3]
                self.probability[7] = sample1[4]

        if  direction == 'noreste':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
            if  grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1):
                self._move(user, 1, -1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[0] = sample2[0]
                self.probability[3] = sample2[1]
                self.probability[4] = sample2[2]
                self.probability[1] = sample1[0]
                self.probability[2] = sample1[1]
                self.probability[5] = sample1[2]
                self.probability[6] = sample1[3]
                self.probability[7] = sample1[4]

        if  direction == 'noroeste':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
            if  grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1):
                self._move(user, -1, -1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[0] = sample2[0]
                self.probability[2] = sample2[1]
                self.probability[5] = sample2[2]
                self.probability[1] = sample1[0]
                self.probability[3] = sample1[1]
                self.probability[4] = sample1[2]
                self.probability[6] = sample1[3]
                self.probability[7] = sample1[4]

        if direction == 'sureste':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                self._move(user, 1, 1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[1] = sample2[0]
                self.probability[2] = sample2[1]
                self.probability[7] = sample2[2]
                self.probability[0] = sample1[0]
                self.probability[3] = sample1[1]
                self.probability[4] = sample1[2]
                self.probability[5] = sample1[3]
                self.probability[6] = sample1[4]

        if direction == 'suroeste':
            #print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1):
                self._move(user, -1, 1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[1] = sample2[0]
                self.probability[3] = sample2[1]
                self.probability[6] = sample2[2]
                self.probability[0] = sample1[0]
                self.probability[2] = sample1[1]
                self.probability[4] = sample1[2]
                self.probability[5] = sample1[3]
                self.probability[7] = sample1[4]

    def mover_cuatro_direcciones_colision_uniform(self, user, grid):
        #print 'Direccion uniforme'
        # print 'movimiento'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)

        if direction == 'norte':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
            if grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                self._move(user, 0, -1)
                self.pasos += 1
            else:
                self.probability[0] = (Decimal(1)*Decimal(0.2))/3
                self.probability[4] = (Decimal(1)*Decimal(0.2))/3
                self.probability[5] = (Decimal(1)*Decimal(0.2))/3
                self.probability[1] = (Decimal(1)*Decimal(0.4))
                self.probability[2] = (Decimal(1)*Decimal(0.4))/4
                self.probability[3] = (Decimal(1)*Decimal(0.4))/4
                self.probability[6] = (Decimal(1)*Decimal(0.4))/4
                self.probability[7] = (Decimal(1)*Decimal(0.4))/4
                # sys.exit("Error message")

        if direction == 'sur':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                self._move(user, 0, 1)
                self.pasos += 1
            else:

                self.probability[1] = (Decimal(1)*Decimal(0.2))/3
                self.probability[6] = (Decimal(1)*Decimal(0.2))/3
                self.probability[7] = (Decimal(1)*Decimal(0.2))/3
                self.probability[0] = (Decimal(1)*Decimal(0.4))
                self.probability[2] = (Decimal(1)*Decimal(0.4))/4
                self.probability[3] = (Decimal(1)*Decimal(0.4))/4
                self.probability[4] = (Decimal(1)*Decimal(0.4))/4
                self.probability[5] = (Decimal(1)*Decimal(0.4))/4

        if direction == 'este':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
            if grid.collision(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                self._move(user, 1, 0)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[2] = (Decimal(1)*Decimal(0.2))/3
                self.probability[5] = (Decimal(1)*Decimal(0.2))/3
                self.probability[7] = (Decimal(1)*Decimal(0.2))/3
                self.probability[3] = (Decimal(1) * Decimal(0.4))
                self.probability[0] = (Decimal(1)*Decimal(0.4))/4
                self.probability[1] = (Decimal(1)*Decimal(0.4))/4
                self.probability[4] = (Decimal(1)*Decimal(0.4))/4
                self.probability[6] = (Decimal(1)*Decimal(0.4))/4
        if direction == 'oeste':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                self._move(user, -1, 0)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[3] = (Decimal(1)*Decimal(0.2))/3
                self.probability[4] = (Decimal(1)*Decimal(0.2))/3
                self.probability[6] = (Decimal(1)*Decimal(0.2))/3
                self.probability[2] = (Decimal(1) * Decimal(0.4))
                self.probability[0] = (Decimal(1)*Decimal(0.4))/4
                self.probability[1] = (Decimal(1)*Decimal(0.4))/4
                self.probability[5] = (Decimal(1)*Decimal(0.4))/4
                self.probability[7] = (Decimal(1)*Decimal(0.4))/4

        if direction == 'noreste':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
            if grid.collision(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                self._move(user, 1, -1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[0] = (Decimal(1)*Decimal(0.2))/3
                self.probability[3] = (Decimal(1)*Decimal(0.2))/3
                self.probability[4] = (Decimal(1)*Decimal(0.2))/3
                self.probability[6] = (Decimal(1) * Decimal(0.4))
                self.probability[1] = (Decimal(1)*Decimal(0.4))/4
                self.probability[2] = (Decimal(1)*Decimal(0.4))/4
                self.probability[5] = (Decimal(1)*Decimal(0.4))/4
                self.probability[7] = (Decimal(1)*Decimal(0.4))/4

        if direction == 'noroeste':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
            if grid.collision(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                self._move(user, -1, -1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)
                self.probability[0] = (Decimal(1)*Decimal(0.2))/3
                self.probability[2] = (Decimal(1)*Decimal(0.2))/3
                self.probability[5] = (Decimal(1)*Decimal(0.2))/3
                self.probability[7] = (Decimal(1) * Decimal(0.4))
                self.probability[1] = (Decimal(1)*Decimal(0.4))/4
                self.probability[3] = (Decimal(1)*Decimal(0.4))/4
                self.probability[4] = (Decimal(1)*Decimal(0.4))/4
                self.probability[6] = (Decimal(1)*Decimal(0.4))/4


        if direction == 'sureste':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                self._move(user, 1, 1)
                self.pasos += 1
            else:
                self.probability[1] = (Decimal(1)*Decimal(0.2))/3
                self.probability[2] = (Decimal(1)*Decimal(0.2))/3
                self.probability[7] = (Decimal(1)*Decimal(0.2))/3
                self.probability[4] = (Decimal(1) * Decimal(0.4))
                self.probability[0] = (Decimal(1)*Decimal(0.4))/4
                self.probability[3] = (Decimal(1)*Decimal(0.4))/4
                self.probability[5] = (Decimal(1)*Decimal(0.4))/4
                self.probability[6] = (Decimal(1)*Decimal(0.4))/4

        if direction == 'suroeste':
            # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
            if grid.collision(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                self._move(user, -1, 1)
                self.pasos += 1
            else:
                sample1 = self._sum_to_x(5, 0.7)
                sample2 = self._sum_to_x(3, 0.3)

                self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                self.probability[5] = (Decimal(1) * Decimal(0.4))
                self.probability[0] = (Decimal(1)*Decimal(0.4))/4
                self.probability[2] = (Decimal(1)*Decimal(0.4))/4
                self.probability[4] = (Decimal(1)*Decimal(0.4))/4
                self.probability[7] = (Decimal(1)*Decimal(0.4))/4

    def mover_cuatro_direcciones_colision_uniform_north(self, user, grid):
        # print 'movimiento'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)

        if user.isNorth():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_north(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_north(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_north(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_north(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_north(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_north(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_north(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_north(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

        elif user.isNorthWest():
            #self._move(user, 1, 0)
            #self.pasos += 1
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            #self._move(user, -1, 0)
            #self.pasos += 1
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isWest():
            #self._move(user, 1, 0)
            #self.pasos += 1
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isEast():
            #self._move(user, -1, -1)
            #self.pasos += 1
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isCenter():
            #self._move(user, 0, -1)
            #self.pasos += 1
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            #self._move(user, 1, -1)
            #self.pasos += 1
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)


        elif user.isSouthEast():
            #self._move(user, -1, -1)
            #self.pasos += 1
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            #self._move(user, -1, 0)
            #self.pasos += 1
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_northWest(self, user, grid):
        #print 'movimiento noroeste'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isNorthWest():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_northWest(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_northWest(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_northWest(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_northWest(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_northWest(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_northWest(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_northWest(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_northWest(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
        elif user.isNorth():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isWest():
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isEast():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isCenter():
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthEast():
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_northEast(self, user, grid):
        #print 'movimiento noroeste'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isNorthEast():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_northEast(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_northEast(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_northEast(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_northEast(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_northEast(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_northEast(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_northEast(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_northEast(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
        elif user.isNorth():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthWest():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isWest():
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isEast():
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isCenter():
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthEast():
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_west(self, user, grid):
        # print 'movimiento noroeste'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isWest():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_west(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_west(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_west(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_west(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_west(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_west(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_west(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_west(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

        elif user.isNorth():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthWest():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isEast():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isCenter():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthEast():
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_center(self, user, grid):
        # print 'movimiento noroeste'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isCenter():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_center(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_center(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_center(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_center(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_center(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_center(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_center(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_center(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

        elif user.isNorth():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthWest():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isEast():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isWest():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthEast():
            self.probability[4] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_east(self, user, grid):
        # print 'movimiento noroeste'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isEast():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_east(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_east(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_east(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_east(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_east(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_east(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_east(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_east(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

        elif user.isNorth():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthWest():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isCenter():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isWest():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthEast():
            self.probability[0] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            self.probability[5] = (Decimal(1) * Decimal(0.3))
            self.probability[0] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_southWest(self, user, grid):
        # print 'movimiento noroeste'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isSouthWest():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_southWest(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_southWest(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_southWest(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_southWest(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_southWest(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_southWest(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_southWest(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_southWest(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

        elif user.isNorth():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthWest():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)


        elif user.isCenter():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isWest():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isEast():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthEast():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_south(self, user, grid):
        # print 'movimiento noroeste'
        # print '{}'.format(len(self.sample))
        # print '{}'.format(len(self.probability))
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isSouth():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_south(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_south(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_south(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_south(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_south(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_south(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_south(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_south(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

        elif user.isNorth():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthWest():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)


        elif user.isCenter():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isWest():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isEast():
            self.probability[6] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[3] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthEast():
            self.probability[3] = (Decimal(1) * Decimal(0.3))
            self.probability[4] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[7] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

    def mover_cuatro_direcciones_colision_uniform_southEast(self, user, grid):
        direction = np.random.choice(self.sample, 1, p=self.probability)
        if user.isSouthEast():
            if direction == 'norte':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0],  self.rastro[self.pasos][1]-1))
                if grid.collision_southEast(self.rastro[self.pasos][0], self.rastro[self.pasos][1] - 1):
                    self._move(user, 0, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[1] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4
                    # sys.exit("Error message")

            if direction == 'sur':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1))
                if grid.collision_southEast(self.rastro[self.pasos][0], self.rastro[self.pasos][1] + 1):
                    self._move(user, 0, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[0] = (Decimal(1) * Decimal(0.4))
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'este':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1]))
                if grid.collision_southEast(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1]):
                    self._move(user, 1, 0)
                    self.pasos += 1
                else:
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4
            if direction == 'oeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_southEast(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1]):
                    self._move(user, -1, 0)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noreste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] - 1))
                if grid.collision_southEast(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, 1, -1)
                    self.pasos += 1
                else:
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'noroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] - 1))
                if grid.collision_southEast(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] - 1):
                    self._move(user, -1, -1)
                    self.pasos += 1
                else:
                    sample1 = self._sum_to_x(5, 0.7)
                    sample2 = self._sum_to_x(3, 0.3)
                    self.probability[0] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.4))
                    self.probability[1] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'sureste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]+1, self.rastro[self.pasos][1] + 1))
                if grid.collision_southEast(self.rastro[self.pasos][0] + 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, 1, 1)
                    self.pasos += 1
                else:
                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[2] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[7] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[4] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[3] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[5] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[6] = (Decimal(1) * Decimal(0.4)) / 4

            if direction == 'suroeste':
                # print 'Collision?: {}'.format(grid.collision(self.rastro[self.pasos][0]-1, self.rastro[self.pasos][1] + 1))
                if grid.collision_southEast(self.rastro[self.pasos][0] - 1, self.rastro[self.pasos][1] + 1):
                    self._move(user, -1, 1)
                    self.pasos += 1
                else:

                    self.probability[1] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[3] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[6] = (Decimal(1) * Decimal(0.2)) / 3
                    self.probability[5] = (Decimal(1) * Decimal(0.4))
                    self.probability[0] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[2] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[4] = (Decimal(1) * Decimal(0.4)) / 4
                    self.probability[7] = (Decimal(1) * Decimal(0.4)) / 4

        elif user.isNorth():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthWest():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isNorthEast():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)


        elif user.isCenter():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)


        elif user.isWest():
            self.probability[7] = (Decimal(1) * Decimal(0.3))
            self.probability[1] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[2] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)


        elif user.isEast():
            self.probability[1] = (Decimal(1) * Decimal(0.3))
            self.probability[6] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[2] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[5] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouth():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)

        elif user.isSouthWest():
            self.probability[2] = (Decimal(1) * Decimal(0.3))
            self.probability[5] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[7] = (Decimal(1) * Decimal(0.5)) / 2
            self.probability[0] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[1] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[3] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[4] = (Decimal(1) * Decimal(0.2)) / 5
            self.probability[6] = (Decimal(1) * Decimal(0.2)) / 5
            self.mover_cuatro_direcciones_colision_uniform(user=user, grid=grid)


    def _move(self, user, x, y):
        user.point.pointX = self.rastro[self.pasos][0] + x
        user.point.pointY = self.rastro[self.pasos][1] + y
        user.painter.canvas.coords(user.oval, user.point.pointX - 2, user.point.pointY - 2, user.point.pointX + 2, user.point.pointY + 2)
        self.rastro.append([self.rastro[self.pasos][0] + x, self.rastro[self.pasos][1] + y, self.time.time])

    def _sum_to_x(self, n, x):
        values = [0.0, x] + list(np.random.uniform(low=0.0, high=x, size=n - 1))
        values.sort()
        return [values[i + 1] - values[i] for i in range(n)]

    def obtener_psicion_rastro(self):
        try:
            return self.rastro.__getitem__(self.time.time)
        except IndexError:
            return self.rastro.__getitem__(len(self.rastro)-1)

    def obtener_psicion_en_tiempo(self, time):
        try:
            return self.rastro.__getitem__(time)
        except IndexError:
            return self.rastro.__getitem__(len(self.rastro) - 1)
