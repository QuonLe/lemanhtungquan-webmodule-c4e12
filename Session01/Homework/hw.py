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
        ket_qua = ("Severely underweight")
    elif 16 <= BMI <18.5:
        ket_qua = ("Underweight")
    elif 18.5 <= BMI < 25:
        ket_qua = ("Normal")
    elif 25 <= BMI <30:
        ket_qua = ("Overweight")
    else:
        ket_qua = ("Obese")
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
