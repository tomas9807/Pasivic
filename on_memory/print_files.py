

def add_zeros_tostring(string,*,how_many,to_left=True):
    list_of_zeros = ['0' for i in range(how_many)]
    string_of_zeros = ''.join(list_of_zeros)
    return string +  string_of_zeros if to_left else string_of_zeros + string



def print_format60(meta*,path,key):
    with open(path,mode='w') as f:
        





