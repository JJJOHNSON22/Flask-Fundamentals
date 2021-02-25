import sys
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html", phrase="Hello!",)

@app.route('/play')
def play():
    return render_template("index.html", phrase="Welcome!", times=3)

@app.route('/play/<num>')
def play_times(num):
    num = int(num)
    return render_template("index.html", phrase="Welcome!", times=num)

@app.route('/play/<num>/<color>')
def play_times_color(num,color):
    num = int(num)
    return render_template("index.html", phrase="Welcome!", times=num, color=color)    

if __name__=="__main__":
    app.run(debug=True)


