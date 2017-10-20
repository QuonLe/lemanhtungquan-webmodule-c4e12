from flask import Flask, render_template
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

# f = Faker()
#
# for _ in range(20):
#     g = Girl(name = f.name(),
#     image ="https://source.unsplash.com/500x300/?sexy",
#     description = f.text(),
#     rating = 4.1)
#     g.save()

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

if __name__ == '__main__':
  app.run(debug=True)
