from database import read as database_read 
from on_memory import check_data,print_files,read_files
import sqlite3
import os
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
            tipo_cedula text not null,
            numero_cedula text unique not null,
            cuenta text,
            es_obrero integer default 0,
            es_empleado integer default 0
            )
            """
            )

        
        patterns = meta.DEFAULT_PATTERNS[meta.SOC]
        patterns = [patterns[meta.NAME],patterns[meta.CED],patterns[meta.ACC1], patterns[meta.ACC2]]
   
   
        for name,cedula,acc_1,acc_2 in df.iloc[:,patterns].values:
            
            name = check_data.is_name(name,meta)
            cedula = check_data.is_cedula(cedula,meta)

            acc= check_data.is_acc(acc_1=acc_1,acc_2=acc_2,meta=meta)
          
            if name and cedula and acc:
                try:
                    cur.execute(f"""
                    insert into {table_name}(nombre,tipo_cedula,numero_cedula,cuenta)
                    values(?,?,?,?)
                    
                    """,(name,cedula[meta.CED_CHAR],cedula[meta.CED],''.join(list(acc.values())) ))
                   
                except sqlite3.Error as e:
                    print('ha ocurrido un error al insertar un socio en base de datos :',e)

        
def setup_empleados_and_socios(path,meta,*,key):
    df = read_files.read(path)
    conn = database_read.connect()
    with conn:
        cur = conn.cursor()
        pattern = meta.DEFAULT_PATTERNS[key][meta.CED]
     
        table='socios'
        col='es_obrero' if key==meta.OBR else 'es_empleado'
        new_var = 1
        where_var = 'numero_cedula'
        ced_col = df.iloc[:,pattern]
        for cedula in ced_col.values:
            cedula = check_data.is_cedula(cedula,meta,key=key)
  
            if cedula:
                try:
                    cur.execute(f"""
                           update {table}
                           set {col}=?
                           where {where_var}=?

                           """,(new_var,cedula))
                 
                except sqlite3.Error as e:
                    print('ha ocurrido un error al insertar un socio en base de datos :',e)

def read_movs(meta,*,list_of_files,mov_type,key):
    conn = database_read.connect()
    with conn:
        cur = conn.cursor()
        #obrero or empleado
        keyword = check_data.get_date_keyword(meta,key)
        table_name =  check_data.get_table_name(meta,key,mov_type)
      
        dates_columns = meta.get_date_column_names(key=key,word=keyword)
 
        cur.execute(
            f"""
            create table if not exists {table_name}(
            id integer primary key,
            socio_id integer unique not null,
            {''.join(date+' real,' for date in dates_columns)}
            foreign key (socio_id) references socios(id) ON DELETE CASCADE
            )
            """
            )
        patterns = meta.DEFAULT_PATTERNS[meta.MOV]
        patterns = [patterns[meta.CED],patterns[mov_type]]
       
        for file in list_of_files:
            try:
                df = read_files.read(file)
            except ValueError as e:
                raise e
            else:
                date = check_data.get_date(meta,file_name=os.path.basename(file),key=key)
                try:
                    if date:

                        
                        
                
                        for idx,values in enumerate(df.iloc[:,patterns].values):
                            cedula,mov = values
                            cedula = check_data.is_cedula(cedula,meta,key=mov_type)
                            mov = check_data.is_mov(mov,meta)
                            try:
                                if cedula and mov:
                                    data = cur.execute('select id from socios where numero_cedula=?',(cedula,)).fetchone()
                                    if data:
                                        socio_id = data[0]
                                        date = keyword + date
                                    
                                        if cur.execute(f'select socio_id from {table_name} where socio_id=?',(socio_id,)).fetchone():
                                            #the socio_id has already been created in the database so update its row
                                            cur.execute(f"""
                                                update {table_name}
                                                set {date}=?
                                                where socio_id=?

                                                """,(mov,socio_id))

                                        else: 
                                            cur.execute(f"""
                                                insert into {table_name}(socio_id,{date})
                                                values(?,?)

                                                """,(socio_id,mov))
                                else: 
                                    
                                    raise ValueError(f'something went wrong in {file} , LINE {idx+1}. Could not read { "cedula," if not cedula else "" } {"mov," if not mov else ""}. \n')
                            except ValueError as e:
                                #print(e)
                                pass
                except Exception as e:
                    print(e)        