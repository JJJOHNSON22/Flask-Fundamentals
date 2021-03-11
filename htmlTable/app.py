from flask_bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    userList = [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

    return render_template("index.html", phrase="User List", users=userList, num=0)

if __name__=="__main__":
    app.run(debug=True)
