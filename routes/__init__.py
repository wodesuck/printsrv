# encoding: utf-8

from flask import render_template, redirect, url_for
from flask.ext.login import current_user
from app import app

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    if current_user.is_authenticated():
        return redirect(url_for("printsrv"))
    return redirect(url_for('login'))

import auth
import printsrv
import history
