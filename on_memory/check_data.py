import re
import pandas as pd
def is_cedula(var,meta,*,key=None):
    var = str(var)
    pattern = meta.REGEX_PATTERNS[meta.CED]
    if key is None:
        if pd.isnull(var): return None
        if var.isalnum(): return None #it means it has not delimiter like v-5965 , it has no "-"

        try: char,num = re.split(r'[-._]+',var)
        except ValueError as e:
            pass
            #print(var,e)

        else:
            if char=='V' or char=='E':
                if num.isdigit():
                    if num[0]=='0':
                        num = re.search(pattern,num).group(1)
                    return {meta.CED_CHAR:char,meta.CED:num}  #right reponse
    else:
        if var.isdigit(): return var
        else: 
            regex = re.search(pattern,var)
            return regex.group(1) or None
    
        

        
        

def is_name(var,meta):
    var = str(var)
    pattern = meta.REGEX_PATTERNS[meta.NAME]
    regex = re.search(pattern,var)
    return var if regex else None

def is_acc(*,acc_1,acc_2,meta):
    if pd.isnull(acc_1): return None
    acc_1 = str(acc_1)
    acc_2 = None if pd.isnull(acc_2) else str(acc_2)

    pattern = meta.REGEX_PATTERNS[meta.ACC1]

    matches_acc1 = pattern.search(acc_1)
  
    if not matches_acc1: return None
    elif matches_acc1.groupdict().get('acc2') is not None:  #then acc_1 contains the whole value 0114-0152-09-1521233610 
        return {meta.ACC1:matches_acc1.groupdict().get('acc1'),meta.ACC2:matches_acc1.groupdict().get('acc2')}

    elif acc_2 is not None: #it means that acc_1 is right and the acc2 must contain values  0114-0152-09   | 1521233610
        return {meta.ACC1:acc_1,meta.ACC2:acc_2}

    return None

def is_mov(var,meta):
    var = str(var)
    
    if pd.isnull(var): return None
    pattern = meta.REGEX_PATTERNS[meta.MOV]
    regex = pattern.search(var)
    if regex:
        mov = regex.groupdict()
        if mov['point'] == ',': mov['point']='.'
        if not mov.get('point'):
            if len(mov.get('significant'))>3:
            
                return float(mov['significant'])/100    
            else: return None
        elif  mov.get('decimal'):
            if len(mov.get('decimal'))<2:
           
                return  format(float(''.join(mov.values())),'.2f')
            else : return round(float(''.join(mov.values())),2)

def get_date(meta,*,file_name,key):
    date = meta.REGEX_PATTERNS[key].search(file_name).groupdict()
    
    if not date: return date 
    elif key==meta.EMP:
        r = range(1,13) #from 1 to 12   
        if int(date['month']) in r: return ''.join(date.values())   
        else: raise ValueError(f'date of {file_name} is wrong not in bounds 1-12 ')
    elif key==meta.OBR:
     
        r = range(1,53)
        if int(date['sem']) in r : return ''.join(date.values())  
        else: raise ValueError(f'date of {file_name} is wrong not in bound 1-52')

def get_date_keyword(meta,key):
    return 'quin_' if key==meta.EMP else 'sem_'
def get_table_name(meta,key,mov_type):
    mov_string = 'aportes' if mov_type==meta.APOR else 'deducciones'
    key_string = 'obreros_'if key==meta.OBR else 'empleados_'
    return key_string + mov_string





        
    