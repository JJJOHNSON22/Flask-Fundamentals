from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = 'jjj'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session['gold'] = 100
    return render_template("index.html")

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)