import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, username, password):
        #self.id = _id
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()

#        query = "SELECT * From users WHERE username = ?"
#        result = cursor.execute(query, (username,))
#        row = result.fetchone()
#        if row:
#            user = cls(*row) # == row[0],row[1],row[2]
#        else:
#            user = None

#        connection.close()
#        return user


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id = id).first()
#        connection = sqlite3.connect('data.db')
#        cursor = connection.cursor()

#        query = "SELECT * From users WHERE id = ?"
#        result = cursor.execute(query, (_id,))
#        row = result.fetchone()
#        if row:
#            user = cls(*row) # == row[0],row[1],row[2]
#        else:
#            user = None

#        connection.close()
#        return user
