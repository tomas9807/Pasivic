

from database import read as database_read,write as database_write
from on_memory import check_data,print_files,read_files
import sqlite3

def setup_socios(path,meta):  
    df = read_files.read(path)
    
    conn = database_read.connect()
    with conn:
        cur = conn.cursor()
        table_name = 'socios'
        cur.execute(
            """
            create table if not exists socios(
            id integer primary key,
            nombre text,
            tipo_cedula text,
            numero_cedula text unique,
            cuenta text,
            es_obrero integer default 0,
            es_empleado integer default 0
            )
            """
            )
        simple = database_write.Simple(cur)
        
        patterns = meta.DEFAULT_PATTERNS[meta.SOC]
        pname = patterns[meta.NAME]
        pcedula = patterns[meta.CED]
        pacc_1 = patterns[meta.ACC1]
        pacc_2 = patterns[meta.ACC2]
        for row in df.itertuples():
            
            name = check_data.is_name(row[pname],meta)
            cedula = check_data.is_cedula(row[pcedula],meta)

            acc_1 = row[pacc_1]
            acc_2 = row[pacc_2]
            acc= check_data.is_acc(acc_1=acc_1,acc_2=acc_2,meta=meta)
            
            if name and cedula and acc:
                try:
                    simple.insert(
                        table=table_name,
                        nombre=name,
                        tipo_cedula=cedula[meta.CED_CHAR],
                        numero_cedula=cedula[meta.CED],
                        cuenta=''.join(list(acc.values()))
                    )
                except sqlite3.Error as e:
                    print('ha ocurrido un error al insertar un socio en base de datos :',e)

        
def setup_empleados_and_socios(path,meta,*,key):
    df = read_files.read(path)
    conn = database_read.connect()
    with conn:
        cur = conn.cursor()
        pattern = meta.DEFAULT_PATTERNS[key][meta.CED]
        simple = database_write.Simple(cur)
        table='socios'
        col='es_obrero' if key==meta.OBR else 'es_empleado'
        new_var = 1
        where_var = 'numero_cedula'
        ced_col = df.iloc[:]

            cedula = check_data.is_cedula(row[pattern],meta,key=key)
            if cedula:
                try:
                    simple.update_where(
                        table=table,
                        col=col,
                        new_var=new_var,
                        where_var=where_var,
                        is_var=cedula
                    )
                except sqlite3.Error as e:
                    print('ha ocurrido un error al insertar un socio en base de datos :',e)

def read_movs(list_of_files):
    for file in list_of_files:
        try:
            df = read_files.read(file)
        except ValueError as e:
            print(e)
        else:
            for row in df.itertuples():








    








        




    


    
def read_socios_mov(path): pass

def read_socios_obr(path): pass

