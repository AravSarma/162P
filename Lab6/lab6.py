from shapes import Point, Triangle, Diamond, Rectangle, Square

def parse_file(filename):
    shapes = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts:
                continue
            
            shape_type = parts[0]
            symbol = parts[1]
            if shape_type == 'P':
                shapes.append(Point(symbol))
            elif shape_type == 'S':
                size = int(parts[2])
                shapes.append(Square(symbol, size))
            elif shape_type == 'T':
                size = int(parts[2])
                shapes.append(Triangle(symbol, size))
            elif shape_type == 'D':
                size = int(parts[2])
                shapes.append(Diamond(symbol, size))
            elif shape_type == 'R':
                width = int(parts[2])
                height = int(parts[3])
                shapes.append(Rectangle(symbol, width, height)) 
    return shapes

def main():
    filename = "lab6-data.txt" 
    shapes = parse_file(filename)
    for shape in shapes:
        shape.draw()
        print()  

if __name__ == "__main__":
    main()
