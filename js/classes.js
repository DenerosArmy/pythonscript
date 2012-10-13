py = require ("./py");
_Foo = function (args, kwargs) {
    this.__init__ = py.instancemethod ([py.def ({}, function (self, x) {
        self.x = x;
        console.log ("initing", x);
    })], {});
    this.print_x = py.instancemethod ([py.def ({}, function (self) {
        console.log (self.x);
    })], {});
    this.__init__ (args, kwargs);
};
Foo = function (args, kwargs) {
    return new _Foo(args, kwargs);
};
f = Foo ([2], {});
f.print_x ([], {});
t = tuple ([[1, 2, 3]], {});
console.log ("length of tuple", py.len ([t], {}));
console.log ("Tuple contains 2?", py.contains ([t, 2], {}));
console.log ("Tuple contains 5?", py.contains ([t, 5], {}));
console.log ("Tuple iteratior is:", py.iter ([t], {}));
console.log ("Tuple string is:", py.str ([t], {}));

