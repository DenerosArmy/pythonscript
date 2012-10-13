var Kwargs = {};
var args = {}; 

function compile_exception() { 
    throw "Compile Time Error";
};
function runtime_exception() { 
    throw "Run Time Error";
}
function def() { 
    if (arguments.length < 1) { 
        exception();
    };
    var py_func = arguments[arguments.length - 1];
    var py_defaults = arguments[arguments.length - 2];
    if (typeof py_func != "function") { 
        compile_exception();
    };
    if (typeof py_defaults != "object") { 
        compile_exception();
    };
    var accepts_args = (arguments[0] === Kwargs) || (arguments[1] === Kwargs) ;
    var accepts_kwargs = (arguments[1] === args) || (arguments[0] === args);
    var py_func_args = get_param_names(py_func);
    var py_num_required_args = 0;

    for (i in py_func_args) { 
        if (i in py_defaults) { 
            break;
        };
        py_num_required_args++;
    };
    if (accept_args) { 
        py_func_args.pop();
    };
    if (accept_kwargs) { 
        py_func_args.pop();
    };
    function output_func(args,dict) { 
       if (args.length < py_num_required_args) { 
           runtime_exception();
        };
       var input_args = [];
       for (var i =0;i<py_func_args.length;i++) {
           if (i < args.length) { 
               input_args[i] = args[i];
            }
           if (py_func_args[i] in dict) { 
               input_args[i] = dict[py_func_args[i]];
               delete dict[py_func_args[i]];
           }
           else if (py_func_args[i] in py_defaults) { 
               input_args[i] = py_defaults[py_func_args[i]];
           }
           else { 
               runtime_exception();
                }
            
           delete args[i];  
        } 
        if (!accept_args && args.length != 0) { 
            runtime_exception();
        }
        if (!accept_kwargs && !is_empty(dict)) { 
            runtime_exception();
        }
        if (accept_args) { 
            input_args.push(args);
        }
        if (accept_kwargs) {
            input_args.push(dict);
        }
        return output_func.apply(input_args);
       
    }    
    return output_func;    

}
function get_param_names(func) {
    var funStr = func.toString();
    return funStr.slice(funStr.indexOf('(')+1, funStr.indexOf(')')).match(/([^\s,]+)/g);
}
function is_empty(ob){
   for(var i in ob){ return false;}
  return true;
}
exports.get_param_names = get_param_names;
exports.def = def;

