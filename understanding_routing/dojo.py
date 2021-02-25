import sys
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def hello_dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/repeat/<num>/<word>')
def repeat_word(num,word):
    num = int(num)
    x = 0
    num_list = '' 
    while (x < num):
        x += 1
        num_list+='<p>'+word+'</p>'
    return num_list

@app.errorhandler(404)
def page_not_found(error):
    return 'Sorry! No response. Try again.', 777

if __name__=="__main__":
    app.run(debug=True)
