import fileinput
import sys
import numpy as np
from decimal import *
from src.manejoDeDatos.generadorDeArchivosBase import GeneradorDeArchivosBase
import math
from src.manejoDeDatos.tablaDescriptiva import TablaDescriptiva
import os



class Grafico(object):

    @classmethod
    def _replace_all(cls, file, searchExp, replaceExp):
        for line in fileinput.input(file, inplace=1):
            if searchExp in line:
                line = line.replace(searchExp, replaceExp)
            sys.stdout.write(line)

    @classmethod
    def cues_encubiertas_enviadas(cls, file, estadisticas):
        #
        nombreGrafico = '\cues_enviadas_servidor.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        cuesMaximas = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.cuesQueArriban.items():
                if int(key) > tiempoMaximo:
                    tiempoMaximo = int(key)
                if len(values) > cuesMaximas:
                    cuesMaximas = len(values)

        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)


        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')

        cls._replace_all(file, "%xmin%", "101")
        cls._replace_all(file, "%xmax%", str(tiempoMaximo))
        cls._replace_all(file, "%xtick%",xtick)
        cls._replace_all(file, "%xticklabels%", xtick)
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%ymax%", str(cuesMaximas))
        cls._replace_all(file, "%xlabel%", "Tiempo de arribo")
        cls._replace_all(file, "%ylabel%", "Numero de Cues que arriban")
        cls._replace_all(file, "%title%", "Consultas encubiertas enviadas")
        datos = ''
        for e in estadisticas:
            datos += '\\addplot coordinates{'
            for key, values in e.cuesQueArriban.items():
                datos += '({},{})\n'.format(key, len(values))
            datos += '}; \\addlegendentry{'+ str(e.tecnica) + '}; \n'
        cls._replace_all(file, "%addplot%", datos)

        descrip = ''
        name = 'cues_encubiertas_enviadas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)


    @classmethod
    def cues_que_arriban_demanda_total(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Total de cues que arriban")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Numero de cues")

        cuesMaximas = 0
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, sum([len(x) for x in e.cuesQueArriban.values()]) )
            if sum([len(x) for x in e.cuesQueArriban.values()]) > cuesMaximas:
                cuesMaximas = sum([len(x) for x in e.cuesQueArriban.values()])
        datos += '};\n'
        cls._replace_all(file, "%addplot%", datos)
        cls._replace_all(file, "%ymax%", str(cuesMaximas))
        descrip = ''
        name = 'cues_que_arriban_demanda_total:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def razon_cues_arribadas_sobre_tiempo(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Razon cues arribadas sobre tiempo")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "$ \\frac{Cues que arriban}{ Tiempo en que arriban} $")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, str(  Decimal(sum([len(x) for x in e.cuesQueArriban.values()])) / Decimal(max(e.cuesQueArriban))  ) )
        datos += '};\n'
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'razon_cues_arribadas_sobre_tiempo:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def cues_creadas(cls, file, estadisticas):
        #
        nombreGrafico = '\cues_creadas.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        cuesMaximas = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.cuesCreadasPorTiempo.items():
                if int(key) > tiempoMaximo:
                    tiempoMaximo = int(key)
                if len(values) > cuesMaximas:
                    cuesMaximas = len(values)
        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)

        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')
        xtick = '{}'.format(xtick).replace("'", '')
        xtick = '{}'.format(xtick).replace('u', '')
        cls._replace_all(file, "%xmin%", "0")
        cls._replace_all(file, "%xmax%", str(tiempoMaximo))
        cls._replace_all(file, "%xtick%", xtick)
        cls._replace_all(file, "%xticklabels%", xtick)
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%ymax%", str(cuesMaximas))
        cls._replace_all(file, "%xlabel%", "Tiempo de creacion")
        cls._replace_all(file, "%ylabel%", "Numero de Cues creadas")
        cls._replace_all(file, "%title%", "Consultas encubiertas creadas")
        datos = ''
        for e in estadisticas:
            datos += '\\addplot coordinates{'
            for key, values in e.cuesCreadasPorTiempo.items():
                datos += '({},{})\n'.format(key, len(values))
            datos += '}; \\addlegendentry{'+ str(e.tecnica) + ' }; \n'
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'cues_creadas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def razon_de_privacidad(cls, file, estadisticas):
        #
        nombreGrafico = '\\razon_privacidad.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_barra_simple(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Razon de privacidad")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "$ \\frac{Cues que arriban}{Cues creadas} $")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        maxim = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, str(Decimal(sum([len(x) for x in e.cuesQueArriban.values()])) / Decimal(sum([len(x) for x in e.cuesCreadasPorusuarios.values()]))))
            if Decimal(sum([len(x) for x in e.cuesQueArriban.values()])) / Decimal(sum([len(x) for x in e.cuesCreadasPorusuarios.values()])) > maxim :
                maxim = Decimal(sum([len(x) for x in e.cuesQueArriban.values()])) / Decimal(sum([len(x) for x in e.cuesCreadasPorusuarios.values()]))
        cls._replace_all(file, "%ymax%", '0.6')
        cls._replace_all(file, "%ymin%", '0.0')
        cls._replace_all(file, "%precision%", '2')
        datos += '};\n'
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'razon_de_arribo:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Efectividad={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def cues_creadas_respondidas(cls, file, estadisticas):
        #
        nombreGrafico = '\carga_trabajo_sistema.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        cuesMaximas = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.cuesCreadasRespondidas.items():

                if int(str(key).split(':')[1]) > int(tiempoMaximo):
                    tiempoMaximo = str(key).split(':')[1]
                if len(values) > cuesMaximas:
                    cuesMaximas = len(values)
        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)

        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')
        xtick = '{}'.format(xtick).replace("'", '')
        xtick = '{}'.format(xtick).replace('u', '')


        cls._replace_all(file, "%xmin%", "0")
        cls._replace_all(file, "%xmax%", "8750")
        cls._replace_all(file, "%xtick%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%xticklabels%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%ymax%", str( int(math.ceil(cuesMaximas/ 200.0)) * 200))
        cls._replace_all(file, "%xlabel%", "Tiempo de difusion de cronograma")
        cls._replace_all(file, "%ylabel%", "Numero de Cues creadas")
        cls._replace_all(file, "%title%", "Carga de trabajo del sistema dinamico")

        datostabla = ''
        datos = ''
        for e in estadisticas:
            datos += '\\addplot coordinates{'
            tiemposCronogramas = []
            numeroRespondidas = []
            for key, values in e.cuesCreadasRespondidas.items():
                tiemposCronogramas.append(int(str(key).split(':')[1]))
                numeroRespondidas.append(len(values))
                datos += '({},{})\n'.format(str(key).split(':')[1], len(values))
            datostabla += "{} & {}&{:.4f}&{}&{} \\\\ \n".format(e.tecnica,len(numeroRespondidas), sum(numeroRespondidas), np.average(numeroRespondidas), max(tiemposCronogramas))
            datos += '}; \\addlegendentry{ '+ str(e.tecnica) + ' }; \n'
        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_carga_trabajo_sistema(datostabla))
        cls._replace_all(file, "%addplot%", datos)



        descrip = ''
        name = 'cues_creadas_respondidas:'
        for e in estadisticas:
            descrip += "\n\t\t \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)
        cls._replace_all(file, "%name%", name)

    @classmethod
    def cues_recibidas_respondidas(cls, file, estadisticas):
        #
        nombreGrafico = '\carga_trabajo_servidor.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        cuesMaximas = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.cuesRecibidasRespondidas.items():

                if int(str(key).split(':')[1]) > int(tiempoMaximo):
                    tiempoMaximo = str(key).split(':')[1]
                if len(values) > cuesMaximas:
                    cuesMaximas = len(values)
        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)

        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')
        xtick = '{}'.format(xtick).replace("'", '')
        xtick = '{}'.format(xtick).replace('u', '')

        cls._replace_all(file, "%xmin%", "0")
        cls._replace_all(file, "%xmax%", "8750")
        cls._replace_all(file, "%xtick%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%xticklabels%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%xlabel%", "Tiempo de difusion de cronograma")
        cls._replace_all(file, "%ylabel%", "Numero de Cues enviadas")
        cls._replace_all(file, "%title%", "Carga de trabajo del servidor acumulado")
        datos = ''
        acumuladoMax = 0
        datostabla = ''
        for e in estadisticas:
            acumulado = 0
            datos += '\\addplot coordinates{'
            tiemposCronogramas = []
            numeroRespondidas = []
            for key, values in e.cuesRecibidasRespondidas.items():
                acumulado += len(values)
                tiemposCronogramas.append(int(str(key).split(':')[1]))
                numeroRespondidas.append(len(values))
                datos += '({},{})\n'.format(str(key).split(':')[1], acumulado)
                if acumulado > acumuladoMax:
                    acumuladoMax = acumulado
            datostabla += "{} & {}&{}&{:.4f}&{}\\\\ \n".format(e.tecnica,len(numeroRespondidas), sum(numeroRespondidas), np.average(numeroRespondidas), max(tiemposCronogramas))
            datos += '}; \\addlegendentry{ ' + str(e.tecnica) + ' }; \n'

        cls._replace_all(file, "%ymax%", "1500")
        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_carga_trabajo_servidor(datostabla))
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'cues_recibidas_respondidas:'
        for e in estadisticas:
            descrip += "\n\t\t \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def razon_utilidad(cls, file, estadisticas):
        #
        nombreGrafico = '\\razon_utilidad.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        cuesMaximas = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.utilidadDeProgramas.items():

                if int(str(key).split(':')[1]) > int(tiempoMaximo):
                    tiempoMaximo = str(key).split(':')[1]
                if Decimal(len(values))/ Decimal( int(str(key).split(':')[1])-int(str(key).split(':')[0])) > cuesMaximas:
                    cuesMaximas = len(values)

        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)

        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')
        xtick = '{}'.format(xtick).replace("'", '')
        xtick = '{}'.format(xtick).replace('u', '')

        cls._replace_all(file, "%xmin%", "0")
        cls._replace_all(file, "%xmax%", "8750")
        cls._replace_all(file, "%xtick%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%xticklabels%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%ymax%", "1")
        cls._replace_all(file, "%xlabel%", "Tiempo de difusion de programa")
        cls._replace_all(file, "%ylabel%", "$\\frac{elementos requeridos en programa}{largo del programa}$")
        cls._replace_all(file, "%title%", "Razon de utilidad")
        datos = ''
        datosTabla = ''
        for e in estadisticas:
            datos += '\\addplot coordinates{'
            utilidad = []
            elementosEncontrados = []
            largoProgramas = []
            for key, values in e.utilidadDeProgramas.items():
                utilidad.append(float(values[0]))
                elementosEncontrados.append(float(values[1]))
                largoProgramas.append(float(values[2]))
                datos += '({},{})\n'.format(str(key).split(':')[1], values[0])

            datosTabla += '{}  &  {:.4f}&{:.4f}&{:.4f}\\\\ \n'.format(e.tecnica, np.average(elementosEncontrados), np.average(largoProgramas), np.average(utilidad))

            datos += '}; \\addlegendentry{ '+ str(e.tecnica) +'}; \n'
        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_razon_utilidad(datosTabla))
        cls._replace_all(file, "smooth" , "smooth,\n\t\t\t\tlegend style={at={(0.5,-0.25)},anchor=north,legend columns=-1},")
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'razon_utilidad:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Efectividad={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def razon_efectividad(cls, file, estadisticas):
        #
        nombreGrafico = '\\razon_efectividad.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        cuesMaximas = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.efectividadProgramas.items():

                if int(str(key).split(':')[1]) > int(tiempoMaximo):
                    tiempoMaximo = str(key).split(':')[1]
                if Decimal(len(values)) / Decimal(
                    int(str(key).split(':')[1]) - int(str(key).split(':')[0])) > cuesMaximas:
                    cuesMaximas = len(values)

        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)

        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')
        xtick = '{}'.format(xtick).replace("'", '')
        xtick = '{}'.format(xtick).replace('u', '')

        cls._replace_all(file, "%xmin%", "0")
        cls._replace_all(file, "%xmax%", "8750")
        cls._replace_all(file, "%xtick%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%xticklabels%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%ymax%", "1")
        cls._replace_all(file, "%xlabel%", "Tiempo de difusion de programa")
        cls._replace_all(file, "%ylabel%", "$\\frac{elementos requeridos en programa}{total elementos requeridos}$")
        cls._replace_all(file, "%title%", "Razon de efectividad")
        datos = ''
        datosTabla = ''
        for e in estadisticas:
            datos += '\\addplot coordinates{'
            efectividad = []
            elementosEncontrados = []
            itemessolicitados = []
            for key, values in e.efectividadProgramas.items():
                efectividad.append(float(values[0]))
                elementosEncontrados.append(float(values[1]))
                itemessolicitados.append(float(values[2]))
                datos += '({},{})\n'.format(str(key).split(':')[1], values[0])
            datos += '}; \\addlegendentry{ ' + str(e.tecnica) + '}; \n'
            datosTabla += '{}  &  {:.4f}&{:.4f}&{:.4f}\\\\ \n'.format(e.tecnica, np.average(elementosEncontrados), np.average(itemessolicitados), np.average(efectividad))
        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_razon_efectividad(datosTabla))
        cls._replace_all(file, "smooth" , "smooth,\n\t\t\t\tlegend style={at={(0.5,-0.25)},anchor=north,legend columns=-1},")
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'razon_efectividad:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Efectividad={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def razon_cues_creadas_respondidas(cls,file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Razon de cues creadas respondidas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "$ \\frac{Cues creadas}{Tiempo en que se responden} $")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        maxim = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, str(Decimal(sum([len(x) for x in e.cuesCreadasRespondidas.values()])) / Decimal(e.tiempoDemandaCumplidaCuesCreadas)))
            if Decimal(sum([len(x) for x in e.cuesCreadasRespondidas.values()])) / Decimal(e.tiempoDemandaCumplidaCuesCreadas) > maxim :
                maxim = Decimal(sum([len(x) for x in e.cuesCreadasRespondidas.values()])) / Decimal(e.tiempoDemandaCumplidaCuesCreadas)
        datos += '};\n'
        cls._replace_all(file, "%ymax%", str(maxim))
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'razon_cues_creadas_respondidas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)

        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def razon_cues_arribadas_respondidas(cls, file, estadisticas):
        #
        nombreGrafico = '\\razon_cues_arribadas_respondidas.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_barra_simple(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Razon de cues arribadas respondidas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "$ \\frac{Cues arribadas}{ Tiempo en que se responden} $")
        maxim = 0
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, str(Decimal(sum([len(x) for x in e.cuesQueArriban.values()])) / Decimal(e.tiempoDemandaCumplidaCuesCreadas)))
            if Decimal(sum([len(x) for x in e.cuesQueArriban.values()])) / Decimal(e.tiempoDemandaCumplidaCuesCreadas) > maxim:
                maxim = Decimal(sum([len(x) for x in e.cuesQueArriban.values()])) / Decimal(e.tiempoDemandaCumplidaCuesCreadas)
        datos += '};\n'
        cls._replace_all(file, "%addplot%", datos)
        descrip = ''
        name = 'razon_cues_arribadas_respondidas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)
        cls._replace_all(file, "%ymax%", '{}'.format(maxim))
        cls._replace_all(file, "%ymin%", '0.0')
        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_espera_creadas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo espera promedio cues creadas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoEsperaConsultas.values())))
            if np.average(list(e.tiempoEsperaConsultas.values())) > max:
                max = np.average(list(e.tiempoEsperaConsultas.values()))
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'tiempo_espera_creadas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_servicio_creadas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo servicio promedio cues creadas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoServicioConsultas.values())))
            if np.average(list(e.tiempoServicioConsultas.values())) > max:
                max = np.average(list(e.tiempoServicioConsultas.values()))
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'tiempo_servicio_creadas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_respuesta_creadas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo respuesta promedio cues creadas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")

        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoRespuestaConsultas.values())))
            if np.average(list(e.tiempoRespuestaConsultas.values())) > max:
                max = np.average(list(e.tiempoRespuestaConsultas.values()))
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'tiempo_respuesta_creadas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_cues_creadas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)
        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')
        cls._replace_all(file, "%title%", "Tiempo de trabajo cues creadas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datos = '\\addplot coordinates {'
        for e in estadisticas:
            #tiempo espera
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoEsperaConsultas.values())))
        datos += '};\n'
        datos += '\\addplot coordinates {'
        for e in estadisticas:
            #tiempo servicio
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoServicioConsultas.values())))
        datos += '};\n'
        datos += '\\addplot coordinates {'
        for e in estadisticas:
            #tiempo respuesta
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoRespuestaConsultas.values())))
        datos += '};\n'
        cls._replace_all(file, "%addplot%", datos)
        cls._replace_all(file, "%legend%", "Tiempo de espera, Tiempo de respuesta, Tiempo de servicio")
        descrip = ''
        name = 'tiempo_cues_creadas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_servidor(cls, file, estadisticas):
        #
        nombreGrafico = '\\tiempo_servidor.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_barra_multiple(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)
        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo de respuesta del servidor")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datosTabla = ''
        datos = '\\addplot+[ybar] plot coordinates {'
        for e in estadisticas:
            #tiempo broadcast
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoBroadcastConsultas.values())))
            datosTabla += "{}   &   {}&{:.4f}&{:.4f}&{:.4f}\\\\ \n".format(e.tecnica, sum([len(x) for x in e.cuesQueArriban.values()]),np.average(list(e.tiempoBroadcastConsultas.values())),  np.average(list(e.latenciaCues.values())), np.average(list(e.tiempoServicioConsultasRecibidas.values())))
        datos += '};\n'
        datos += '\\addplot+[ybar] plot coordinates {'
        for e in estadisticas:
            # latencia
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.latenciaCues.values())))
        datos += '};\n'
        datos += '\\addplot+[ybar] plot coordinates {'
        for e in estadisticas:
            # tiempo respuesta
            datos += '({},{}) '.format(e.tecnica,  np.average(list(e.tiempoServicioConsultasRecibidas.values())) )
        datos += '};\n'

        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_tiempo_respuesta_servidor(datosTabla))
        cls._replace_all(file, "%addplot%", datos)
        cls._replace_all(file, "%legend%", "\strut Tiempo broadcast, \strut Tiempo procesamiento, \strut Tiempo Respuesta")
        descrip = ''
        name = 'tiempo_servidor:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_servidor_no_enviadas(cls, file, estadisticas):
        #
        nombreGrafico = '\\tiempo_servidor_no_enviadas.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_barra_simple(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo de respuesta de cues no enviadas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%precision%", "0")
        cls._replace_all(file, "%ylabel%", "$\overline{Tiempo respuesta}$")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        datosTabla = ''
        max = 0
        for e in estadisticas:
            datos += '({},{:.4f}) '.format(e.tecnica, np.average(list(e.tiempoBroadcastNoEnviadas.values())))
            if np.average(list(e.tiempoBroadcastNoEnviadas.values())) > max:
                max = np.average(list(e.tiempoBroadcastNoEnviadas.values()))
            datosTabla += '\n{}   &    {}&{}&{}\\\\'.format(e.tecnica, e.cuesTotalesCreadas,sum([len(x) for x in e.cuesQueArriban.values()]), e.cuesTotalesCreadas-sum([len(x) for x in e.cuesQueArriban.values()]))
        datos += '};\n'

        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_tiempo_respuesta_broadcast(datosTabla))
        cls._replace_all(file, "%addplot%", datos)

        max -= max % -100
        cls._replace_all(file, "%ymax%", '{}'.format(max))
        cls._replace_all(file, "%ymin%", '0.0')
        descrip = ''
        name = 'tiempo_broadcast_no_enviadas:'

        for e in estadisticas:
            descrip += "\n\\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)


    @classmethod
    def tiempo_servidor_total(cls, file, estadisticas):
        #e.tecnica, np.average(list(e.tiempoBroadcastNoEnviadas.values()) + list(e.tiempoEsperaConsultasRecibidas.values()))
        #
        nombreGrafico = '\\tiempo_respuesta_total.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_barra_simple(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo de respuesta total")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%precision%", "0")
        cls._replace_all(file, "%ylabel%", "$\overline{Tiempo respuesta}$")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoBroadcastNoEnviadas.values()) + list(e.tiempoEsperaConsultasRecibidas.values())))
            if np.average(list(e.tiempoBroadcastNoEnviadas.values()) + list(e.tiempoEsperaConsultasRecibidas.values())) > max:
                max = np.average(list(e.tiempoBroadcastNoEnviadas.values()) + list(e.tiempoEsperaConsultasRecibidas.values()))
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        cls._replace_all(file, "%ymin%", '0')
        descrip = ''
        name = 'tiempo_respuesta_total:'

        for e in estadisticas:
            descrip += " \n{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]\\\\".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)



    @classmethod
    def tiempo_espera_recibidas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo espera promedio cues recibidas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoEsperaConsultasRecibidas.values())))
            if np.average(list(e.tiempoEsperaConsultasRecibidas.values())) > max:
                max = np.average(list(e.tiempoEsperaConsultasRecibidas.values()))
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'tiempo_espera_recibidas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_servicio_recibidas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo servicio promedio cues recibidas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoServicioConsultasRecibidas.values())))
            if np.average(list(e.tiempoServicioConsultasRecibidas.values())) > max:
                max = np.average(list(e.tiempoServicioConsultasRecibidas.values()))
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'tiempo_servicio_recibidas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_respuesta_recibidas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Tiempo respuesta promedio cues recibidas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoRespuestaConsultasArribadas.values())))
            if np.average(list(e.tiempoRespuestaConsultasArribadas.values())) > max:
                max = np.average(list(e.tiempoRespuestaConsultasArribadas.values()))
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'tiempo_respuesta_recibidas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tiempo_cues_recibidas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)
        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')
        cls._replace_all(file, "%title%", "Tiempo de trabajo cues recibidas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Tiempo promedio")
        datos = '\\addplot coordinates {'
        for e in estadisticas:
            # tiempo espera
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoEsperaConsultasRecibidas.values())))
        datos += '};\n'
        datos += '\\addplot coordinates {'
        for e in estadisticas:
            # tiempo servicio
            datos += '({},{}) '.format(e.tecnica,  np.average(list(e.tiempoServicioConsultasRecibidas.values())))
        datos += '};\n'
        datos += '\\addplot coordinates {'
        for e in estadisticas:
            # tiempo respuesta
            datos += '({},{}) '.format(e.tecnica, np.average(list(e.tiempoRespuestaConsultasArribadas.values())))
        datos += '};\n'
        cls._replace_all(file, "%addplot%", datos)
        cls._replace_all(file, "%legend%", "Tiempo de espera, Tiempo de respuesta, Tiempo de servicio")
        descrip = ''
        name = 'tiempo_cues_recibidas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def cues_creadas_obsoletas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Cues creadas obsoletas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Numero de obsoletas")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, sum([len(x) for x in e.cuesObsoletasCreadas.values()]))
            if sum([len(x) for x in e.cuesObsoletasCreadas.values()]) > max:
                max = sum([len(x) for x in e.cuesObsoletasCreadas.values()])
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'cues_creadas_obsoletas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def cues_arribadas_obsoletas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Cues arribadas obsoletas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Numero de obsoletas")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, sum([len(x) for x in e.cuesObsoletasEnviadas.values()]))
            if sum([len(x) for x in e.cuesObsoletasEnviadas.values()]) > max:
                max = sum([len(x) for x in e.cuesObsoletasEnviadas.values()])
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'cues_arribadas_obsoletas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def cues_no_arribadas_obsoletas(cls, file, estadisticas):
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Cues no enviadas obsoletas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Numero de obsoletas")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, sum([len(x) for x in e.cuesObsoletasCreadas.values()])-sum([len(x) for x in e.cuesObsoletasEnviadas.values()]))
            if sum([len(x) for x in e.cuesObsoletasCreadas.values()]) - sum([len(x) for x in e.cuesObsoletasEnviadas.values()]) > max:
                max = sum([len(x) for x in e.cuesObsoletasCreadas.values()]) - sum([len(x) for x in e.cuesObsoletasEnviadas.values()])
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % -100
        cls._replace_all(file, "%ymax%", str(max))
        descrip = ''
        name = 'cues_no_arribadas_obsoletas:'
        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def obsolescencia(cls, file, estadisticas):
        #
        nombreGrafico = '\obsolescencia.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_barra_multiple(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)
        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')
        cls._replace_all(file, "%title%", "Cues obsoletas")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "Consultas obsoletas")
        datos = '\\addplot coordinates {'
        obsoletasServidor = []
        for e in estadisticas:
            #creadas
            datos += '({},{}) '.format(e.tecnica, sum([len(x) for x in e.cuesObsoletasCreadas.values()]))
            obsoletasServidor.append(sum([len(x) for x in e.cuesObsoletasCreadas.values()]))
        datos += '};\n'
        datos += '\\addplot coordinates {'
        obsoletasBroadcast = []
        for e in estadisticas:
            #cues arribadas
            datos += '({},{}) '.format(e.tecnica, sum([len(x) for x in e.cuesObsoletasEnviadas.values()]))
            obsoletasBroadcast.append(sum([len(x) for x in e.cuesObsoletasEnviadas.values()]))
        datos += '};\n'

        datosTabla = ''
        for i in range(0, len(estadisticas)):
            datosTabla += '{}  &  {}&{}\\\\ \n'.format(estadisticas[i].tecnica, obsoletasServidor[i], obsoletasBroadcast[i])

        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_obsolescencia(datosTabla))
        cls._replace_all(file, "%addplot%", datos)
        cls._replace_all(file, "%legend%", "CUEs del servidor, Consultas totales")
        descrip = ''
        name = 'obsolescencia:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def razon_de_rendimiento(cls, file, estadisticas):
        #
        nombreGrafico = '\\razon_rendimiento.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_barra_simple(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        simbolic = []
        for e in estadisticas:
            simbolic.append(e.tecnica)

        simbolic = '{}'.format(simbolic).replace('[', '')
        simbolic = '{}'.format(simbolic).replace(']', '')
        simbolic = '{}'.format(simbolic).replace('L', '')
        simbolic = '{}'.format(simbolic).replace("'", '')
        simbolic = '{}'.format(simbolic).replace('u', '')

        cls._replace_all(file, "%title%", "Razon de rendimiento")
        cls._replace_all(file, "%simbol%", simbolic)
        cls._replace_all(file, "%ylabel%", "$\\frac{Numero cues creadas}{tiempo ultima cue}$")
        datos = '\\addplot[ybar,fill=blue] coordinates {'
        max = 0
        for e in estadisticas:
            datos += '({},{}) '.format(e.tecnica, Decimal(e.cuesTotalesCreadas)/Decimal(e.tiempoEnQueSeRespondeLaUltimaCue))
            if Decimal(e.cuesTotalesCreadas)/Decimal(e.tiempoEnQueSeRespondeLaUltimaCue) > max:
                max = Decimal(e.cuesTotalesCreadas)/Decimal(e.tiempoEnQueSeRespondeLaUltimaCue)
        datos += '};\n'

        cls._replace_all(file, "%addplot%", datos)
        max -= max % - 100
        cls._replace_all(file, "%ymax%", '{}'.format(max))
        cls._replace_all(file, "%ymin%", '0.0')
        descrip = ''
        name = 'razon_de_rendimiento:'

        for e in estadisticas:
            descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def puntos_seleccion(cls, file, estadisticas, seleccion):

        if seleccion:
            #
            nombreGrafico = '\puntos_seleccion.tex'
            #
            archivoBase = GeneradorDeArchivosBase()
            archivoBase.generar_grafico_puntos(nombreGrafico, file)
            #
            file += nombreGrafico

            #
            tiempoMaximo = 0
            cuesMaximas = 0
            xtick = []
            for e in estadisticas:
                for key, values in e.elementosPorPrograma.items():
                    if int(str(key).split(':')[1]) > tiempoMaximo:
                        tiempoMaximo = int(str(key).split(':')[1])
                for key, puntos in e.valorSeleccion.items():
                    if puntos > cuesMaximas:
                        cuesMaximas = puntos

            # division en 5
            tiempoMaximo = int(tiempoMaximo)
            for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
                xtick.append(value)

            xtick = '{}'.format(xtick).replace('[', '')
            xtick = '{}'.format(xtick).replace(']', '')
            xtick = '{}'.format(xtick).replace('L', '')

            cls._replace_all(file, "%xmin%", "101")
            cls._replace_all(file, "%xmax%", str(tiempoMaximo))
            cls._replace_all(file, "%xtick%", xtick)
            cls._replace_all(file, "%xticklabels%", xtick)
            cls._replace_all(file, "%ymin%", "0")
            cls._replace_all(file, "%ymax%", str(cuesMaximas))
            cls._replace_all(file, "%xlabel%", "Tiempo de arribo")
            cls._replace_all(file, "%ylabel%", "Puntos")
            cls._replace_all(file, "%title%", "Puntos de seleccion de los programas")
            datos = ''
            for e in estadisticas:
                datos += '\\addplot coordinates{'
                for key, values in e.cuesQueArriban.items():
                    datos += '({},{})\n'.format(key, len(values))
                datos += '}; \\addlegendentry{' + str(e.tecnica) + '}; \n'
            cls._replace_all(file, "%addplot%", datos)

            descrip = ''
            name = 'cues_encubiertas_enviadas:'
            for e in estadisticas:
                descrip += "{} & [Usuarios = {}, K-anonimato = {}, POIs = {}, CUEs = {}, Repeticiones = {}, Talla = {} ]\\\\ \n".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
                name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas,  e.efectividad, e.talla)
            cls._replace_all(file, "%descrip%", descrip)

            cls._replace_all(file, "%name%", name)

    @classmethod
    def tabla_carga_trabajo(cls, file, estadisticas):
        #
        nombretabla = '\\tabla_carga_trabajo.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_tabla_cdt(nombretabla, file)
        #
        file += nombretabla

        #
        datos = ''
        for e in estadisticas:
            cuesArribadas = float(sum([len(x) for x in e.cuesQueArriban.values()]))
            tiempoRespuestaCuesArribadas = float(max(e.cuesQueArriban))
            totalCuesRespondidas = float(sum([len(x) for x in e.cuesCreadasRespondidas.values()]))
            tiempoRespuestaCuesCreadas = float(e.tiempoDemandaCumplidaCuesCreadas)
            datos += '\n{} &     {}&{}&{}&{:.4f}\\\\'.format(e.tecnica,int(totalCuesRespondidas), int(cuesArribadas), int(tiempoRespuestaCuesCreadas), float(totalCuesRespondidas)/float(cuesArribadas))
        cls._replace_all(file, "%datatable%", datos)
        ##########################
        descrip = ''
        name = 'tabla_carga_trabajo:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def tabla_tiempo_respuesta(cls, file, estadisticas):
        #
        nombretabla = '\\tabla_tiempo_respuesta.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_tabla_tdr(nombretabla, file)
        #
        file += nombretabla

        #
        datos = ''
        for e in estadisticas:
            totalCuesRespondidas = float(sum([len(x) for x in e.cuesCreadasRespondidas.values()]))
            cuesArribadas = (float(sum([len(x) for x in e.cuesQueArriban.values()])))/ totalCuesRespondidas
            cuesNoEnviadas = (e.cuesTotalesCreadas - sum([len(x) for x in e.cuesQueArriban.values()]))/totalCuesRespondidas

            tiempoRespuestaArribadas = cuesArribadas*np.average(list(e.tiempoBroadcastConsultas.values()))+np.average(list(e.latenciaCues.values()))+np.average(list(e.tiempoServicioConsultasRecibidas.values()))

            tiempoRespuestaNoEnviadas = cuesNoEnviadas*np.average(list(e.tiempoBroadcastNoEnviadas.values()))

            tiempoRespuestaTotal =tiempoRespuestaArribadas + tiempoRespuestaNoEnviadas
            datos += '\n{} &     {:.4f}&{:.4f}&{:.4f}\\\\'.format(e.tecnica, tiempoRespuestaTotal, tiempoRespuestaArribadas,tiempoRespuestaNoEnviadas)
        cls._replace_all(file, "%datatable%", datos)
        ##########################
        descrip = ''
        name = 'tabla_carga_trabajo:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(
                e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi,
                                                    e.cuesTotalesCreadas, e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def justicia_stetch(cls, file, estadisticas):
        #
        nombreGrafico = '\justicia_stetch.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        stretchMaximo = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.stretchPromedioPorPrograma.items():

                if int(str(key).split(':')[1]) > int(tiempoMaximo):
                    tiempoMaximo = str(key).split(':')[1]
                if values > stretchMaximo:
                    stretchMaximo = int(values)
        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)

        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')
        xtick = '{}'.format(xtick).replace("'", '')
        xtick = '{}'.format(xtick).replace('u', '')

        cls._replace_all(file, "%xmin%", "0")
        cls._replace_all(file, "%xmax%", "8750")
        cls._replace_all(file, "%xtick%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%xticklabels%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%ymax%", str(stretchMaximo))
        cls._replace_all(file, "%xlabel%", "Tiempo de difusion de cronograma")
        cls._replace_all(file, "%ylabel%", "Stretch")
        cls._replace_all(file, "%title%", "Stretch programas")
        datos = ''
        datosTabla = ''
        for e in estadisticas:
            datos += '\\addplot coordinates{'
            stretchAll = []
            for key, values in e.stretchPromedioPorPrograma.items():
                stretchAll.append(float(values))
                datos += '({},{})\n'.format(str(key).split(':')[1], values)
            datosTabla += '{}   &  {}&{}&{:.4f}\\\\ \n'.format(e.tecnica,max(stretchAll), min(stretchAll), np.average(stretchAll))
            datos += '}; \\addlegendentry{ ' + str(e.tecnica) + ' }; \n'

        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_justicia_stretch(datosTabla))
        cls._replace_all(file, "%addplot%", datos)
        cls._replace_all(file, "smooth" , "smooth,\n\t\t\t\tlegend style={at={(0.5,-0.25)},anchor=north,legend columns=-1},")
        descrip = ''
        name = 'justicia_stetch:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += " {}:{}:{}:{}:{}:{}:{} ".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi,
                                                    e.cuesTotalesCreadas, e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)

    @classmethod
    def justicia_jitter(cls, file, estadisticas):
        #
        nombreGrafico = '\justicia_jitter.tex'
        #
        archivoBase = GeneradorDeArchivosBase()
        archivoBase.generar_grafico_puntos(nombreGrafico, file)
        #
        file += nombreGrafico

        #
        tiempoMaximo = 0
        jitterMaximo = 0
        xtick = []
        for e in estadisticas:
            for key, values in e.jitterPromedioPorPrograma.items():

                if int(str(key).split(':')[1]) > int(tiempoMaximo):
                    tiempoMaximo = str(key).split(':')[1]
                if values > jitterMaximo:
                    jitterMaximo = int(values)
        # division en 5
        tiempoMaximo = int(tiempoMaximo)
        for value in range(tiempoMaximo / 5, tiempoMaximo + 1, tiempoMaximo / 5):
            xtick.append(value)

        xtick = '{}'.format(xtick).replace('[', '')
        xtick = '{}'.format(xtick).replace(']', '')
        xtick = '{}'.format(xtick).replace('L', '')
        xtick = '{}'.format(xtick).replace("'", '')
        xtick = '{}'.format(xtick).replace('u', '')

        cls._replace_all(file, "%xmin%", "0")
        cls._replace_all(file, "%xmax%", "8750")
        cls._replace_all(file, "%xtick%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%xticklabels%", "1250, 3750, 5000, 7500, 8750")
        cls._replace_all(file, "%ymin%", "0")
        cls._replace_all(file, "%ymax%", str(jitterMaximo))
        cls._replace_all(file, "%xlabel%", "Tiempo de difusion de cronograma")
        cls._replace_all(file, "%ylabel%", "Jitter")
        cls._replace_all(file, "%title%", "Jitter de programas")
        datos = ''
        datosTabla = ''
        for e in estadisticas:
            datos += '\\addplot coordinates{'
            jitterAll = []
            for key, values in e.jitterPromedioPorPrograma.items():
                jitterAll.append(float(values))
                datos += '({},{})\n'.format(str(key).split(':')[1], values)
            datosTabla += '{}   &  {}&{}&{:.4f}\\\\ \n'.format(e.tecnica,max(jitterAll), min(jitterAll), np.average(jitterAll))
            datos += '}; \\addlegendentry{ ' + str(e.tecnica) + ' }; \n'

        cls._replace_all(file, "\end{tikzpicture}", "\end{tikzpicture}\n"+ TablaDescriptiva.tabla_descriptiva_justicia_jitter(datosTabla))
        cls._replace_all(file, "%addplot%", datos)
        cls._replace_all(file, "smooth" , "smooth,\n\t\t\t\tlegend style={at={(0.5,-0.25)},anchor=north,legend columns=-1},")
        descrip = ''
        name = 'justicia_jitter:'
        for e in estadisticas:
            descrip += "\n \\\\{}->[Usuarios={}, K-anonimato={}, POIs={}, CUEs={}, Repeticiones={}, Talla={}]".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi, e.cuesTotalesCreadas, e.efectividad, e.talla)
            name += "{}:{}:{}:{}:{}:{}:{}".format(e.tecnica, e.numeroUsuarios, e.anonimato, e.numeroPoi,
                                                    e.cuesTotalesCreadas, e.efectividad, e.talla)
        cls._replace_all(file, "%descrip%", descrip)

        cls._replace_all(file, "%name%", name)