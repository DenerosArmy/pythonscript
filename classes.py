from pythonscript import js
py = js('require("./py")')
pylib = js('require("./pylib")')

class Foo(object):
    def __init__(self, x):
        print 'initing', x
    def method(self, x ,y):
        print x, y

f = Foo(2)
f.method(0, 0)


