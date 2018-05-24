from flask_script import Manager
from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
manage = Manager(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    manage.run()