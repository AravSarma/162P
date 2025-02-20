from reversemath import ReverseFloat

def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    "Call rev floar method from rev math "
    rf1 = ReverseFloat(num1)
    rf2 = ReverseFloat(num2)
    print(f"{num1} + {num2} = {rf1 + rf2}")
    print(f"{num1} - {num2} = {rf1 - rf2}")
    print(f"{num1} * {num2} = {rf1 * rf2}")
    print(f"{num1} / {num2} = {rf1 / rf2}")

if __name__ == "__main__":
    main()

"""Create a file called lab5a.py that takes 2 
command line arguments, converts them to floats
, then uses them to create instances of the ReverseFloat class
.  It should then test all of the operators and methods.  
It should print out the results.  
Example output line from the multiplication:"""