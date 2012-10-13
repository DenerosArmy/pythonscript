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
            string += "{0}\n".format(stmt)
        return string


class Expression(object):
    def __init__(self):
        pass


class Statement(object):
    def __init__(self):
        pass


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
        string = "function {0}(".format(self.name)
        for arg in self.args:
            string += arg + ", "
        string = string[:-2] + ") {\n"
        for stmt in self.body:
            string += "    {0};\n".format(stmt)
        string += "}\n"
        return string


class Return(Statement):
    def __init__(self, value):
        """
        @type value: L{Statement}
        """
        self.value = value

    def __str(self):
        return "return {0};".format(self.value)


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
    def __init__(self, values):
        """
        @type value: C{str}
        """
        self.values = values

    def __str__(self):
        return ""


class For(Statement):
    def __init__(self, iter_var, condition, body, orelse):
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
        self.orelse = orelse

    def __str__(self):
        return ""


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
        return ""


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
        return ""


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
        return ""


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
        return ""


class Unary(Expression):
    def __init__(self, op, values):
        """
        @type op: L{UnaryOp}
        @type values: C{list}
        @param values: list of L{Expression}
        """
        self.op = op
        self.values = values

    def __str__(self):
        return ""


class Dict(Expression):
    def __init__(self, keys, values):
        """
        @type keys: C{list}
        @type values: C{list}
        """
        self.keys = keys
        self.values = values

    def __str__(self):
        return ""


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
        return ""


class Call(Expression):
    def __init__(self, func, args):
        """
        @type func: L{Function}
        @type args: C{list}
        @param args: list of L{Expression}
        """
        self.func = func
        self.args = args

    def __str__(self):
        return ""


class Num(Expression):
    def __init__(self, value):
        """
        @type value: C{int} or C{float}
        """
        self.value = value

    def __str__(self):
        return ""


class Str(Expression):
    def __init__(self, value):
        """
        @type value: C{str}
        """
        self.value = value

    def __str__(self):
        return ""


class Name(Expression):
    def __init__(self, name):
        """
        @type name: C{str}
        """
        self.name = name

    def __str__(self):
        return ""

class List(Expression):
    def __init__(self, elem):
        """
        @type elem: C{list}
        @param elem: list of C{Expression}
        """
        self.elem = elem

    def __str__(self):
        return ""


class BoolOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("||", "$$")
        self.op = op

    def __str__(self):
        return ""


class BinOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("+", "-", "*", "/", "%")
        self.op = op

    def __str__(self):
        return ""


class UnaryOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("!")
        self.op = op

    def __str__(self):
        return ""


class CompareOp(object):
    def __init__(self, op):
        """
        @type op: C{str}
        """
        assert op in ("==", "===", "!=", "!==", ">", "<", ">=", "<=")
        self.op = op

    def __str__(self):
        return ""
