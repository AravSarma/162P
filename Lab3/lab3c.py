def is_palindrome(s): 
    if len(s) <=1: 
        #len of 1  is a palindrome 
        return True  
    #check if first and last char the same if not return false  
    if s[0] != s[-1]: 
        return False 
    return is_palindrome(s[1:-1])

user_input = input("\nEnter a string for palindrome check: ").strip().lower().replace(" ","")

print("Palindrome" if is_palindrome(user_input) else "not palindrome")