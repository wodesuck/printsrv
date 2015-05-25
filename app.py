#!/usr/bin/env python2
# encoding: utf-8

from flask import Flask, g, render_template, redirect, url_for
from flask.ext.login import LoginManager, current_user
from playhouse.flask_utils import FlaskDB
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
app.config.from_object('common.config')
database = FlaskDB(app)
login_manager = LoginManager()
login_manager.init_app(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
