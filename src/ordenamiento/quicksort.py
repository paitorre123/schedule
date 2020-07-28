

class QuickSort(object):

    @classmethod
    def array_menorAMayor(cls, A, izq, der):
        pivote = A[izq]
        i = izq
        j = der

        while i < j:
            while A[i]<= pivote and i < j:
                i += 1
            while A[j]> pivote:
                j -= 1
            if i < j:
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
        A[izq] = A[j]
        A[j] = pivote
        if izq < j - 1:
            cls.array_menorAMayor(A, izq, j - 1)
        if j + 1 < der:
            cls.array_menorAMayor(A, j + 1, der)

    @classmethod
    def menorAMayor(cls, A, izq, der):
        pivote = A[izq]
        i = izq
        j = der

        while i < j:
            while A[i].puntuacion <= pivote.puntuacion and i < j:
                i += 1
            while A[j].puntuacion > pivote.puntuacion:
                j -= 1
            if i < j:
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
        A[izq] = A[j]
        A[j] = pivote
        if izq < j - 1:
            cls.menorAMayor(A, izq, j - 1)
        if j + 1 < der:
            cls.menorAMayor(A, j + 1, der)

    @classmethod
    def mayorAMenor(cls, A, izq, der):
        pivote = A[izq]
        i = izq
        j = der

        while i < j:
            while A[i].puntuacion >= pivote.puntuacion and i < j:
                i += 1
            while A[j].puntuacion < pivote.puntuacion:
                j -= 1
            if i < j:
                aux = A[i]
                A[i] = A[j]
                A[j] = aux
        A[izq] = A[j]
        A[j] = pivote
        if izq < j - 1:
            cls.mayorAMenor(A, izq, j - 1)
        if j + 1 < der:
            cls.mayorAMenor(A, j + 1, der)