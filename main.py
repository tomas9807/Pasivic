import setup
import timeit
import os
from configuration import get_meta

def init():



    meta = get_meta.EasyManipulation()
    setup.setup_socios('socios.xls',meta)
    setup.setup_empleados_and_socios('SOCIOS OBREROS.xlsx',meta,key=meta.OBR)
    setup.setup_empleados_and_socios('SOCIOS EMPLEADOS.xlsx',meta,key=meta.EMP)
    

    setup.read_movs(meta,list_of_files=('01 Aporte PASIVIC 15-01-2016.csv',),mov_type=meta.APOR,key=meta.EMP)

if __name__=='__main__':
    init()

