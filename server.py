from flask import Flask, request 
import ast 
from notebook import convert 
from functools import wraps
from flask import Flask,url_for,render_template
app = Flask(__name__)
app.debug = True


@app.route("/api", methods=['GET', 'POST'])
def hello():
    contents = request.args['code'];
    return "eval({0})".format(str(request.args['code']).strip());
    """ 
    t = ast.parse(str(request.args['code']))
    output = str(convert(t))
    return str(request.args['callback'] + "({0})".format(output[:-2]))  
    """
@app.route("/", methods=['GET', 'POST']) 
def test():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

