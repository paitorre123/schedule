class TablaDescriptiva(object):

    @classmethod
    def tabla_descriptiva_carga_trabajo_sistema(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{5}{|c|}{Datos (CDTsis)} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & Numero creadas &Total CUEs creadas& Promedio creadas & $T_{finalizacion}$   \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_carga_trabajo_servidor(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{5}{|c|}{Datos (CDTser)} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & Numero enviadas & Total CUEs enviadas & Promedio enviadas & $T_{finalizacion}$   \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_tiempo_respuesta_servidor(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{5}{|c|}{Datos (TDRser)} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & Numero enviadas & $T_{broadcast}$ & $T_{latencia}$ & $T_{transmision}$   \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_tiempo_respuesta_broadcast(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{4}{|c|}{Datos (TDRbro)} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & Numero creadas & Numero enviadas &Numero no enviadas \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_razon_utilidad(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{4}{|c|}{Datos (RDU)} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & $\overline{elementos \ encontrados}$ & $\overline{largo}$ &$\overline{utilidad}$ \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_razon_efectividad(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{4}{|c|}{Datos (RDE)} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & $\overline{elementos \ encontrados}$ & $\overline{elementos \ requeridos}$ &$\overline{efectividad}$ \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_justicia_stretch(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{4}{|c|}{Datos Stretch} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & Maximo stretch & Minimo stretch&$\overline{stretch}$ \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_justicia_jitter(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{4}{|c|}{Datos jitter} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & Maximo jitter & Minimo jitter&$\overline{jitter}$ \\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla

    @classmethod
    def tabla_descriptiva_obsolescencia(cls, datos):
        datostabla = '%----------------------------------------------------------------\n'
        datostabla += '\\begin{tabular}{ |c|c|c|}\n' \
                      '\hline\n' \
                      '\multicolumn{3}{|c|}{Datos obsolescencia} \\\\ \n' \
                      '\hline\n' \
                      '\hline\n' \
                      'Tecnica  & Obsoletas en el servidor & Obsoletas en el broadcast\\\\ \n' \
                      '\hline \n'
        datostabla += datos
        datostabla += '\hline\n' \
                      '\end{tabular}\n' \
                      '%----------------------------------------------------------------'
        return datostabla
