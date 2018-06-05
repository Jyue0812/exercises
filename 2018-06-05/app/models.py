from app.extension import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(12))
    recipes = db.relationship('Recipe', backref='users')


class Recipe(db.Model):
    __tablename__ = 'recipes'
    rid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    recipe = db.Column(db.Text)
    createdtime = db.Column(db.DateTime)


