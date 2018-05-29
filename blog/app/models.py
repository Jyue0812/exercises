from extensions import db
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from extensions import login_manager

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))
    email = db.Column(db.String(40))
    confirmed = db.Column(db.BOOLEAN, default=False)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm': self.id})

    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except:
            return '激活失败'
        if data.get('confirm') != self.id:
            return '激活失败'
        self.confirmed = True
        db.session.add(self)
        return '激活成功'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

