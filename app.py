from flask import Flask
from flask import request
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"
@app.route("/hello1")
def hello_world1():
    return "Hello world1"

@app.route("/add")
def test():
    sum=4+5
    return "addition result :{}".format(sum)

@app.route("/input_url")
def request_input():
    data=request.args.get('x')
    return "This is my url input from url {}".format(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0")