from flask import Flask, render_template
app = Flask(__name__)

#binding
@app.route('/')  #homepage
def index():
    return render_template("index.html")

@app.route('/c4e12')
def c4e12():
    return "nen"


@app.route('/thangbencanh')
def thangbencanh():
    return "lam gi co ai"

@app.route('/<name>/<age>')
def say_hi(name, age):
    return "Hi " + name + ", " + age

@app.route('/tinh_tong/<int:no1>/<int:no2>')
def tinh_tong(no1,no2):
    tong = no1 + no2
    return str(tong)

@app.route('/h1')
def tag_h1():
    return "<h1> Khong biet viet gi  </h1><p>Hom nay GAM thua </p>"




if __name__ == '__main__':
  app.run(debug=True)
