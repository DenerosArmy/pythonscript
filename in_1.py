from pythonscript import js
js('var py = require("./py")')
js('console.log("Test in_1")')
def foo(x, y=1, **kwargs):
    print x+y
foo(**{'x': 1, 'y': 2})
js('console.log("End test in_1")')
