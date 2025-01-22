import sys
if len(sys.argv)!=2:
    print("Usage: python linecount.py <filename>")
    sys.exit(1)
try:
    with open(sys.argv[1],'r') as file:
        lines = file.readlines()
        print(f"Number of lines: {len(lines)}")
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")