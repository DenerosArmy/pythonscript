var kwargs = {};
var args = {}; 

function compile_exception() { 
  // console.trace("Compile Time Error"); 
   throw("GOOD BYE");
};
function runtime_exception() { 
   //console.trace("Run Time Error"); 
   throw("GOOD BYE");
};
function def() { 
    if (arguments.length < 1) { 
        compile_exception();
    };
    var py_func = arguments[arguments.length - 1];
    var py_defaults = arguments[arguments.length - 2];
    if (typeof py_func != "function") { 
        compile_exception();
    };
    if (typeof py_defaults != "object") { 
        compile_exception();
    };
    var accepts_kwargs = (arguments[0] === kwargs) || (arguments[1] === kwargs) ;
    var accepts_args = (arguments[1] === args) || (arguments[0] === args);
    var py_func_args = get_param_names(py_func);
    var py_num_required_args = 0;

    for (i in py_func_args) { 
        if (i in py_defaults) { 
            break;
        };
        py_num_required_args++;
    };
    if (accepts_args) { 
        py_func_args.pop();
    };
    if (accepts_kwargs) { 
        py_func_args.pop();
    };
    function output_func(args,dict) {
	  //console.log("func is", py_func);
	  //console.log("args are", args);
       var input_args = [];
       var i = 0;
       for (i=0;i<py_func_args.length;i++) {
           if (i < args.length) { 
               input_args[i] = args[i];
            }
           else if (py_func_args[i] in dict) { 
               input_args[i] = dict[py_func_args[i]];
               delete dict[py_func_args[i]];
           }
           else if (py_func_args[i] in py_defaults) { 
               input_args[i] = py_defaults[py_func_args[i]];
           }
           else { 
               runtime_exception();
                }
        }
        var rest_args = [];
        for (i;i<args.length;i++) {
            rest_args.push(args[i]);
        };
        if (!accepts_args && rest_args.length != 0) { 
            runtime_exception();
        }
        if (!accepts_kwargs && !is_empty(dict)) { 
            runtime_exception();
        }
        if (accepts_args) { 
            input_args.push(rest_args);
        }
        if (accepts_kwargs) {
            input_args.push(dict);
        }
        return py_func.apply(this,input_args);
       
    }    
    return output_func;    

}
function get_param_names(func) {
    var funStr = func.toString();
    var output = funStr.slice(funStr.indexOf('(')+1, funStr.indexOf(')')).match(/([^\s,]+)/g);
    if (output == null) {
        return [];
    }
    else { 
        return output;
    }

}
function is_empty(ob){
   for(var i in ob){ return false;}
  return true;
}
exports.get_param_names = get_param_names;
exports.def = def;
exports.kwargs = kwargs;
exports.args = args;
py = {}
py.def = def;
py.kwargs = kwargs;
py.args = args;instancemethod = py.def ({}, function (fn) {
    the_fn = py.def (py.kwargs, py.args, {}, function (args, kwargs) {
        return fn ([this].concat(args), kwargs);
    });
    return the_fn;
});
py.instancemethod = instancemethod;
contains = py.def ({}, function (seq, item) {
    return seq.__contains__ ([item], {});
});
exports.instancemethod = instancemethod;
exports.contains = contains;

len = py.def ({}, function (seq) {
    var count, res, res;
    return seq.__len__ ([], {});
});
iter = py.def ({}, function (seq) {
    var count, res, res;
    return seq.__iter__ ([], {});
});
str = py.def ({}, function (seq) {
    var count, res, res;
    return seq.__str__ ([], {});
});
_tuple = function (args, kwargs) {
    this.__init__ = py.instancemethod ([py.def ({}, function (self, items) {
        var count, res, res;
        self._items = items;
        self._len = -1;
    })], {});
    this.__len__ = py.instancemethod ([py.def ({}, function (self) {
        var count, res, res;
        if (self._len == -1) {
            count = 0;
            for (var index in self._items) {
                            count += 1;;
                        };
                        ;
            self._len = count;
            return count;
        } else {
            return self._len;
        };
    })], {});
    this.__contains__ = py.instancemethod ([py.def ({}, function (self, item) {
        var count, res, res;
        for (var index in self._items) {
                          if (item === self._items[index]) {
                              return true;;
                          };
                      };
                      ;
        return false;
    })], {});
    this.__iter__ = py.instancemethod ([py.def ({}, function (self) {
        var count, res, res;
        return self._items;
    })], {});
    this.__str__ = py.instancemethod ([py.def ({}, function (self) {
        var count, res, res;
        res = "(";
        for (var index in self._items) {
                          res += '' + self._items[index] + ',';
                      };
                      ;
        res = res + ")";
        return res;
    })], {});
    this.__init__ (args, kwargs);
};
tuple = function (args, kwargs) {
    return new _tuple(args, kwargs);
};
exports.len = len;
exports.iter = iter;
exports.str = str;
exports.tuple = tuple;

