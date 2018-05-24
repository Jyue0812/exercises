from flask import Flask, make_response, Blueprint,request

cookie = Blueprint('cookie', __name__)

@cookie.route('/get/')
def get():
    return request.cookies.get('name')

@cookie.route('/set/')
def set():
    resp = make_response('cookie set')
    resp.set_cookie('name','hahah', max_age= 3)
    return resp

@cookie.route('/del/')
def dele():
    resp = make_response('cookie del')
    resp.delete_cookie('name')
    return resp

