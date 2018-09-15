import pandas as pd
import matplotlib.pyplot as ptl
import numpy as np
import subprocess 
import os

    
def read(path):

    if path.lower().endswith(('xls','xlsx')):
        df = pd.read_excel(path,header=None,)
        
    elif path.lower().endswith('csv'):
        df = pd.read_csv(path)
    
        
    else:
        if os.name== 'posix':
           
            proc = subprocess.run(f'file --mime "{os.path.basename(path)}"', shell=True,stdout=subprocess.PIPE)
            raise ValueError(f'the file is -> {proc.stdout}')

    if df.empty: raise ValueError()   
    return df
               

        
       
 
    
