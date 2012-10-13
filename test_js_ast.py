from unittest import TestCase

from js_ast import *


class JavascriptASTTest(TestCase):
    def test_module(self):
        module = Module(["test_statement1", "test_statement2"])
        self.assertEqual(str(module), "test_statement1;\ntest_statement2;\n")


    def test_function(self):
        function = Function("func", ["arg0", "arg1"], ["body0", "body1"])
        self.assertEqual(str(function), "function func (arg0, arg1) {\n    body0;\n    body1;\n}")


    def test_return(self):
        return_node = Return("1")
        self.assertEqual(str(return_node), "return 1;")


    def test_declare_var(self):
        declaration = DeclareVar(["a", "b", "c"])
        self.assertEqual(str(declaration), "var a, b, c")


    def test_assign(self):
        assign = Assign("x", 1)
        self.assertEqual(str(assign), "x = 1")


    def test_print_empty(self):
        print_node = Print("")
        self.assertEqual(str(print_node), "console.log()")

    def test_print_int(self):
        print_node = Print("1")
        self.assertEqual(str(print_node), "console.log(1)")

    def test_print_list(self):
        print_node = Print("[1, 2, 3, 4]")
        self.assertEqual(str(print_node), "console.log([1, 2, 3, 4])")


    def test_for(self):
        for_node = For("i=0", "i<10", "i++", ["func()"])
        self.assertEqual(str(for_node), "for (i=0; i<10; i++) {\n    func();\n}")


    def test_while(self):
        while_node = While("a=b", ["func()"])
        self.assertEqual(str(while_node), "while (a=b) {\n    func();\n}")


    def test_if(self):
        if_node = If("a=b", ["func()"], ["func()"])
        self.assertEqual(str(if_node), "if (a=b) {\n    func();\n} else {\n    func();\n}")


    def test_bool(self):
        op = BoolOp("&&")
        bool_node = Bool(op, ["True", "False"])
        self.assertEqual(str(bool_node), "True && False")
        op = BoolOp("||")
        bool_node = Bool(op, ["True", "False"])
        self.assertEqual(str(bool_node), "True || False")


    def test_bin(self):
        op = BinOp("+")
        bin_node = Bin(op, "4", "5")

    def test_call(self):
        call_node = Call("func", ["asdf", "asdf"])
        self.assertEqual(str(call_node), "func (asdf, asdf)")


    def test_empty_dict(self):
        dict_node = Dict([], [])
        self.assertEqual(str(dict_node), "{}")

    def test_dict(self):
        dict_node = Dict(["key0", "key1"], ["val0", "val1"])
        self.assertEqual(str(dict_node), "{key0:val0, key1:val1}")


    def test_empty_list(self):
        list_node = List([])
        self.assertEqual(str(list_node), "[]")

    def test_list(self):
        list_node = List(["a", "b", "c"])
        self.assertEqual(str(list_node), "[a, b, c]")


    def test_str(self):
        str_node = Str("asdf")
        self.assertEqual(str(str_node), '"asdf"')
