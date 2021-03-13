from modularapi.db import db

"""
Configure all your database tables
"""
class SampleDataBase(db.Model):
    __tablename__ = "SampleDataBase"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)