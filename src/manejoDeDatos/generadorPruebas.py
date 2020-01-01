


class GeneradorDePruebas(object):
    def __init__(self):
        self.pruebas = ['Grafico.cues_encubiertas_enviadas',
                    #'Grafico.cues_que_arriban_demanda_total',
                    #'Grafico.razon_cues_arribadas_sobre_tiempo',
                    'Grafico.cues_creadas',
                    'Grafico.razon_de_arribo',
                    'Grafico.razon_de_rendimiento',
                    'Grafico.cues_creadas_respondidas',
                    'Grafico.cues_recibidas_respondidas',
                    'Grafico.razon_utilidad',
                    'Grafico.razon_efectividad',
                    #'Grafico.razon_cues_creadas_respondidas',
                    'Grafico.razon_cues_arribadas_respondidas',
                    #'Grafico.tiempo_espera_creadas',
                    #'Grafico.tiempo_respuesta_creadas',
                    #'Grafico.tiempo_servicio_creadas',
                    #'Grafico.tiempo_espera_recibidas',
                    #'Grafico.tiempo_respuesta_recibidas',
                    #'Grafico.tiempo_servicio_recibidas',
                    #'Grafico.tiempo_cues_creadas',
                    #'Grafico.tiempo_cues_recibidas',
                    'Grafico.tiempo_servidor',
                    'Grafico.tiempo_servidor_no_enviadas',
                    'Grafico.tiempo_servidor_total',
                    #'Grafico.cues_creadas_obsoletas',
                    #'Grafico.cues_arribadas_obsoletas',
                    #'Grafico.cues_no_arribadas_obsoletas',
                    'Grafico.obsolescencia',
                        'Grafico.puntos_seleccion']
        self.direcciones = ["D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\carga-trabajo\cues_que_arriban.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\carga-trabajo\cues_que_arriba_total.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\carga-trabajo\\\\razon_carga_trabajo.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\carga-trabajo\cues_creadas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\carga-trabajo\\\\razon_de_arribo.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\carga-trabajo\\\\razon_rendimiento.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\utilidad\cues_respondidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\utilidad\cues_recibidas_respondidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\utilidad\\\\razon_de_utilidad.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\utilidad\\\\razon_de_efectividad.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\utilidad\\\\razon_cues_creadas_respondidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\utilidad\\\\razon_cues_arribadas_respondidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_espera_creadas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_respuesta_creadas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_servicio_creadas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_espera_recibidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_respuesta_recibidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_servicio_recibidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_cues_creadas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_cues_recibidas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_servidor.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_servidor_no_enviadas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\\\\tiempo\\\\tiempo_servidor_total.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\obsolescencia\cues_creadas_obsoletas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\obsolescencia\cues_arribadas_obsoletas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\obsolescencia\cues_no_enviadas_obsoletas.tex",
                        "D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%\obsolescencia\obsolescencia.tex"]
        self.direccion = 'D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\graficos\%carpeta%'

    def generar(self):
        print 'Estadisticas.URL_EXCEL = "{}"'.format('D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\[K=4-R=3-T=100]\[AlgoritmoDeEnvergaduraProbabilista][Stretch][USER=200][POI=1600][k=4].xlsx')
        print 'e1 = Estadisticas(1600, 200, 4, "AED-ASS")'.format()
        print 'Estadisticas.URL_EXCEL = "{}"'.format('D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\[K=4-R=3-T=100]\[AlgoritmoDeEnvergaduraProbabilista][Stretch][USER=200][POI=1600][k=4].xlsx')
        print 'e2 = Estadisticas(1600, 200, 4, "AED-ASS")'.format()
        print 'Estadisticas.URL_EXCEL = "{}"'.format('D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\[K=4-R=3-T=100]\[AlgoritmoRelevanciaProbabilista][Stretch][USER=200][POI=1600][k=4].xlsx')
        print 'e3 = Estadisticas(1600, 200, 4, "AED-ASS")'.format()
        print 'Estadisticas.URL_EXCEL = "{}"'.format('D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos\[K=4-R=3-T=100]\[AlgoritmoDeEnvergaduraProbabilista][CargaDeTrabajo][USER=500][POI=1600][k=4].xlsx')
        print 'e4 = Estadisticas(1600, 500, 4, "AED-ASS")'.format()
        #print 'datos = [e1, e2, e3]'
        print 'datos = [e1, e2, e3, e4]'
        for i in range(0, len(self.pruebas)):
            print '{}("{}", datos)'.format(self.pruebas[i], self.direccion.replace("%carpeta%", "datos-6"))


if __name__ == '__main__':
    GeneradorDePruebas().generar()