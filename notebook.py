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
    if str(func) == 'js':
        assert len(obj.args) == 1, "Cannot call 'js' built-in with more than one argument"
        s = obj.args[0]
        assert type(s) == ast.Str, "Cannot call 'js' built-in with non-string argument"
        return js_ast.RawExpression(s.s)
    args = js_ast.List(map(convert, obj.args))
    kwargs_explicit = {kw.arg: convert(kw.value) for kw in obj.keywords }
    kwargs_dict = obj.kwargs
    if kwargs_explicit and kwargs_dict:
        raise NotImplementedError, "Both explicit keyword args and kwargs dict are not permitted"
    elif kwargs_dict:
        kwargs = convert(kwargs_dict)
    else:
        kwargs = js_ast.Dict(kwargs_explicit.keys(), kwargs_explicit.values())
    
    return js_ast.Call(func, [args, kwargs])

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
def _sub(obj): return js_ast.BinOp('-')
@converts(ast.Div)
def _div(obj): return js_ast.BinOp('/')
@converts(ast.Mod)
def _(obj): return js_ast.BinOp('%')
@converts(ast.And)
def _and(obj): return js_ast.BoolOp('&&')
@converts(ast.Or)
def _or(obj): return js_ast.BoolOp('||')
@converts(ast.Not)
def _not(obj): return js_ast.UnaryOp('!')
@converts(ast.Eq)
def _eq(obj): return js_ast.CompareOp('==')
@converts(ast.NotEq)
def _neq(obj): return js_ast.CompareOp('!=')
@converts(ast.Lt)
def _lt(obj): return js_ast.CompareOp('<')
@converts(ast.LtE)
def _lte(obj): return js_ast.CompareOp('<=')
@converts(ast.Gt)
def _gt(obj): return js_ast.CompareOp('>')
@converts(ast.GtE)
def _gte(obj): return js_ast.CompareOp('>=')

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
    name = js_ast.Name(obj.name)
    args = map(convert, obj.args.args)
    str_args = [js_ast.Str(o.id) for o in obj.args.args]
    kwarg = obj.args.kwarg # arg kwargs go in
    vararg = obj.args.vararg # arg varargs go in
    if vararg:
        args.append(js_ast.Name(vararg))
    if kwarg:
        args.append(js_ast.Name(kwarg))
    defaults = dict(reversed(zip(reversed(str_args), map(convert, reversed(obj.args.defaults)))))
    #print 'Defaults', defaults
    
    assert not obj.decorator_list, "Decorators are not supported"
    body = map(convert, obj.body)
    
    passed_args = []
    if kwarg:
        passed_args.append(js_ast.Name('py.kwargs'))
    if vararg:
        passed_args.append(js_ast.Name('py.args'))
    passed_args.append(js_ast.Dict(defaults.keys(), defaults.values()))
    #print "Passed Args", passed_args
    the_fn = js_ast.Function(args, body)
    passed_args.append(the_fn)
    
    the_def = js_ast.Call(js_ast.Name("py.def"), passed_args)
    return js_ast.Assign(js_ast.Name(name), the_def)

# <codecell>

@converts(ast.Dict)
def _dict(obj):
    return js_ast.Dict(map(convert, obj.keys), map(convert, obj.values))

# <codecell>

@converts(ast.Str)
def _str(obj):
    return js_ast.Str(obj.s)

# <codecell>

#@converts(ast.Import)
#def _import(obj):
#    return js_ast.RawStatement('')

# <codecell>

@converts(ast.ImportFrom)
def _importfrom(obj):
    module = obj.module
    assert module == 'pythonscript', "Only pythonscript module may be imported"
    return js_ast.NullStatement()

# <codecell>

@converts(ast.Return)
def _return(obj):
    return js_ast.Return(convert(obj.value))

# <codecell>

@converts(ast.Compare)
def compare(obj):
    assert len(obj.ops) == 1, "Does not support multiple comparisons in one statement"
    return js_ast.Compare(convert(obj.ops[0]), convert(obj.left), convert(obj.comparators[0]))

@converts(ast.While)
def _while(obj):
    test = obj.test
    body = obj.body
    return js_ast.While(convert(test), map(convert, body))

@converts(ast.For)
def _for(obj):
    target = obj.target
    body = obj.body
    _iter = obj.iter
    return js_ast.For(convert(target), convert(_iter), map(convert, body))
