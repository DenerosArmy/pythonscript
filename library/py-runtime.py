from pythonscript import js
# Python library to help with implementation of a Python runtime in Javascript

def instancemethod(fn):
    def the_fn(*args, **kwargs):
        return fn(*js('[this].concat(args)'), **kwargs)
    return the_fn
js.py.instancemethod = instancemethod

def contains(seq, item):
    return seq.__contains__(item)

js.exports.instancemethod = instancemethod
js.exports.contains = contains
