


def test(key): 
    print('the input key is:',key)   
    else:
        month = ['15','30']
        for i in range(1,53):
            if i==4: 
                yield '2904'
            else:
                str_i = str(i)
                if i<10:
                    str_i= '0'+str_i 
                yield month[0] + str_i if i % 2 else month[1] + str_i

my_list = list(test(1))
print('the list is :' ,my_list)
