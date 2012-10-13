var py = require("./py");
console.log ("Testing decorators");
inc = py.def ({}, function (fn) {
    the_fn = py.def ({}, function (x) {
        return fn ([x], {}) + 1;
    });
    return the_fn;
});
foo = inc ([inc ([py.def ({}, function (x) {
    return x;
})], {})], {});
console.log ("foo(1) is", foo ([1], {}));

