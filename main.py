import setup
import timeit
import os
from configuration import get_meta


def get_right_path(path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__),path))


def get_list_files(folder):
    if os.path.isdir(folder):
        return (os.path.join(folder,file) for file in os.listdir(folder))




def init():



    meta = get_meta.EasyManipulation()
    # setup.setup_socios('socios.xls',meta)
    # setup.setup_empleados_and_socios('SOCIOS OBREROS.xlsx',meta,key=meta.OBR)
    # setup.setup_empleados_and_socios('SOCIOS EMPLEADOS.xlsx',meta,key=meta.EMP)

    # empleados_aportes = get_list_files(get_right_path('EMPLEADOS 2016 OK/APORTES 2016'))
    # empleados_deducciones = get_list_files(get_right_path('EMPLEADOS 2016 OK/DEDUCCIONES 2016'))
    # obreros_aportes = get_list_files(get_right_path('OBREROS 2016 OK/APORTES OK'))
    # obreros_decciones = get_list_files(get_right_path('OBREROS 2016 OK/DEDUCCIONES OK'))

    # setup.read_movs(meta,list_of_files=empleados_aportes,mov_type=meta.APOR,key=meta.EMP)
    # setup.read_movs(meta,list_of_files=empleados_deducciones,mov_type=meta.DEDUC,key=meta.EMP)
    # setup.read_movs(meta,list_of_files=obreros_aportes,mov_type=meta.APOR,key=meta.OBR)
    # setup.read_movs(meta,list_of_files=obreros_decciones,mov_type=meta.DEDUC,key=meta.OBR)
    

if __name__=='__main__':
    init()

