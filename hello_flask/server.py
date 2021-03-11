from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    print('in the hello function')
    return render_template("index.html", phrase="hello", times=5)	# notice the 2 new named arguments!

@app.route("/<name>/<times>")
def hello_person(name, times):
    print('*'*80)
    print('in hello_person function')
    print(name)
    return render_template('name.html',
    some_name=name,
    num_times=int(times))

if __name__=="__main__":
    app.run(debug=True)