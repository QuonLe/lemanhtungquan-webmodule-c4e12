from flask import Flask, render_template
from flask import Flask,redirect
app = Flask(__name__)


@app.route('/')
def index():
    return "Homework"

@app.route('/school')
def techkids():
    return redirect("http://www.techkids.vn", code=302)

@app.route('/bmi/<int:weight>/<float:height>')
def ketqua(weight,height):
    BMI =  weight / ( height * height )
    if BMI < 16:
        print("Severely underweight")
    elif 16 <= BMI <18.5:
        print("Underweight")
    elif 18.5 <= BMI < 25:
        print("Normal")
    elif 25 <= BMI <30:
        print("Overweight")
    else:
        print("Obese")
    return ketqua

@app.route('/praticalex1')
def ex1():
    return render_template("praticalex1.html")

@app.route('/praticalex2')
def ex2():
    return render_template("praticalex2.html")

@app.route('/study')
def study():
    return render_template("study.html")

if __name__ == '__main__':
  app.run(debug=True)
