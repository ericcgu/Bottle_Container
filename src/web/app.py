import bottle
from bottle import Bottle, route, run

app = Bottle()

#Basics
@route('/')
def hello_world():
    return "Hello World!!"

@route('/login')
def login():
    return '<h1>Login</h1>'

#Parameter
@route('/article/<id>')
def article(id):
    return 'Article: ' + id    

####################################
# Step 1

# Make a route that accepts two numbers in the path. (ie /add/5/6)
# In the view function, return a string that contains the result of adding the numbers.

@route('/add/<num1:int>/<num2:int>')
def add(num1, num2):
    return str(num1+num2)

####################################

run(host="0.0.0.0", port=8080, debug=True, reloader=True)