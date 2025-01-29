def read_sort_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    people = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):  # Skip header 
            continue

        part = line.split("|")  
        #put this n due to error 
        if len(part) < 4:  
            continue
        try:
            name = part[1].strip()  
            age = int(part[2].strip())  
            people.append((age, name))
            #if age is not a vlid int
        except ValueError:
            continue  

    people.sort()

    for age, name in people:
        print(f"{age}, {name}")

if __name__ == "__main__":
    read_sort_file("lab2-data.txt")



"""
•	Reads in the lab2-data.txt file
•	Splits the lines into parts
•	Recombines the age and name into a line
•	Put the new lines into a list
•	Sort the list using the builtin sort method
•	Use a for loop to look at each line
•	Split the age and name into different parts
•	Display the names in age order
"""
