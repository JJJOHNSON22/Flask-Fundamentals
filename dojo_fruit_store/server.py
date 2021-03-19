from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print("*"*80)
    print(request.form)
    formStrawberryCount = int(request.form['strawberry'])
    formRaspberryCount = int(request.form['raspberry'])
    formAppleCount = int(request.form['apple'])
    formFirstName = request.form['first_name']
    formLastName = request.form['last_name']
    formStudentID = request.form['student_id']
    formFruitCount = formStrawberryCount + formRaspberryCount + formAppleCount
    print(f"Charging {formFirstName} {formLastName} for {formFruitCount} fruits.")
    return render_template("checkout.html",
    tempFruitCount=formFruitCount,
    tempStrawberryCount=formStrawberryCount,
    tempRaspberryCount=formRaspberryCount,
    tempAppleCount=formAppleCount,
    tempFirstName=formFirstName,
    tempLastName=formLastName,
    tempStudentID=formStudentID)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    