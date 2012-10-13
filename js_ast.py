"""
TODO: 
TryCatch(Statement)
"""


class Module(object):
    def __init__(self, body):
        """
        @type body: C{list}
        @param body: list of C{Statement}
        """
        self.body = body

    def __str__(self):
        string = ""
        for stmt in self.body:
            string += "{0};\n".format(stmt)
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


class Function(Statement):
    def __init__(self, name, args, body):
        """
        @type name: L{Name}
        @type args: C{list}
        @param args: list of L{Name}
        @type body: C{list}
        @param body: list of L{Statement}
        """
        self.name = name
        self.args = args
        self.body = body

    def __str__(self):
        string = "function {0} (".format(self.name)
        if len(self.args) > 0:
            for arg in self.args:
                string += str(arg) + ", "
            string = string[:-2] + ") {\n"
        else:
            string += ") {\n"

        for stmt in self.body:
            string += "    {0};\n".format(stmt)
        string += "}"
        return string


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


class Print(Statement):
    def __init__(self, value):
        """
        @type value: anything that can be printed
        """
        self.value = value

    def __str__(self):
        return "console.log({0})".format(self.value)


class For(Statement):
    def __init__(self, iter_var, condition, inc, body):
        """
        @type iter_var: L{Statement}
        @type condition: L{Expression}
        @type body: C{list}
        @param body: list of L{Statement}
        @type orelse: L{Statement}
        """
        self.iter_var = iter_var
        self.condition = condition
        self.body = body
        self.inc = inc

    def __str__(self):
        string = "for ({0}; {1}; {2}) {{\n".format(self.iter_var, self.condition, self.inc)
        for elem in self.body:
            string += "    {0};\n".format(elem)
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
            string += "    {0};\n".format(elem)
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
            string += "    {0};\n".format(elem)
        if self.else_body:
            string += "} else {\n"
            for elem in self.else_body:
                string += "    {0};\n".format(elem)
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
        if self.op in ("+", "-"):
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
