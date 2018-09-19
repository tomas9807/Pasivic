import re

class EasyManipulation():
 
    def set_default_patterns(self):
    
        self.DEFAULT_PATTERNS = {
        self.SOC:{self.NAME:1,self.CED:3,self.ACC1:5,self.ACC2:6},
        self.EMP:{self.CED:2,},
        self.OBR:{self.CED:0,},
        self.MOV:{self.CED:0,self.APOR:2,self.DEDUC:2}
    }

    def set_regex_patterns(self):
        self.REGEX_PATTERNS = {
            self.CED:re.compile(r'0*([1-9][0-9]*)'),
            self.NAME:re.compile(r'([a-zA-z]+)'),
            self.ACC1:re.compile(r'(?P<acc1>[0-9]{4}-[0-9]{4}-[0-9]{2})(?P<acc2>-\d+)?'),
            self.MOV:re.compile(r'0*(?P<significant>[1-9][0-9]*)(?P<point>[.,])?(?P<decimal>[0-9]){0,2}'),
            self.EMP:re.compile(r'(?P<day>15|30|28|29)-?(?P<month>[0-9]{1,2})'),
            self.OBR:re.compile(r'0*(?P<significant>[1-9][0-9]*)(?P<point>[.,])?(?P<decimal>[0-9]){0,2}')
        }
        
    def __init__(self):
   
        self.SOC = 0
        self.OBR = 1
        self.EMP = 2
        self.CED = 3
        self.NAME =  4
        self.ACC1 = 5
        self.ACC2 = 6
        self.CED_CHAR =  7
        self.APOR = 8
        self.DEDUC = 9
        self.MOV = 10
        
        #itertuples always return index for tuples so start counting by 1 as 0 is index
        self.set_default_patterns()
        self.set_regex_patterns()
        



