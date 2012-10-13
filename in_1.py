from pythonscript import js

js('console.log("Test in_1");')
def foo(x, y=1, **kwargs):
    print y
foo(**{'y': 2})
js('console.log("End test in_1");')
