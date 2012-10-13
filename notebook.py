# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import ast

# <codecell>

import js_ast

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
    return [convert(o) for o in obj.body]

# <codecell>

@converts(ast.Assign)
def assign(obj):
    assert len(obj.targets) == 1, "Tuple assignment not supported"
    return js_ast.Assign(convert(obj.targets[0]), convert(obj.value))
        

# <codecell>

@converts(ast.Name)
def name(obj):
    return js_ast.Name(obj.id)

# <codecell>

@converts(ast.Num)
def num(obj):
    return ['NUMBER', obj.n]

# <codecell>

TEXT = """
x = True
"""

# <codecell>

t = ast.parse(TEXT)

# <codecell>

c = convert(t)

# <codecell>


# <codecell>


# <codecell>


