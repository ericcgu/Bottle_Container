import bottle
from bottle import route, run

app = bottle.default_app()

@route('/')
def hello_world():
    return "Hello World!!"

@route('/login')
def login():
    return '<h1>Login</h1>'

run(host="0.0.0.0", port=8080, debug=True, reloader=True)