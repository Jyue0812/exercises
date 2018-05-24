from flask import Flask, render_template, render_template_string, g
from flask_script import Manager
from cookie import cookie
from sess import sess

app = Flask(__name__)
manage = Manager(app)
app.config['SECRET_KEY'] = '123456'
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.register_blueprint(cookie)
app.register_blueprint(sess)

@app.route('/')
def index():
    # return render_template('index.html')
    return render_template_string('<h1>hello string</h1>')

# @app.route('/inc/')
# def inc():
#     # return render_template('index.html')
#     return render_template('incl.html')

@app.route('/p/')
def extends():
    # return render_template('index.html')
    return render_template('parents.html')

@app.route('/c/')
def cextends():
    # return render_template('index.html')
    return render_template('children.html')

@app.route('/inc/')
def macro():
    # return render_template('index.html')
    return render_template('inc1.html',name="erhua")


@app.route('/var/')
def var():
    # return render_template('index.html')
    g.passwd = "12345"
    return render_template('index.html', hellou="xiaohei")


if __name__ == '__main__':
    manage.run()