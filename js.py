from notebook import convert
import getopt
import sys
import os
import ast

from notebook import convert


if __name__ == '__main__':
    if len(sys.argv) not in (2,3):
        print "Need exactly one argument, the filename, and one option -n"
        exit(1)

    semis = True

    try:
        opts, args = getopt.getopt(sys.argv[2:], "n", ["no_semicolons"])
    except getopt.GetoptError:
        sys.exit(2)


    for opt, arg in opts:
        if opt in ("-n", "--no_semicolons"):
            semis = False

    filename = sys.argv[1]
    with open(os.path.abspath(filename)) as f:
        t = ast.parse(f.read(), filename)
        print convert(t, semis)
