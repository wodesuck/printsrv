from app import database
from peewee import *
from flask.ext.login import UserMixin

class User(database.Model, UserMixin):
    username = CharField(unique=True)
    password = CharField()
