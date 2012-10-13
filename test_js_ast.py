from unittest import TestCase

from js_ast import *


class JavascriptASTTest(TestCase):
    def test_module(self):
        module = Module(["test_statement1", "test_statement2"])
        self.assertEqual(str(module), "test_statement1\ntest_statement2\n")

    def test_if(self):
        if_node = If("a=b", ["func()"], ["func()"])
        self.assertEqual(str(if_node), "if (a=b) {\n    func();\n} else {\n    func();\n}")

    def test_while(self):
        while_node = While("a=b", ["func()"])
        self.assertEqual(str(while_node), "while (a=b) {\n    func();\n}")

    def test_for(self):
        for_node = For("i=0", "i<10", "i++", ["func()"])
        self.assertEqual(str(for_node), "for (i=0; i<10; i++) {\n    func();\n}")

    def test_call(self):
        call_node = Call("func", ["asdf", "asdf"])
        self.assertEqual(str(call_node), "func (asdf, asdf)")

    def test_dict(self):
        dict_node = Dict(["key0", "key1"], ["val0", "val1"])
        self.assertEqual(str(dict_node), "{key0:val0, key1:val1}")
