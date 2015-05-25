#!/usr/bin/env python2

from app import database
from models import User, History

database.connect_db()
database.database.create_tables([User, History])
database.database.execute_sql('alter table history auto_increment=1001')
