from pythonscript import js
py = js.require('./py')

class Foo(object):
    def __init__(self, x):
        self.x = x
        print 'initing', x
    def print_x(self):
        print self.x

f = Foo(2)
f.print_x()

# library functions

t = (1, 2, 3)
print "length of tuple", py.len(t)
print "Tuple contains 2?", py.contains(t, 2)
print "Tuple contains 5?", py.contains(t, 5)
print "Tuple iteratior is:", py.iter(t)
print "Tuple string is:", py.str(t)

print "Range(0, 50, 2)", py.range(0, 50, 2)


# t = list([1, 2, 3, 4])
# print "length of list", py.len(t)
# print "List contains 2?", py.contains(t, 2)
# print "List contains 5?", py.contains(t, 5)
# print "List iteratior is:", py.iter(t)
# print "List string is:", py.str(t)
