from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = 'jjj'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    if 'winnerList' not in session:
        print('Creating List')
        session['winnerList'] = [{'userName': 'Joe', 'score': 5}]
    if 'randomNumber' in session:
        print('*'*80)
        print(session['winnerList'])
        if session['guestType'] == 'correct':
            print('You are correct')
        print(session['randomNumber'])
        print(session['guestType'])
    else:
        session['randomNumber'] = random.randint(1, 100)
        session['counter'] = 0
        print('*'*80)
        print('New number generated.')
        print(session['randomNumber'])
        session['guestType'] = 'newGuest'
        print(session['guestType'])
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guessCheck():
    session['userGuess'] = request.form['guess']
    session['counter'] = int(session['counter']) + 1
    print(session['userGuess'])
    print(session['counter'])

    if str(session['userGuess']) == '':
        return redirect('/')
    if str(session['userGuess']) != '' and int(session['userGuess']) == int(session['randomNumber']):
        session['guestType'] = 'correct'
        return redirect('/')
    elif int(session['userGuess']) < int(session['randomNumber']):
        session['guestType'] = 'tooLow'
    else:
        session['guestType'] = 'tooHigh'
    print(session['guestType'])
    if session['counter'] >= 5:
        session['guestType'] = 'gameOver'
    return redirect('/')

@app.route('/destroy', methods=['POST'])
def tryAgain():
    session.pop('randomNumber')
    return redirect('/')

@app.route('/save', methods=['POST'])
def addPlayer():
    session['guestType'] = 'winners'
    newWinner = {'userName': request.form['user'], 'score': session['counter']}
    session['winnerList'].append(newWinner)
    return redirect('/')

@app.route('/leaderboard', methods=['POST', 'GET'])
def winners():
    session['guestType'] = 'winners'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)