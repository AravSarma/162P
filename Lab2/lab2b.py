def count_ages(filename):
    with open(filename,'r') as file : 
        lines = file.readlines()
    age_count = {}
    for line in lines: 
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        part  = line.split('|')
        if len(part)<4:
            continue
        #using try because of file reading n manipulation to
        #catch unexpected erros etc. 
        try: 
            age = int(part[2].strip())
            if age in age_count:
                age_count[age]+=1
            else:
                age_count[age]=1
        #if value not valid
        except ValueError:
            continue
    for age in sorted(age_count.keys()):
        print(f"Age: {age} -> Count: {age_count[age]}")    
if __name__ == "__main__":
    count_ages("lab2-data.txt")    
"""
read
count occurence of age, return counts of age  
"""
