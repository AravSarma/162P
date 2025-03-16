class Pascal:
    def __init__(self):
        self.data = {}

    def get_val(self, row, col):
        if col == 0 or col == row:
            return 1
        if (row, col) in self.data:
            return self.data[(row, col)]
        
        #recursion
        val = self.get_val(row - 1, col - 1) + self.get_val(row - 1, col)
        self.data[(row, col)] = val
        return val

    def display_tri(self, num_r):
        for r in range(num_r):
            row_val = [self.get_val(r, col) for col in range(r + 1)]
            print(" ".join(map(str, row_val)).center(num_r * 3))  

if __name__ == "__main__":
    num_lines = int(input("enter number of rows for pascals triangle: "))
    pascal = Pascal()
    pascal.display_tri(num_lines)
