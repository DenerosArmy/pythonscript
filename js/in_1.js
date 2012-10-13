py = require ("./py");
console.log ("Test in_1");
foo = py.def (py.kwargs, {"y":1}, function (x, y, kwargs) {
    console.log (x + y);
});
foo ([], {"x":1, "y":2});
console.log ("End test in_1");

