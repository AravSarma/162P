class Point:
    def __init__(self, symbol):
        self.symbol = symbol

    def setSymbol(self, symbol):
        self.symbol = symbol

    def draw(self):
        print(self.symbol)  


class Triangle(Point):
    def __init__(self, symbol, size):
        super().__init__(symbol)
        self.size = size

    def draw(self):
        for i in range(1, self.size + 1):
            print(self.symbol * i)


class Diamond(Point):
    def __init__(self, symbol, size):
        super().__init__(symbol)
        self.size = size

    def draw(self):
        for i in range(1, self.size + 1, 2):
            print(" " * ((self.size - i) // 2) + self.symbol * i)
        for i in range(self.size - 2, 0, -2):
            print(" " * ((self.size - i) // 2) + self.symbol * i)


class Rectangle(Point):
    def __init__(self, symbol, width, height):
        super().__init__(symbol)
        self.width = width
        self.height = height

    def draw(self):
        for _ in range(self.height):
            print(self.symbol * self.width)


class Square(Rectangle):
    def __init__(self, symbol, size):
        super().__init__(symbol, size, size)  

if __name__ == "__main__":
    print("Point:")
    Point('.').draw()
    
    print("\nTriangle:")
    Triangle('X', 4).draw()
    
    print("\nDiamond:")
    Diamond('!', 3).draw()
    
    print("\nRectangle:")
    Rectangle('~', 3, 4).draw()
    
    print("\nSquare:")
    Square('#', 3).draw()
