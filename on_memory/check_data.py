import re
import pandas as pd
def is_cedula(var,meta,*,key=None):
    var = str(var)
    pattern = meta.REGEX_PATTERNS[meta.CED]
    if key is None:
        if pd.isnull(var): return None
        if var.isalnum(): return None #it means it has not delimiter like v-5965 , it has no "-"
        char,num = re.split(r'[-._]+',var)
        if char=='V' or char=='E':
            if num.isdigit():
                if num[0]=='0':
                    num = re.search(pattern,num).group(1)
                return {meta.CED_CHAR:char,meta.CED:num}  #right reponse
    else:
        if var.isdigit(): return var
        else: 
            regex = re.search(pattern,var)
            return regex.group(1) if regex else None
    
        

        
        

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






        
    