from typing import Counter
import base64
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = 'jjj'
app.config['SESSION_TYPE'] = 'filesystem'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    session['counter'] = 1
    print('*'*80)
    print(session['counter'])
    if 'count' in session and 'countCustom' in session:
        if int(session['countCustom']) > 1:
            session['count'] = int(session['count']) + int(session['countCustom'])
            print(f"Count is {session['count']}")
        else:
            session['count'] = int(session['count']) + int(session['counter'])
    else:
        print("First time visit")
        session['count'] = 1
        session['countCustom'] = 0
        session['refreshCount'] = 0
    session['refreshCount'] = int(session['refreshCount']) + int(session['counter'])
    return render_template("index.html", phrase="Count", tempCount=session['count'])

@app.route('/destroy', methods=['POST'])
def destroy_session():
    session.clear()
    return redirect('/')

@app.route('/add_two', methods=['POST'])
def addTwo():
    if int(session['countCustom']) > 1:
        session['count'] = int(session['count']) + int(session['countCustom'])
        print(f"Count is {session['count']}")
    else:
        session['count'] = int(session['count']) + int(session['counter'])
        print(f"Count is {session['count']}")
    return redirect('/')

@app.route('/custom', methods=['POST'])
def customCounter():
    session['countCustom'] = request.form['customCount']
    print(session['countCustom'])
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)