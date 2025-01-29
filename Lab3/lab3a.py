def factorial1(n):
    result  = 1 
    for i in range(1,n+1):
        result *=i 
    return result
def factorial2(n):
    if n ==0 or n==1:
        return 1 
    return n*factorial2(n-1)

print("Choose  factorial 1 or 2, iterative or recursive")
iterative = input().strip().lower()

print("Enter a number:")
number = int(input())

if iterative == "iterative":
    print("Factorial:", factorial1(number))
elif iterative == "recursive":
    print("Factorial:", factorial2(number))
else:
    print("Invalid method. Please enter 'iterative' or 'recursive'.")
"""
•	factorial1  Should take an integer as input and using an iterative approach calculate factorial for the integer.
•	factorial2  Should take an integer as input and using a recursive approach calculate factorial for the integer.
•	The program should accept two arguments from the command line.  The first is a method (ie. iterative, recursive) and the second is an integer from the command line.
•	Using the requested method calculate factorial and print the result on the screen.

"""