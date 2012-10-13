from pythonscript import js
js('var py = require("./py")')
print "Testing factorial"
def factorial(n):
    if (n > 0):
        return n * factorial(n-1)
    else:
        return 1

print "Factorial of 2 is", factorial(2)
print "Factorial of 3 is", factorial(3)
print "Factorial of 4 is", factorial(4)
print "Factorial of 5 is", factorial(5)
