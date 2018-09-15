

class Simple():

   


    def __init__(self,cursor):
        self.cur = cursor
        self.insert_query = None

    def insert(self,*,table=None,**kwargs):
        if self.insert_query is None:
  
            which_values = ','.join(list(kwargs.keys()))
            interrogations = ','.join('?' for key in kwargs)
            self.insert_query = f'insert into {table} ({which_values}) values ({interrogations})'
        
        self.cur.execute(self.insert_query,list(kwargs.values()))

   

    def update(self,*,table,col,new_var):
        self.cur.execute(f'update {table}  set {col} = {new_var}')

    def update_where(self,*,table,col,new_var,where_var,is_var):
        self.cur.execute(f'update {table}  set {col} = {new_var} where {where_var} is {is_var}')





