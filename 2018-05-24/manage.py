from flask import Flask, render_template,request
from flask_script import Manager
from flask_moment import Moment
from datetime import datetime, timedelta
from flask_mail import Mail, Message

mail = Mail(app)
import os
from flask_uploads import UploadSet, IMAGES, configure_uploads,patch_request_class
app = Flask(__name__)

# ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd()
photos = UploadSet('photos', IMAGES)

configure_uploads(app, photos)
patch_request_class(app, size=None)

base_url = os.path.abspath(os.path.dirname(__file__))
# app.config['MAX_CONTENT_LENGTH'] = 1024*1024*8
# app.config['UPLOAD_FOLDER'] = os.path.join(base_url, 'upload')

# email

app.config['MAIL_SERVER'] = 'smtp.xxxx.com'
app.config['MAIL_USERNAME'] = '1HWOQH'
app.config['MAIL_PASSWORD'] = '123456'

manage = Manager(app)
moment = Moment(app)
@app.route('/')
def index():
    return 'flask-moment'


@app.route('/mail/')
def mail():
    msg = Message('haha',
                  recipients="yueyuezhu@msn.com",
                  sender=app.config['MAIL_USERNAME'])
    mail.send(msg)
    return '邮件已发送'

@app.route('/upload/', methods=['GET','POST'])
def upload():
    if request.method=="POST" and 'photo' in request.files:
        photos.save(request.files['photo'])

    return render_template('upload.html')

@app.route('/moment/')
def moment():
    current_time = datetime.utcnow()
    return render_template('mom.html', current_time=current_time)

if __name__ == '__main__':
    manage.run()
