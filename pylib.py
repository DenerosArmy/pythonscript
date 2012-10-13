from pythonscript import js
js('var py = require("./py")')

def instancemethod(fn):
    def the_fn(*args, **kwargs):
        return fn(*js('[this].concat(args)'), **kwargs)
    return the_fn

js('exports.instancemethod = instancemethod')
