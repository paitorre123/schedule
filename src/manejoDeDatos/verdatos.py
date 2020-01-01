from src.manejoDeDatos.grafico import Grafico
import os

class Simbol(object):
    @classmethod
    def simbolic_four(self, d1, d2, d3,d4):
        return "symbolic x coords={"+ d1 + ", "+ d2 + ", "+ d3 + ", "+ d4 + "}, "

    @classmethod
    def simbolic_three(self, d1, d2, d3):
        return "symbolic x coords={" + d1 + ", " + d2 + ", " + d3 + "}, "

algoritmosScheduleDeterminista = [
                                      ['\[AlgoritmoDeEnvergaduraDeterminista]', 'AED'],#0
                                      ['\[AlgoritmoDePopularidadDeterminista]', 'APD'],#1
                                      ['\[AlgoritmoRelevanciaDeterminista]', 'ARD']#2
                                     ]
algoritmosScheduleProbabilista =[
                                  ['\[AlgoritmoDeEnvergaduraProbabilista]', 'AEP'],#0
                                  ['\[AlgoritmoDePopularidadProbabilista]', 'APP'],#1
                                  ['\[AlgoritmoRelevanciaProbabilista]', 'ARP'],#2
                                  ['\[AlgoritmoDeEnvergaduraProbabilistaConTiempoDeEspera]', 'AEPT'],#3
                                  ['\[AlgoritmoDePopularidadProbabilistaConTiempoDeEspera]', 'APPT'],#4
                                  ['\[AlgoritmoRelevanciaProbabilistaConTiempoDeEspera]', 'ARPT']#5
                                ]
algoritmoSeleccion = [
                      ['[CargaDeTrabajo]', 'ASC'],#0
                      ['[Jitter]', 'ASJ'],#1
                      ['[Stretch]', 'ASS']#0
                      ]

numeroCarpeta = 1
fileToModify = '/obsolescencia.tex'
urlToModify = 'C:/Users/EMANON/Desktop/Tesis/graficos/datos-{}'
lineToModify = "symbolic x coords={AEP-ASJ-T-50, AEP-ASS-T-50, AEP-ASC-T-50},"



if __name__ == '__main__':
    j = [1,2,3,4,5,6,7,8,9,10]
    j2 = sorted(i for i in j if i >= 5)
    print j2
    os.system('pause')
    for asd in algoritmosScheduleDeterminista:
        d1 = "{}-{}".format(asd[1], 200)
        d2 = "{}-{}".format(asd[1], 300)
        d3 = "{}-{}".format(asd[1], 400)
        d4 = "{}-{}".format(asd[1], 500)
        f = Simbol.simbolic_four(d1, d2, d3,d4)
        urtm = urlToModify.format(numeroCarpeta)
        Grafico._replace_all(urtm+fileToModify, lineToModify, f)
        print urtm +"->"+ f
        numeroCarpeta += 1

    for asd in algoritmosScheduleProbabilista:
        for ads in algoritmoSeleccion:
            d1 = "{}-{}-{}".format(asd[1], ads[1], 200)
            d2 = "{}-{}-{}".format(asd[1], ads[1], 300)
            d3 = "{}-{}-{}".format(asd[1], ads[1], 400)
            d4 = "{}-{}-{}".format(asd[1], ads[1], 500)
            f = Simbol.simbolic_four(d1, d2, d3,d4)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm+fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for users in [200, 300, 400, 500]:
        d1 =  "{}".format(algoritmosScheduleDeterminista[0][1])
        d2 =  "{}".format(algoritmosScheduleDeterminista[1][1])
        d3 =  "{}".format(algoritmosScheduleDeterminista[2][1])
        f = Simbol.simbolic_three(d1, d2, d3)
        urtm = urlToModify.format(numeroCarpeta)
        Grafico._replace_all(urtm + fileToModify, lineToModify, f)
        print urtm + "->" + f
        numeroCarpeta += 1

    for users in [200, 300, 400, 500]:
        for ads in algoritmoSeleccion:
            d1 = "{}-{}".format(algoritmosScheduleProbabilista[0][1],ads[1])
            d2 = "{}-{}".format(algoritmosScheduleProbabilista[1][1],ads[1])
            d3 = "{}-{}".format(algoritmosScheduleProbabilista[2][1],ads[1])
            f = Simbol.simbolic_three(d1, d2, d3)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm + fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for users in [200, 300, 400, 500]:
        for ads in algoritmoSeleccion:
            d1 =  "{}-{}".format(algoritmosScheduleProbabilista[3][1],ads[1])
            d2 =  "{}-{}".format(algoritmosScheduleProbabilista[4][1],ads[1])
            d3 =  "{}-{}".format(algoritmosScheduleProbabilista[5][1],ads[1])
            f = Simbol.simbolic_three(d1, d2, d3)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm+fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for asd in algoritmosScheduleDeterminista:
        for ads in ['[None]']:
            d1 = "{}-{}".format(asd[1], "K-4")
            d2 = "{}-{}".format(asd[1], "K-6")
            d3 = "{}-{}".format(asd[1], "K-8")
            d4 = "{}-{}".format(asd[1], "K-10")
            f = Simbol.simbolic_four(d1, d2, d3,d4)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm+fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for asd in algoritmosScheduleProbabilista:
        for ads in algoritmoSeleccion:
            d1 = "{}-{}-{}".format(asd[1], ads[1], "K-4")
            d2 = "{}-{}-{}".format(asd[1], ads[1], "K-6")
            d3 = "{}-{}-{}".format(asd[1], ads[1], "K-8")
            d4 = "{}-{}-{}".format(asd[1], ads[1], "K-10")
            f = Simbol.simbolic_four(d1, d2, d3,d4)
            urtm = urlToModify.format(numeroCarpeta)
            Grafico._replace_all(urtm+fileToModify, lineToModify, f)
            print urtm + "->" + f
            numeroCarpeta += 1

    for asd in algoritmosScheduleDeterminista:
        for anmt in [4,6,8,10]:
            for ads in ['[None]']:
                d1 = "{}-{}".format(asd[1], "R-1")
                d2 = "{}-{}".format(asd[1], "R-3")
                d3 = "{}-{}".format(asd[1], "R-6")
                f = Simbol.simbolic_three(d1, d2, d3)
                urtm = urlToModify.format(numeroCarpeta)
                Grafico._replace_all(urtm+fileToModify, lineToModify, f)
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
                Grafico._replace_all(urtm+fileToModify, lineToModify, f)
                print urtm + "->" + f
                numeroCarpeta += 1

    for asd in algoritmosScheduleDeterminista:
        for anmt in [4, 6, 8, 10]:
            for ads in ['[None]']:
                d1 =  "{}-{}".format(asd[1], "T-50")
                d2 =  "{}-{}".format(asd[1], "T-100")
                d3 =  "{}-{}".format(asd[1], "T-200")
                f = Simbol.simbolic_three(d1, d2, d3)
                urtm = urlToModify.format(numeroCarpeta)
                Grafico._replace_all(urtm+fileToModify, lineToModify, f)
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
                Grafico._replace_all(urtm+fileToModify, lineToModify, f)
                print urtm + "->" + f
                numeroCarpeta += 1