
class Instruction:
    """Simple instructions representative of a RISC machine

    These instructions are mostly immutable -- once constructed,
    they will not be changed -- only displayed and executed
    """
    def __init__(self,t):      # default constructor
        self._temp = t          # every instruction has a register
    def get_temp(self):         #     which holds its answer
        return self._temp

class Print(Instruction):
    """A simple non-RISC output function to display a value"""
    def __str__(self):
        return "print T" + str(self._temp)
    def execute(self,temps,stack,pc,sp):
        print( temps[self._temp] )

class Initialize(Instruction):
    """Variable assignment"""
    def __init__(self,t,v):
        super().__init__(t)     #Replace with get_item
        self._value = v
    def __str__(self):
        return "T" + str(self._temp) + " = " + str(self._value)
    def execute(self,temps,stack,pc,sp):
        temps[self._temp] = self._value

class Load(Instruction):
    """Stack lookup and variable (register) assignment"""
    def __init__(self,t,i):
        super().__init__(t)
        self._index = i
    def __str__(self):
        return "T" + str(self._temp) + " = stack[" + str(self._index) + "]"
    def execute(self,temps,stack,pc,sp):
        temps[self._temp] = stack[self._index]

class Store(Instruction):
    """Stack assignment and variable(register) lookup"""
    def __init__(self,t,p):
        super().__init__(t)
        self._pos = p
    def __str__(self):
        return "stack[" + str(self._pos) + "]" + " = T" + str(self._temp)
    def execute(self,temps,stack,pc,sp):
        stack[self._pos] = temps[self._temp]
        
class Compute(Instruction):
    """Use eval()"""
    def __init__(self,t,tl,op,tr):
        super().__init__(t)
        self._temp_left = tl
        self._operator = op
        self._temp_right = tr
    def __str__(self):
        return "T" + str(self._temp) + " = (T" + str(self._temp_left)  + str(self._operator)  + "T" + str(self._temp_right) + ")"
    def execute(self,temps,stack,pc,sp):
        temps[self._temp] = eval(str(temps[self._temp_left]) + str(self._operator) + str(temps[self._temp_right]))
