from mymath import Mymath

math_inst = Mymath() 

print("Absolute of -150:", math_inst.absolute(-150)) 
print("Absolute of 259:", math_inst.absolute(259)) 

numbers = [5,10,15,20,25,1,2,4,5,1,2,3]
print("Average:", math_inst.average(numbers))
#error catch 
try:
    print(math_inst.average([]))
except ValueError as e:
    print(e)