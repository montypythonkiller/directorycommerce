from app import app
from flask import render_template
from queryDB import getx
import random
@app.route('/')
@app.route('/index')


def index():
    ret_category = ''
    items = getx(ret_category)
    return render_template("index.html",
                           title='Home',
                           items=items) 
                           
@app.route('/men')
def men():
    ret_category = 'men?lim'
    items = getx(ret_category)
    return render_template("men.html",
                           title="Men's Clothing",
                           items=items
                           )                             
@app.route('/women')
def women():
    ret_category = 'women?l'
    items = getx(ret_category)
    randoNum = random.randint(2,2500)
    rando = "?v=" + str(randoNum)
    
    return render_template("men.html",
                           title="Men's Clothing",
                           items=items,rando=rando
                           )
                           
@app.route('/child')
def child():
    ret_category = 'kids'
    items = getx(ret_category)
    return render_template("child.html",
                           title="Kid's Clothing",
                           items=items
                           )  

@app.route('/electronics')
def electronics():
    ret_category = 'electronics'
    items = getx(ret_category)
    return render_template("electronics.html",
                           title="Electronics",
                           items=items
                           )                            