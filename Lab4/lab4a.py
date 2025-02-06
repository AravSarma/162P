from car import Car 
'''Write a program called lab4a.py that 
imports the class you created and creates multiple
 instances of class objects.  
 Make sure your program displays some information from 
 the class to show that you know how to access
 private instance attributes using the properties.'''

car1 = Car("Audi", "RS6", 2020)
car2 = Car("BMW", "M4", 2018)

#print b4 modification 
print(car1.display())  
print(car2.display()) 
print("\nafter change\n")
#modify
car1.set_year(2025)
car2.set_make("Mercedes")
car2.set_model("C63 AMG")
#display
print(car1.display())  
print(car2.display()) 

#error catch 
try:
    car2.set_year(1810)
except ValueError as e:
    print(e)