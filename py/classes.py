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

    def __iter__(self):
        return self._items

    def __str__(self):
        res = "("
        js("""for (var index in self._items) {
                  res += '' + self._items[index] + ','
              }
              """)
        res = res + ')' # TODO: why does += not work here?
        return res

t = (1, 2, 3)
print "length of tuple", py.len(t)
print "Tuple contains 2?", py.contains(t, 2)
print "Tuple contains 5?", py.contains(t, 5)
print "Tuple iteratior is:", py.iter(t)
print "Tuple string is:", py.str(t)


# t = list([1, 2, 3, 4])
# print "length of list", py.len(t)
# print "List contains 2?", py.contains(t, 2)
# print "List contains 5?", py.contains(t, 5)
# print "List iteratior is:", py.iter(t)
# print "List string is:", py.str(t)
