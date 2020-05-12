from src.manejoDeDatos.grafico import Grafico
import os

if __name__ == '__main__':
    url = 'C:/Users/pablo/Study/Tesis/graficos/datos-{}'
    files = [
             #'/carga_trabajo_servidor.tex',
             #'/carga_trabajo_sistema.tex',
             #'/cues_creadas.tex',
             #'/cues_enviadas_servidor.tex',
             #'/justicia_jitter.tex',
             #'/justicia_stetch.tex',
             #'/obsolescencia.tex',
             #'/razon_cues_arribadas_respondidas.tex',
             #'/razon_efectividad.tex',
             #'/razon_privacidad.tex',
             #'/razon_rendimiento.tex',
             #'/razon_utilidad.tex',
             #'/tabla_carga_trabajo.tex',
             #'/tiempo_respuesta_total.tex',
             #'/tiempo_servidor.tex',
             '/tiempo_servidor_no_enviadas.tex'
             ]
    #for i in range(1,239):
        #for file in files:
           #Grafico._replace_all(url.format(i)+file, '[!ht]', '[H]')
            #Grafico._replace_all(url.format(i) + file, '[ht]', '[H]')

    for i in range(1, 239):
        for file in files:
            dataLog = []
            with open(url.format(i)+file, 'rt') as f:
                data = f.readlines()
            for line in data:
                if line.__contains__('Tecnica  & Numero creadas & Numero enviadas &Numero no enviadas \\ '):
                    #print(line)
                    dataLog.append(line)
            #print str(dataLog[0]).replace('razon_de_arribo', 'razon_privacidad')
            #log = "legend style={at={(0.5,-0.25)},anchor=north,legend columns=-1},"
            #os.system('pause')
            Grafico._replace_all(url.format(i)+file, dataLog[0], "Técnica  & Número creadas & Número enviadas &Número no enviadas \\\\  \n")
