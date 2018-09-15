import re

class EasyManipulation():
    KEYS = {
        'socios':1,
        'obrero':2,
        'empleado':3,
        'cedula':4,
        'name':5,
        'first_acc':6,
        'second_acc':7,
        'cedula_char':8,
        
        }
    def set_default_patterns(self):
    
        self.DEFAULT_PATTERNS = {
        self.SOC:{self.NAME:2,self.CED:4,self.ACC1:6,self.ACC2:7},
        self.EMP:{self.CED:3},
        self.OBR:{self.CED:1},
    }

    def set_regex_patterns(self):
        self.REGEX_PATTERNS = {
            self.CED:re.compile(r'0*([1-9][0-9]*)'),
            self.NAME:re.compile(r'([a-zA-z]+)'),
            self.ACC1:re.compile(r'(?P<acc1>[0-9]{4}-[0-9]{4}-[0-9]{2})(?P<acc2>-\d+)?')
        }
        
    def __init__(self):
        pointer_keys = EasyManipulation.KEYS
        self.SOC = pointer_keys['socios']
        self.OBR = pointer_keys['obrero']
        self.EMP = pointer_keys['empleado']
        self.CED = pointer_keys['cedula']
        self.NAME =  pointer_keys['name']
        self.ACC1 = pointer_keys['first_acc']
        self.ACC2 = pointer_keys['second_acc']
        self.CED_CHAR =  pointer_keys['cedula_char'] 
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


