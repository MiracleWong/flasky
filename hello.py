#!/usr/bin/env/python
# -*- encoding: utf-8 -*-

from flask import Flask
from flask import request
from flask import make_response
from flask import render_template
from flask.ext.script import Manager, Server
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

app = Flask(__name__)
manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True))
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/')
def index():
    # return '<h1>Hello M iracle</h1>'
    # user_agent = request.headers.get('User-Agent')
    # return '<p>Your browser is %s</p>' % user_agent
    # response = make_response('<h1>This document carries a cookie!</h1>')
    # response.set_cookie('answer', '42')
    # return response
    print(datetime.utcnow())
    return render_template('index.html', current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_find(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
