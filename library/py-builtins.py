from pythonscript import js
# Python built-ins library

def len(seq):
    return seq.__len__()

def iter(seq):
    return seq.__iter__()

def str(seq):
    return seq.__str__()


class tuple(object):
    def __init__(self, items):
        self._items = items
        self._len = -1

    def __len__(self):
        if self._len == -1:
            count = 0
            for elem in self._items:
                count += 1
            self._len = count
            return count
        else:
            return self._len

    def __contains__(self, item):
        for other in self._items:
            if item == other:
                return True
        return False

    def __iter__(self):
        return self._items

    def __str__(self):
        res = "("
        for item in self._items:
            res += '' + item + ','
        res +=  ')'
        return res

def range(start, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0
    res = []
    a = start
    while a+step <= stop:
        res[res.length] = a
        a += step
    return res

js.exports.len = len
js.exports.iter = iter
js.exports.str = str
js.exports.tuple = tuple
js.exports.range = range
