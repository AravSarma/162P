def load_data(filename, delimiter='|'):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            row = line.strip().split(delimiter)
            if len(row) == 3:  
                name, age, major = row
                data.append((name, int(age), major))  
    return data

def sort_data(data, sort_by=0):
    return sorted(data, key=lambda x: x[sort_by])

def display_data(data):
    print("\nsorted data:")
    print("Name\tAge\tMajor")
    print("-" * 35)
    for entry in data:
        print(f"{entry[0]}\t{entry[1]}\t{entry[2]}")

def main():
    filename = "data.txt" 
    data = load_data(filename)
    sorted_data = sort_data(data, 0)  
    display_data(sorted_data)

if __name__ == "__main__":
    main()
