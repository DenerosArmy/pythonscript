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
            js("""for (var index in self._items) {
                count += 1;
            }
            """)
            self._len = count
            return count
        else:
            return self._len

    def __contains__(self, item):
        js("""for (var index in self._items) {
                  if (item === self._items[index]) {
                      return true;
                  }
              }
              """)
        return False

    def __iter__(self):
        return self._items

    def __str__(self):
        res = "("
        js("""for (var index in self._items) {
                  res += '' + self._items[index] + ','
              }
              """)
        res +=  ')'
        return res

def range(start, stop=None, step=1):
    if stop == None:
        stop = start
        start = 0
    res = []
    a = start
    while a+step <= stop:
        js("res[res.length] = a;")
        a += step
    return res

js.exports.len = len
js.exports.iter = iter
js.exports.str = str
js.exports.tuple = tuple
js.exports.range = range
