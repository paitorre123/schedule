import os
import numpy as np


class Probabilista(object):

    @classmethod
    def ordenarProbabilista(cls, A):
        try:
            return np.random.choice(A, len(A), p=[o.puntuacion for o in A], replace=False)
        except ValueError:
            for _ in A:
                print '{}'.format(_)
                print 'Error en el ordenamiento probabilista'
                os.system('pause')
