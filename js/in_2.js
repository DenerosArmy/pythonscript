py = require ("./py");
console.log ("Test in_2");
in_2 = py.def ({}, function () {
    return 1 + 2;
});
console.log (in_2 ([], {}));
console.log ("End test in_2");

