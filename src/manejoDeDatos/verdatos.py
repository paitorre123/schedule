from src.manejoDeDatos.grafico import Grafico
import os


class Simbol(object):
    @classmethod
    def simbolic_four(cls, d1, d2, d3, d4):
        data_1 = "\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}] \n".format(d1[0],
                                                                                                                d1[1],
                                                                                                                d1[2],
                                                                                                                d1[3],
                                                                                                                d1[4],
                                                                                                                d1[5],
                                                                                                                d1[6])
        data_2 = "\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}] \n".format(d2[0],
                                                                                                                d2[1],
                                                                                                                d2[2],
                                                                                                                d2[3],
                                                                                                                d2[4],
                                                                                                                d2[5],
                                                                                                                d2[6])
        data_3 = "\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}] \n".format(d3[0],
                                                                                                                d3[1],
                                                                                                                d3[2],
                                                                                                                d3[3],
                                                                                                                d3[4],
                                                                                                                d3[5],
                                                                                                                d3[6])
        data_4 = "\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(d4[0],
                                                                                                             d1[1],
                                                                                                             d4[2],
                                                                                                             d1[3],
                                                                                                             d4[4],
                                                                                                             d4[5],
                                                                                                             d4[6])
        return "\caption[]{ \n" + data_1 + data_2 + data_3 + data_4 + "}"

    @classmethod
    def simbolic_three(cls, d1, d2, d3):
        data_1 = "\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}] \n".format(d1[0],
                                                                                                                d1[1],
                                                                                                                d1[2],
                                                                                                                d1[3],
                                                                                                                d1[4],
                                                                                                                d1[5],
                                                                                                                d1[6])
        data_2 = "\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}] \n".format(d2[0],
                                                                                                                d2[1],
                                                                                                                d2[2],
                                                                                                                d2[3],
                                                                                                                d2[4],
                                                                                                                d2[5],
                                                                                                                d2[6])
        data_3 = "\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}] \n".format(d3[0],
                                                                                                                d3[1],
                                                                                                                d3[2],
                                                                                                                d3[3],
                                                                                                                d3[4],
                                                                                                                d3[5],
                                                                                                                d3[6])
        return "\caption[]{ \n" + data_1 + data_2 + data_3 + "}"


algoritmosScheduleDeterminista = [
    ['\[AlgoritmoDeEnvergaduraDeterminista]', 'E'],  # 0
    ['\[AlgoritmoDePopularidadDeterminista]', 'P'],  # 1
    ['\[AlgoritmoRelevanciaDeterminista]', 'P']  # 2
]
algoritmosScheduleProbabilista = [
    ['\[AlgoritmoDeEnvergaduraProbabilista]', 'PE'],  # 0
    ['\[AlgoritmoDePopularidadProbabilista]', 'PP'],  # 1
    ['\[AlgoritmoRelevanciaProbabilista]', 'PR'],  # 2
    ['\[AlgoritmoDeEnvergaduraProbabilistaConTiempoDeEspera]', 'ExW'],  # 3
    ['\[AlgoritmoDePopularidadProbabilistaConTiempoDeEspera]', 'PxW'],  # 4
    ['\[AlgoritmoRelevanciaProbabilistaConTiempoDeEspera]', 'RxW']  # 5
]
algoritmoSeleccion = [
    ['[CargaDeTrabajo]', 'C'],  # 0
    ['[Jitter]', 'J'],  # 1
    ['[Stretch]', 'S']  # 0
]

numeroCarpeta = 1
fileToModify = '/tiempo_respuesta_total.tex'
urlToModify = 'C:/Users/pablo/Study/Tesis/Tesis-documento - mejorado/graficos/datos-{}'
lineToModify = "\caption[]"

