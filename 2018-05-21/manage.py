from flask import Flask, request, make_response, redirect
app = Flask('__name?__')

@app.route('/')
def index():
    return "hahahhh"

@app.route('/test/')
def test():
    return "hahahhhtest"

@app.route('/welcome/<name>/')
def welcome(name):
    return "hahahhh%s" % name


@app.route('/user/<int:uid>/')
def user(uid):
    return "%d您好" %uid


@app.route('/path/<path:p>/')
def path(p):
    return "%s您好" %p

@app.route('/request/')
def req():
    # return request.url
    # return request.host_url
    return request.headers['User-Agent']
    # return request.values.get('passwd')
    # return request.remote_addr
    # return request.method
    # return request.base_url

@app.route('/response/')
def response():
    # return '200 ol', 404
    resp = make_response('hgahhaah', 404)
    resp.headers['hello']="world"
    return resp

@app.route('/old/')
def old():
    return redirect('/new/')

@app.route('/new/')
def new():
    return 'new'

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0", port=5000, threaded=True)