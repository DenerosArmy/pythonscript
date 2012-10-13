var py = require("./py");
var unit = require("nodeunit");

foobar = py.def({},function() {
	console.log("fuck");
})
foobar1 = py.def( py.kwargs, {'c' : 1}, function(a, b, c, kwargs) {
        return a;
}); 
foobar2 = py.def(py.args, py.kwargs, function(a, b, args, kwargs) {
    return arguments;
})
console.log(foobar2([1,2,3,4,5,6,7,8,9,10],{}));
exports.foobar1 = foobar1;
exports.foobar = foobar;
exports.py = py;
