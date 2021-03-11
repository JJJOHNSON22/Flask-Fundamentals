import sys
import random
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    print('8 rows 8 columns')
    return render_template("index.html", phrase="Home", rows=8, columns=8)

@app.route("/<x>")
def xRows(x):
    print(f'{x} rows')
    return render_template('index.html', phrase=f'{x} Rows', rows=int(x), columns=8)

@app.route("/<x>/<y>")
def xyBoard(x, y):
    print(f'{x} rows {y} columns')
    return render_template('index.html', phrase=f'{x} Rows by {y} Columns', rows=int(x), columns=int(y))

@app.route("/<x>/<y>/<color1>/<color2>")
def colorChoice(x, y, color1, color2):
    print(f'{x} rows {y} columns - {color1} & {color2}')
    return render_template('index.html', phrase=f'{x} Rows by {y} Columns', key='colorSelect', rows=int(x), columns=int(y), color1=color1, color2=color2)


if __name__=="__main__":
    app.run(debug=True)