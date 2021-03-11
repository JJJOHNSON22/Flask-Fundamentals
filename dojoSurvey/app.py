from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template("index.html", phrase="New User")

@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print('*'*80)
    print(request.form)
    formFirstName = request.form['firstName']
    formLastName = request.form['lastName']
    formEmail = request.form['userEmail']
    formLangList = request.form.getlist('languages')
    formLang = ""
    for lang in formLangList:
        if lang == formLangList[-1]:
            formLang += (lang + "")
        else:
            formLang += (lang + ", ")
    formSpec = request.form['userSpec']
    formBio = request.form['userBio']

    return render_template("show.html",
    tempFirstName=formFirstName,
    tempLastName=formLastName,
    tempEmail=formEmail,
    tempLang=formLang,
    tempSpec=formSpec,
    tempBio=formBio)

if __name__=="__main__":
    app.run(debug=True)