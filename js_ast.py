"""
TODO: 
TryCatch(Statement)
"""


class Expression(object):
    pass


class Statement(object):
    pass


class Name(object):
    def __init__(self, name):
        """
        @type name: C{str}
        """
        self.name = name


class FunctionDef(Statement):
    def __init__(self, name, args, body):
        """
        @type name: C{str}
        @type args: C{tuple}
        @type body: C{list}
        @param body: list of L{Statement}
        """
        self.name = name
        self.args = args
        self.body = body


class Return(Statement):
    def __init__(self, value):
        """
        @type value: L{Statement}
        """
        self.value = value


class Assign(Statement):
    def __init__(self, target, value)
        """
        @type target: L{Expression}
        @type value: L{Expression}
        """
        self.target = target
        self.value = value


class Print(Statement):
    def __init__(self, values):
        """
        @type value: C{str}
        """
        self.values = values


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


class While(Statement):
    def __init__(self, condition, body):
        """
        @type condition: L{expression}
        @type body: L{list}
        @param body: list of L{Statement}
        """
        self.condition = condition
        self.body = body


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
