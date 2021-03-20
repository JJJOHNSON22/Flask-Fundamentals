from typing import Counter
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, session 

app = Flask(__name__)
app.secret_key = 'jjj'
app.config['SESSION_TYPE'] = 'filesystem'
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    if 'count' in session:
        session['count'] = int(session['count']) + 1
        print(f"Count is {session['count']}")
    else:
        print("First time visit")
        session['count'] = 1
    return render_template("index.html", phrase="Count", tempCount=session['count'])

if __name__=="__main__":
    app.run(debug=True)