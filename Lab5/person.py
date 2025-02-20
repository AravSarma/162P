class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def get_name(self):
        return self._name
    def set_name(self,value):
        self._name = value
    def get_age(self):
        return self._age
    def set_age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cant be negative")
