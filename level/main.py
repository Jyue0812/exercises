__author__ = 'Steve Cassidy'

from bottle import Bottle, template, request, static_file, redirect
import interface
import users
import bottle_sqlite


app = Bottle()


@app.route('/')
def index(db):
    """show the home page"""
    return template('index', title='Welcome to Jobs', dbfile = app.plugins[2].dbfile)


@app.route('/about')
def about():
    """generate the about page"""
    return template('about', title="About", dbfile = app.plugins[2].dbfile)


@app.route('/positions/<id>')
def description(db, id):
    """show the selected position's detailed information"""
    return template('position_detail', title="Position Detail", dbfile = app.plugins[2].dbfile, id=id)


@app.post('/login')
def login(db):
    """user login"""

    # obtain the username and password from forms
    nick = request.forms.get('nick')
    password = request.forms.get('password')

    # login
    if users.check_login(db, nick, password):
        users.generate_session(db, nick)
        return redirect('/', 303)
    else:
        return template('login_failed', title="Login Error", dbfile = app.plugins[2].dbfile)

@app.post('/logout')
def logout(db):
    """user logout"""
    user_nick = users.session_user(db)
    users.delete_session(db, user_nick)
    return redirect('/', 303)


@app.post('/post')
def post(db):
    """post a new work position information"""
    user_name = users.session_user(db)

    # only the login user can post new position
    if user_name is not None:
        interface.position_add(db, user_name, request.forms.get('title'), request.forms.get('location'), request.forms.get('company'), request.forms.get('description') )
        return redirect('/', 302)
    else:
        return "Please login firstly."
#
# @app.route('/static/<filename>')
# def server_static(filename):
#     return static_file(filename, root='/static')

@app.route('/static/js/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/js')

@app.route('/static/css/<filename>')
def server_static(filename):
    return static_file(filename, root='./static/css')





if __name__ == '__main__':

    from bottle.ext import sqlite
    from database import DATABASE_NAME
    # install the database plugin
    app.install(sqlite.Plugin(dbfile=DATABASE_NAME))
    app.run(debug=True, port=8010)
