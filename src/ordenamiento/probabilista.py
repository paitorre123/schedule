import os
import numpy as np


class Probabilista(object):

    @classmethod
    def ordenarProbabilista(cls, A):
        return np.random.choice(A, len(A), p=[o.puntuacion for o in A], replace=False)

