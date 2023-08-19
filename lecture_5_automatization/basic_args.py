import sys
print()
args = sys.argv
if len(args) == 1:
    print('Please input filename')
else:
    filename = args[1]
    with open(filename) as f:
        print(f.read())
print()
