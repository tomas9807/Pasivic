import re
from collections import Counter
class EasyManipulation():
    KEYS = Counter()
    
    def set_default_patterns(self):
    
        self.DEFAULT_PATTERNS = {
        self.SOC:{self.NAME:2,self.CED:4,self.ACC1:6,self.ACC2:7},
        self.EMP:{self.CED:3,},
        self.OBR:{self.CED:1,},
        self.MOV:{self.CED:1,self.APOR:3,self.DEDUC:3}
    }

    def set_regex_patterns(self):
        self.REGEX_PATTERNS = {
            self.CED:re.compile(r'0*([1-9][0-9]*)'),
            self.NAME:re.compile(r'([a-zA-z]+)'),
            self.ACC1:re.compile(r'(?P<acc1>[0-9]{4}-[0-9]{4}-[0-9]{2})(?P<acc2>-\d+)?')
            self.MOV:re.compile(r'0*(?P<significant>[1-9][0-9]*)(?P<point>[.,])?(?P<decimal>[0-9]){0,2}')
        }
        
    def __init__(self):
        keys = EasyManipulation.KEYS
        self.SOC = keys['socios']
        self.OBR = keys['obrero']
        self.EMP = keys['empleado']
        self.CED = keys['cedula']
        self.NAME =  keys['name']
        self.ACC1 = keys['first_acc']
        self.ACC2 = keys['second_acc']
        self.CED_CHAR =  keys['cedula_char'] 
        self.APOR = keys['aporte']
        self.DEDUC = keys['deduccion']
        self.MOV = keys['movimiento']

        #itertuples always return index for tuples so start counting by 1 as 0 is index
        self.set_default_patterns()
        self.set_regex_patterns()
        
    @classmethod 
    def get_key_by_val(cls,val):
        for key,value in cls.KEYS.items():
            if key==value:
                return key

    @classmethod
    def pretty_print(cls,dict):
        return {cls.get_key_by_val(value):value for key,value in dict.items()}


