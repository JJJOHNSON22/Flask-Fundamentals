from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = 'jjj'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    if 'randomNumber' in session:
        print('*'*80)
        if session['guestType'] == 'correct':
            print('You are correct')
        else:
            session['guestType'] = 'returnGuest'
        print(session['randomNumber'])
        print(session['guestType'])
    else:
        session['randomNumber'] = random.randint(1, 100)
        print('*'*80)
        print('New number generated.')
        print(session['randomNumber'])
        session['guestType'] = 'newGuest'
        print(session['guestType'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guessCheck():
    session['userGuess'] = request.form['guess']
    print(session['userGuess'])
    if session['userGuess'] != '' and int(session['userGuess']) == int(session['randomNumber']):
        session['guestType'] = 'correct'
    else:
        session['guestType'] = 'returnGuest'
    print(session['guestType'])
    return redirect('/')

@app.route('/destroy', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)