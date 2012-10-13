from pythonscript import js
py = js.require('./py')
print "Test in_1"
def foo(x, y=1, **kwargs):
    print x+y
foo(**{'x': 1, 'y': 2})
print "End test in_1"
