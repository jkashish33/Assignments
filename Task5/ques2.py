import sys
try:
    with open(sys.argv[1], 'r') as my_file:
        print(my_file.read())
except FileNotFoundError:
    print("File Not found.")