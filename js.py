from notebook import convert
import sys
import ast

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Need exactly one argument, the filename"
        exit(1)

    filename = sys.argv[1]
    with open(filename) as f:
        t = ast.parse(f.read(), filename)
        print convert(t)
