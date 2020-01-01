import shutil

class GeneradorDeArchivosBase(object):
    def __init__(self):
        self.url = 'D:\Usuarios\PABLO\Proyectos\Python\workspaces-2019-1\schedule\src\manejoDeDatos'
        self.grafico = ['\\baseGraficoBarrasSimple.txt',
                        '\\baseGraficoBarraMultiple.txt',
                        '\\baseGraficoPuntos.txt',
                        '\\baseTablaCDT.txt',
                        '\\baseTablaTDR.txt']


    def generar_grafico_barra_simple(self, name, location):
        shutil.copy(self.url + self.grafico[0], location + name)

    def generar_grafico_barra_multiple(self, name, location):
        shutil.copy(self.url + self.grafico[1], location + name)

    def generar_grafico_puntos(self, name, location):
        shutil.copy(self.url + self.grafico[2], location + name)

    def generar_tabla_cdt(self, name, location):
        shutil.copy(self.url + self.grafico[3], location + name)

    def generar_tabla_tdr(self, name, location):
        shutil.copy(self.url + self.grafico[4], location + name)
