from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, session 
import random

app = Flask(__name__)
app.secret_key = 'jjj'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session['earnGold'] = [
        {'jobName':'Farm', 'payRate':'1', 'earnings':'10-20'},
        {'jobName':'Cave', 'payRate':'2', 'earnings':'5-10'},
        {'jobName':'House', 'payRate':'4', 'earnings':'2-5'},
        {'jobName':'Casino', 'payRate':'casino', 'earnings':'or lose 0-50'},
        ]
    if 'gold' not in session:
        session['gold'] = 10
        session['messages'] = []
        session['counter'] = 0
    else:
        if int(session['gold']) >= 50:
            print('*'*80)
            print('You Won!')
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def processMoney():
    messageList = session['messages']
    name = request.form['job']
    if request.form['earn'] == 'casino':
        total = random.randint(0,100) - 50
        session['gold'] = int(session['gold'] + total)
        if total < 0:
            messageList.insert(0, f'<li style="list-style: none; text-align:left; color: red;"> You lost ${total} from the {name}. </li>')
        else:
            messageList.insert(0, f'<li style="list-style: none; text-align:left; color: green;"> You won ${total} from the {name}! </li>')
    else:
        randEarn = random.randint(10,20)
        total = randEarn // int(request.form['earn'])
        session['gold'] = int(session['gold'] + total)
        messageList.insert(0, f'<li style="list-style: none; text-align:left; color: green;"> You earned ${total} from {name}. </li>')
    session['messages'] = messageList
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)