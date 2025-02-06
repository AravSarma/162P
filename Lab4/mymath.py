class Mymath: 
    def absolute(self,num): 
        return abs(num)
    
    def average(self,numbers): 
        if len(numbers) == 0:
            raise ValueError("enter >0")
        return sum(numbers) / len(numbers)
    
    