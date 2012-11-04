"""
TODO: 
TryCatch(Statement)
"""


class Module(object):
    def __init__(self, body, semis=True):
        """
        @type body: C{list}
        @param body: list of C{Statement}
        @type semis: C{bool}
        @para semis: whether or not to use semis
        """
        self.body = body
        self.semis = semis

    def __str__(self):
        string = ""
        for stmt in self.body:
            if type(stmt) != NullStatement and str(stmt).strip() != "":
                lines = str(stmt).split("\n")
                for line in lines:
                    if line[-1] not in ("{", "(", "}") and self.semis:
                        string += "{0};\n".format(line)
                    else:
                        string += "{0}\n".format(line)
        return string


class Expression(object):
    def __init__(self):
        pass


class Statement(object):
    def __init__(self):
        pass


class RawExpression(Expression):
    def __init__(self, exp):
        """
        @type exp: C{str}
        """
        self.exp = exp

    def __str__(self):
        return self.exp


class RawStatement(Statement):
    def __init__(self, stmt):
        """
        @type exp: C{str}
        """
        self.stmt= stmt

    def __str__(self):
        return self.stmt


class NullStatement(Statement):
    def __str__(self):
        return ""
    pass


class Function(Statement):
    def __init__(self, args, body):
        """
        @type args: C{list}
        @param args: list of L{Name}
        @type body: C{list}
        @param body: list of L{Statement}
        """
        self.args = args
        self.body = body

    def __str__(self):
        string = "function ("
        if len(self.args) > 0:
            for arg in self.args:
                string += str(arg) + ", "
            string = string[:-2] + ") {\n"
        else:
            string += ") {\n"

        for stmt in self.body:
            if type(stmt) != NullStatement and str(stmt) != "":
                lines = str(stmt).split("\n")
                for line in lines:
                    string += "    {0}\n".format(line)
        string += "}"
        return string


class Vars(Statement):
    def __init__(self, names):
        """
        @type names: C{list}
        @param names: list of strings as local variable names
        """
        self.names = names

    def __str__(self):
        if len(self.names) == 0:
            return ""
        string = "var "
        for name in self.names:
            string += "{0}, ".format(name)
        return string[:-2]


class Return(Statement):
    def __init__(self, value):
        """
        @type value: L{Statement}
        """
        self.value = value

    def __str__(self):
        return "return {0}".format(self.value)


class DeclareVar(Statement):
    def __init__(self, variables):
        """
        @type var: C{list}
        @param var: list of L{names}
        """
        self.variables = variables

    def __str__(self):
        string = "var "
        for var in self.variables:
            string += "{0}, ".format(var)
        return string[:-2]


class Assign(Statement):
    def __init__(self, target, value):
        """
        @type target: L{Name}
        @type value: L{Expression}
        """
        self.target = target
        self.value = value

    def __str__(self):
        return "{0} = {1}".format(self.target, self.value)


class AugAssign(Statement):
    def __init__(self, target, op, value):
        """
        @type target: L{Name}
        @type op: L{BinOp}
        @type target: L{Expression}
        """
        self.target = target
        self.op = op
        self.value = value

    def __str__(self):
        return "{0} {1}= {2}".format(self.target, self.op, self.value)


class Print(Statement):
    def __init__(self, value):
        """
        @type value: anything that can be printed
        """
        self.value = value

    def __str__(self):
        return "console.log({0})".format(self.value)


class For(Statement):
    def __init__(self, target, iterable, body):
        """
        @type target: L{Name}
        @type iterable: L{Expression}
        @param iterable: an expression that returns an iterable object
        @type body: C{list}
        @param body: list of L{Statement}
        """
        self.target = target
        self.iterable = iterable
        self.body = body

    def __str__(self):
        string = "for ({0} in {1}) {{\n".format(self.target, self.iterable)
        for elem in self.body:
            if type(elem) != NullStatement and str(elem) != "":
                lines = str(elem).split("\n")
                for line in lines:
                    string += "    {0}\n".format(line)
        return string + "}"


class While(Statement):
    def __init__(self, condition, body):
        """
        @type condition: L{expression}
        @type body: L{list}
        @param body: list of L{Statement}
        """
        self.condition = condition
        self.body = body

    def __str__(self):
        string = "while ({0}) {{\n".format(self.condition)
        for elem in self.body:
            if type(elem) != NullStatement and str(elem) != "":
                lines = str(elem).split("\n")
                for line in lines:
                    string += "    {0}\n".format(line)
        return string + "}"


