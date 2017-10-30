from flask import Flask, render_template, request, redirect
import mlab
from mongoengine import * #Document,StringField,FloatField
# from faker import Faker
app = Flask(__name__)

mlab.connect()

class Girl(Document):
    name = StringField()
    image = StringField()
    description = StringField()
    rating = FloatField()


@app.route('/')
def index():
    girl_list = Girl.objects()
    return render_template('girls.html', girls = girl_list)

@app.route('/list')
def list_demo():
    n_list = ['quan','long','huy','tung']
    return render_template('girls_list.html',names = n_list )

@app.route('/dict')
def dict_demo():
    d  = {
    'name' : 'Nay va xua',
    'image' : 'https://goo.gl/TzpGn7'
    }
    return render_template ('girls_dict.html', girl = d)

@app.route('/css_demo')
def css_demo():
    return render_template('css_demo.html')

@app.route('/admin_demo')
def admin():
    girl_list = Girl.objects()
    return render_template('admin.html', girls = girl_list)

@app.route('/add_girl', methods = ['GET','POST'])
def add_girl():
    if request.method == "GET":
        return render_template('add_girl.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        image = form['image']
        description = form['description']
        girl = Girl(name=name, image=image, description=description, rating = 4.1)
        girl.save()
        return "Added"

@app.route('/test')
def test():
    return render_template('/test.html')

# #Mongo
# #1 Find record base on id
# # Mongoengine lazy loading
# girl = Girl.objects().with_id("59e33402aa27240008a46004")
#
# #2 Delete
# if girl is None:
#     print("Not found")
# else:
#     girl.delete()



@app.route('/delete_girl/<girl_id>')
def delete_girl(girl_id):
    girl = Girl.objects().with_id(girl_id)
    if girl is None:
        print("Not found")
    else:
        girl.delete()
        return redirect('/admin_demo')

@app.route('/update_girl/<girl_id>', methods = ['GET','POST'])
def update_girl(girl_id):
    girl = Girl.objects().with_id(girl_id)
    if request.method == "GET":
        return render_template('/update_girl.html' , girl = girl)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        image = form['image']
        description = form['description']
        girl.update(set__name = name, set__description = description, set__image =  image)
        return redirect ('/admin_demo')






if __name__ == '__main__':
  app.run(debug=True)