if __name__ == '__main__':

    for asd in algoritmosScheduleDeterminista:
        """Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}"""
        d1 = ["{}-{}".format(asd[1], 200), 200, 4, 1600, 1400, 3, 100]
        d2 = ["{}-{}".format(asd[1], 300), 300, 4, 1600, 1400, 3, 100]
        d3 = ["{}-{}".format(asd[1], 400), 400, 4, 1600, 1400, 3, 100]
        d4 = ["{}-{}".format(asd[1], 500), 500, 4, 1600, 1400, 3, 100]
        f = Simbol.simbolic_four(d1, d2, d3, d4)
        urtm = urlToModify.format(numeroCarpeta)
        # os.system('pause')
        Grafico._replace_all(urtm + fileToModify, lineToModify, f)
        print urtm + "->" + f
        numeroCarpeta += 1

    for asd in algoritmosScheduleProbabilista:
        for ads in algoritmoSeleccion:
            """Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}"""
            d1 = ["{}-{}-{}".format(asd[1], ads[1], 200), 200, 4, 1600, 1400, 3, 100]
            d2 = ["{}-{}-{}".format(asd[1], ads[1], 300), 300, 4, 1600, 1400, 3, 100]
            d3 = ["{}-{}-{}".format(asd[1], ads[1], 400), 400, 4, 1600, 1400, 3, 100]
            d4 = ["{}-{}-{}".format(asd[1], ads[1], 500), 500, 4, 1600, 1400, 3, 100]

            f = Simbol.simbolic_four(d1, d2, d3, d4)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm + fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for users in [200, 300, 400, 500]:
        """Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}"""
        d1 = ["{}".format(algoritmosScheduleDeterminista[0][1]), users, 4, 1600, 1400, 3, 100]
        d2 = ["{}".format(algoritmosScheduleDeterminista[1][1]), users, 4, 1600, 1400, 3, 100]
        d3 = ["{}".format(algoritmosScheduleDeterminista[2][1]), users, 4, 1600, 1400, 3, 100]

        f = Simbol.simbolic_three(d1, d2, d3)
        urtm = urlToModify.format(numeroCarpeta)
        Grafico._replace_all(urtm + fileToModify, lineToModify, f)
        print urtm + "->" + f
        numeroCarpeta += 1

    for users in [200, 300, 400, 500]:
        for ads in algoritmoSeleccion:
            """Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}"""
            d1 = ["{}-{}".format(algoritmosScheduleProbabilista[0][1], ads[1]), users, 4, 1600, 1400, 3, 100]
            d2 = ["{}-{}".format(algoritmosScheduleDeterminista[1][1], ads[1]), users, 4, 1600, 1400, 3, 100]
            d3 = ["{}-{}".format(algoritmosScheduleDeterminista[2][1], ads[1]), users, 4, 1600, 1400, 3, 100]
            f = Simbol.simbolic_three(d1, d2, d3)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm + fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for users in [200, 300, 400, 500]:
        for ads in algoritmoSeleccion:
            """Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}"""
            d1 = ["{}".format(algoritmosScheduleProbabilista[3][1], ads[1]), users, 4, 1600, 1400, 3, 100]
            d2 = ["{}".format(algoritmosScheduleDeterminista[4][1], ads[1]), users, 4, 1600, 1400, 3, 100]
            d3 = ["{}".format(algoritmosScheduleDeterminista[5][1], ads[1]), users, 4, 1600, 1400, 3, 100]

            f = Simbol.simbolic_three(d1, d2, d3)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm + fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for asd in algoritmosScheduleDeterminista:
        for ads in ['[None]']:
            d1 = ["{}-{}".format(asd[1], "K-4"), 200, 4, 1600, 1400, 3, 100]
            d2 = ["{}-{}".format(asd[1], "K-6"), 200, 6, 1600, 1400, 3, 100]
            d3 = ["{}-{}".format(asd[1], "K-8"), 200, 8, 1600, 1400, 3, 100]
            d4 = ["{}-{}".format(asd[1], "K-10"), 200, 10, 1600, 1400, 3, 100]

            f = Simbol.simbolic_four(d1, d2, d3, d4)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm + fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for asd in algoritmosScheduleProbabilista:
        for ads in algoritmoSeleccion:
            d1 = "{}-{}-{}".format(asd[1], ads[1], "K-4")
            d2 = "{}-{}-{}".format(asd[1], ads[1], "K-6")
            d3 = "{}-{}-{}".format(asd[1], ads[1], "K-8")
            d4 = "{}-{}-{}".format(asd[1], ads[1], "K-10")
            f = Simbol.simbolic_four(d1, d2, d3, d4)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm + fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for asd in algoritmosScheduleDeterminista:
        for anmt in [4, 6, 8, 10]:
            for ads in ['[None]']:
                d1 = "{}-{}".format(asd[1], "R-1")
                d2 = "{}-{}".format(asd[1], "R-3")
                d3 = "{}-{}".format(asd[1], "R-6")
                f = Simbol.simbolic_three(d1, d2, d3)
                urtm = urlToModify.format(numeroCarpeta)
                Grafico._replace_all(urtm + fileToModify, lineToModify, f)
                print urtm + "->" + f
                numeroCarpeta += 1

    for asd in algoritmosScheduleProbabilista:
        for anmt in [4, 6, 8, 10]:
            for ads in algoritmoSeleccion:
                d1 = "{}-{}-{}".format(asd[1], ads[1], "R-1")
                d2 = "{}-{}-{}".format(asd[1], ads[1], "R-3")
                d3 = "{}-{}-{}".format(asd[1], ads[1], "R-6")
                f = Simbol.simbolic_three(d1, d2, d3)
                urtm = urlToModify.format(numeroCarpeta)
                Grafico._replace_all(urtm + fileToModify, lineToModify, f)
                print urtm + "->" + f
                numeroCarpeta += 1

    for asd in algoritmosScheduleDeterminista:
        for anmt in [4, 6, 8, 10]:
            for ads in ['[None]']:
                d1 = "{}-{}".format(asd[1], "T-50")
                d2 = "{}-{}".format(asd[1], "T-100")
                d3 = "{}-{}".format(asd[1], "T-200")
                f = Simbol.simbolic_three(d1, d2, d3)
                urtm = urlToModify.format(numeroCarpeta)
                Grafico._replace_all(urtm + fileToModify, lineToModify, f)
                print urtm + "->" + f
                numeroCarpeta += 1

    for asd in algoritmosScheduleProbabilista:
        for anmt in [4, 6, 8, 10]:
            for ads in algoritmoSeleccion:
                d1 = "{}-{}-{}".format(asd[1], ads[1], "T-50")
                d2 = "{}-{}-{}".format(asd[1], ads[1], "T-100")
                d3 = "{}-{}-{}".format(asd[1], ads[1], "T-200")
                f = Simbol.simbolic_three(d1, d2, d3)
                urtm = urlToModify.format(numeroCarpeta)
                Grafico._replace_all(urtm + fileToModify, lineToModify, f)
                print urtm + "->" + f
                numeroCarpeta += 1