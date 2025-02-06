class Car:
    def __init__(self,make,model,year):
        self._make = make
        self._model = model
        self._year = year
#get
    def get_make(self):
        return self._make
    def get_model(self):
        return self._model
    def get_year(self):
        return self._year
#set
    def set_make(self,n_make):
        self._make = n_make
    def set_model(self,n_model):
        self._model = n_model
    def set_year(self,n_year):
        #year first car was made
        if n_year>=1886:
            self._year = n_year
        else:
            raise ValueError("year entered must be 1886 and onwards\n")
    def display(self):
        return f"{self._year} {self._make} {self._model}"
