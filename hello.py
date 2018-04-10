#!/usr/bin/env/python
# -*- encoding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    # return '<h1>Hello World</h1>'
    #user_agent = request.headers.get('User-Agent')
    #return '<p>Your browser is %s</p>' % user_agent
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
