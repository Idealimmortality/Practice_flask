#!/usr/bin/python3
from hello_app import db
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nikename = db.Column(db.String(20),index=True,unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '{}'.format(self.nikename)


