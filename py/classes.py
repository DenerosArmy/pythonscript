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


t = tuple([1, 2, 3])
print "length of tuple", py.len(t)
print "Tuple contains 2?", py.contains(t, 2)
print "Tuple contains 5?", py.contains(t, 5)