class If(Statement):
    def __init__(self, condition, if_body, else_body):
        """
        @type condition: L{Statement}
        @type if_body: C{list}
        @param if_body: list of L{Statement}
        @type else_body: C{list}
        @param else_body: list of L{Statement}
        """
        self.condition = condition
        self.if_body = if_body
        self.else_body = else_body

    def __str__(self):
        string = "if ({0}) {{\n".format(self.condition)
        for elem in self.if_body:
            if type(elem) != NullStatement and str(elem) != "":
                lines = str(elem).split("\n")
                for line in lines:
                    string += "    {0}\n".format(line)
        if self.else_body:
            string += "} else {\n"
            for elem in self.else_body:
                if type(elem) != NullStatement and str(elem) != "":
                    lines = str(elem).split("\n")
                    for line in lines:
                        string += "    {0}\n".format(line)
        return string + "}"


class Bool(Expression):
    def __init__(self, op, values):
        """
        @type op: L{BoolOp}
        @type values: C{list}
        @param values: list of L{Expression}
        """
        self.op = op
        self.values = values

    def __str__(self):
        string = ""
        for val in self.values:
            string += "{0} {1} ".format(val, self.op)
        return string[:-4]


class Bin(Expression):
    def __init__(self, op, left, right):
        """
        @type op: L{BinOp}
        @type left: L{Expression}
        @type right: L{Expression}
        """
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        if str(self.op) in ("+", "-"):
            return "({0} {1} {2})".format(self.left, self.op, self.right)
        return "{0} {1} {2}".format(self.left, self.op, self.right)


class Unary(Expression):
    def __init__(self, op, value):
        """
        @type op: L{UnaryOp}
        @type values: C{list}
        @param values: list of L{Expression}
        """
        self.op = op
        self.value = value

    def __str__(self):
        if len(self.value.split()) == 1:
            return "{0}{1}".format(self.op, self.value)
        return "{0}({1})".format(self.op, self.value)


class Dict(Expression):
    def __init__(self, keys, values):
        """
        @type keys: C{list}
        @type values: C{list}
        """
        assert len(keys) == len(values)
        self.keys = keys
        self.values = values

    def __str__(self):
        string = "{"
        for i in xrange(len(self.keys)):
            string += "{0}:{1}, ".format(self.keys[i], self.values[i])
        if string == "{":
            return "{}"
        return string[:-2] + "}"


class Compare(Expression):
    def __init__(self, op, left, right):
        """
        @type op: L{CompareOp}
        @type left: L{Expression}
        @type right: L{Expression}
        """
        self.op = op
        self.left = left
        self.right = right

    def __str__(self):
        return "{0} {1} {2}".format(self.left, self.op, self.right)


class Call(Expression):
    def __init__(self, func, args):
        """
        @type func: L{Name}
        @type args: C{list}
        @param args: list of L{Expression}
        """
        self.func = func
        self.args = args

    def __str__(self):
        string = "{0} (".format(self.func)
        if len(self.args) == 0:
            return string + ")"
        for arg in self.args:
            string += str(arg) + ", "
        return string[:-2] + ")"


class Num(Expression):
    def __init__(self, value):
        """
        @type value: C{int} or C{float}
        """
        self.value = value

    def __str__(self):
        return str(self.value)


class Str(Expression):
    def __init__(self, value):
        """
        @type value: C{str}
        """
        self.value = value

    def __str__(self):
        return '"{0}"'.format(self.value)


class Attribute(Expression):
    def __init__(self, value, attr):
        """
        @type attr: C{str}
        @type value: C{Expression}
        """
        self.value = value
        self.attr = attr

    def __str__(self):
        return "{0}.{1}".format(self.value, self.attr)


class Subscript(Expression):
    def __init__(self, value, index):
        """
        @type value: L{Name}
        @type index: C{Expression}
        """
        self.value = value
        self.index = index

    def __str__(self):
        return "{0}[{1}]".format(self.value, self.index)


class Name(Expression):
    def __init__(self, name):
        """
        @type name: C{str}
        """
        self.name = name

    def __str__(self):
        return str(self.name)

class List(Expression):
    def __init__(self, elems):
        """
        @type elem: C{list}
        @param elem: list of C{Expression}
        """
        self.elems = elems

    def __str__(self):
        string = "["
        for elem in self.elems:
            string += "{0}, ".format(elem)
        if string == "[":
            return "[]"
        return string[:-2] + "]"


class BoolOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("||", "&&")
        self.op = op

    def __str__(self):
        return self.op


class BinOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("+", "-", "*", "/", "%")
        self.op = op

    def __str__(self):
        return self.op


class UnaryOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("!", "~")
        self.op = op

    def __str__(self):
        return self.op


class CompareOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("==", "===", "!=", "!==", ">", "<", ">=", "<=")
        self.op = op

    def __str__(self):
        return self.op
