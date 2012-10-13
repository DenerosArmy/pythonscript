var py = require("./py");
console.log ("Testing factorial");
factorial = py.def ({}, function (n) {
    if (n > 0) {
        return n * factorial ([n - 1], {});
    } else {
        return 1;
    };
});
console.log ("Factorial of 2 is", factorial ([2], {}));
console.log ("Factorial of 3 is", factorial ([3], {}));
console.log ("Factorial of 4 is", factorial ([4], {}));
console.log ("Factorial of 5 is", factorial ([5], {}));

