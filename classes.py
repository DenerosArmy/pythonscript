from pythonscript import js
py = js('require("./py")')
pylib = js('require("./pylib")')

class Foo(object):
    def __init__(self, x):
        self.x = x
        print 'initing', x
    def print_x(self):
        print self.x

f = Foo(2)
f.print_x()


