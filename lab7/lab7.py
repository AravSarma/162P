import sys
from shapes import Triangle, Diamond, Rectangle, Square
#using sys to make it easier for me to pass file
def read_shapes_from_file(filename):
    shapes = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 0:
                    continue
                shape_type = parts[0].lower()
                symbol = parts[1]


                if shape_type == "triangle":
                    #parts is index of item i need, size, widht height etc. 
                    size = int(parts[2])
                    shapes.append(Triangle(symbol, size))
                elif shape_type == "diamond":
                    size = int(parts[2])
                    shapes.append(Diamond(symbol, size))
                elif shape_type == "rectangle":
                    width, height = int(parts[2]), int(parts[3])
                    shapes.append(Rectangle(symbol, width, height))
                elif shape_type == "square":
                    size = int(parts[2])
                    shapes.append(Square(symbol, size))
                else:
                    print(f"Unknown shape: {shape_type}")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    
    return shapes

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python lab7.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    shapes = read_shapes_from_file(filename)

    for shape in shapes:
        shape.draw()
        print()  
