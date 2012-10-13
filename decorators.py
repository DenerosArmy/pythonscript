from pythonscript import js
js('var py = require("./py")')
print "Testing decorators"

def inc(fn):
    def the_fn(x):
        return fn(x) + 1
    return the_fn

@inc
@inc
def foo(x):
    return x

print "foo(1) is", foo(1)
