from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = 'jjj'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 10
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def processMoney():
    if request.form['earn'] == 'casino':
        randEarn = random.randint(0,100) - 50
        session['gold'] = int(session['gold'] + randEarn)
    else:
        randEarn = random.randint(10,20)
        total = randEarn // int(request.form['earn'])
        session['gold'] = int(session['gold'] + total)
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)