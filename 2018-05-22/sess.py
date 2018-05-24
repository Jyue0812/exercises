from flask import Flask, make_response, Blueprint,request, session

sess = Blueprint('sess', __name__)

@sess.route('/sget/')
def get():
    return session.get('uname')


@sess.route('/sset/')
def set():
    session['uname'] = "dhaoiwdha"
    return "session set"