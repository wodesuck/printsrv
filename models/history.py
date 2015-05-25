from app import database
from user import User
from peewee import *
from datetime import datetime

class History(database.Model):
    user = ForeignKeyField(User, related_name='history')
    content = TextField()
    timestamp = DateTimeField(default=datetime.now)

    class Meta:
        order_by = ('-timestamp',)
