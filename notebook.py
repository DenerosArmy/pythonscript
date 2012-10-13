# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import ast

# <codecell>

import js_ast

# <codecell>

def jsp(obj):
    if type(obj) not in vars(js_ast).values():
        if type(obj) == list or type(obj) == tuple:
            return map(jsp, obj)
        else:
            return obj
    return {k:jsp(v) for k, v in vars(obj).items()}

# <codecell>

converters = {}

# <codecell>

def converts(cls):
    def real_decorator(fn):
        converters[cls] = fn
        return fn
    return real_decorator

# <codecell>

def convert(obj):
    if type(obj) in converters:
        return converters[type(obj)](obj)
    else:
        return None

# <codecell>

@converts(ast.Module)
def module(obj):
    return js_ast.Module(map(convert, obj.body))

# <codecell>

@converts(ast.Assign)
def assign(obj):
    assert len(obj.targets) == 1, "Multi-assignment not supported"
    assert type(obj.targets) != ast.Tuple, "Tuple assignment not supported"
    return js_ast.Assign(convert(obj.targets[0]), convert(obj.value))
        

# <codecell>

@converts(ast.Name)
def name(obj):
    return js_ast.Name(obj.id)

# <codecell>

@converts(ast.Num)
def num(obj):
    return js_ast.Num(obj.n)

# <codecell>

@converts(ast.Call)
def call(obj):
    func = convert(obj.func)
    args = js_ast.List(map(convert, obj.args))
    kwargs_ = {kw.arg: convert(kw.value) for kw in obj.keywords }
    kwargs = js_ast.Dict(kwargs_.keys(), kwargs_.values())
    return js_ast.Call(func, js_ast.List([args, kwargs]))

# <codecell>

@converts(ast.Expr)
def expression(obj):
    value = obj.value
    return convert(value)

# <codecell>

@converts(ast.BoolOp)
def boolop(obj):
    op = obj.op
    values = map(convert, obj.values)
    assert convert(op) is not None, "Operator " + str(op) + " is not supported"
    return js_ast.Bool(convert(op), values)

# <codecell>

@converts(ast.BinOp)
def binop(obj):
    op = obj.op
    left = obj.left
    right = obj.right
    return js_ast.Bin(convert(op), convert(left), convert(right))

# <codecell>

@converts(ast.UnaryOp)
def unaryop(obj):
    op = obj.op
    operand = obj.operand
    return js_ast.Unary(convert(op), convert(operand))

# <codecell>

@converts(ast.Add)
def _add(obj): return js_ast.BinOp('+')
@converts(ast.Mult)
def _mult(obj): return js_ast.BinOp('*')
@converts(ast.Sub)
def _mult(obj): return js_ast.BinOp('-')
@converts(ast.Div)
def _mult(obj): return js_ast.BinOp('/')
@converts(ast.Mod)
def _(obj): return js_ast.BinOp('%')
@converts(ast.And)
def _and(obj): return js_ast.BoolOp('&&')
@converts(ast.Or)
def _or(obj): return js_ast.BoolOp('||')
@converts(ast.Not)
def _not(obj): return js_ast.UnaryOp('!')

# <codecell>

@converts(ast.If)
def _if(obj):
    test = obj.test
    body = obj.body
    orelse = obj.orelse
    return js_ast.If(convert(test), map(convert, body), map(convert, orelse))

# <codecell>

@converts(ast.Print)
def _print(obj):
    values = obj.values
    newline = obj.nl # TODO: actually handle this
    dest = obj.dest
    assert dest is None, "Only printing to stdout is supported"
    return js_ast.Call(js_ast.Name('console.log'), map(convert, values))

# <codecell>

@converts(ast.FunctionDef)
def _def(obj):
    name = obj.name
    args = map(convert, obj.args.args)
    kwarg = obj.args.kwarg # arg kwargs go in
    vararg = obj.args.vararg # arg varargs go in
    if vararg:
        args.append(js_ast.Name(vararg))
    if kwarg:
        args.append(js_ast.Name(kwarg))
    
    assert not obj.decorator_list, "Decorators are not supported"
    body = map(convert, obj.body)

# <codecell>

TEXT = """
x + 2
"""

# <codecell>

t = ast.parse(TEXT)
print ast.dump(t)
print 'PARSED'
print jsp(convert(t))
print 'CONVERTED'
print convert(t)

# <codecell>


# <codecell>

# TODO: x * (y+z)   SAME AS (x * y) + z - > x*y+z ----- why is this wrong?
