#!/usr/bin/env python2

from app import database
from models import User
from common.config import SALT
from md5 import md5
import csv
import sys

if len(sys.argv) != 2:
    print 'importuser.py [FILE]'
    exit(1)

csvfile = sys.argv[1]
database.connect_db()
for username, password in csv.reader(open(csvfile)):
    password = md5(password + SALT).hexdigest()
    User.create(username=username, password=password)
