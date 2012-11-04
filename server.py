from flask import Flask, request,jsonify
import ast 
from notebook import convert 
from functools import wraps
from flask import Flask,url_for,render_template
import json
import logging
app = Flask(__name__)
app.debug = True
from flask import make_response
from functools import update_wrapper

def nocache(f):
    def new_func(*args, **kwargs):
        resp = make_response(f(*args, **kwargs))
        resp.cache_control.no_cache = True
        return resp
    return update_wrapper(new_func, f)

@nocache
@app.route("/api", methods=['GET', 'POST'])
def hello():
    t = ast.parse(str(request.args['code']))
    output = str(convert(t))
    return jsonify(r=output)


#return str(request.args['callback'] + "({0})".format(output[:-2]))  
    
@app.route("/", methods=['GET', 'POST']) 
def test():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

