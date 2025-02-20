class ReverseFloat:
    def __init__(self, value):
        self.value = float(value)
    
    def __str__(self):
        return "%.2f" % self.value
    
    def __add__(self, other):
        if isinstance(other, ReverseFloat):
            return ReverseFloat(self.value - other.value)
        return ReverseFloat(self.value - other)
    
    def __sub__(self, other):
        if isinstance(other, ReverseFloat):
            return ReverseFloat(self.value + other.value)
        return ReverseFloat(self.value + other)
    
    def __mul__(self, other):
        if isinstance(other, ReverseFloat):
            return ReverseFloat(self.value / other.value)
        return ReverseFloat(self.value / other)
    
    def __truediv__(self, other):
        if isinstance(other, ReverseFloat):
            return ReverseFloat(self.value * other.value)
        return ReverseFloat(self.value * other)

''''The class should take a single number as input.  You will need to create the following overloaded methods:

__init__(self, value) – Sets the internal value
__str__(self) – Returns a string of the value with 2 digits after the decimal (ie. “%.2f”)
__add__(self, other) – Returns a new ReverseFloat with the value of other subtracted from self
__sub__(self, other) – Returns a new ReverseFloat with the value of other added to self
__mul__(self, other) – Returns a new ReverseFloat with the value of self divided by other
__truediv__(self, other) – Returns a new ReverseFloat with the value of self multiplied by other
'''