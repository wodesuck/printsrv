# encoding: utf-8

from flask import request, render_template, redirect, url_for, flash
from flask.ext.login import login_user, logout_user, login_required
from app import app, login_manager
from models import User
from common.config import SALT
from md5 import md5

login_manager.login_view = "login"
login_manager.login_message = u"登陆以访问该页面"
login_manager.login_message_category = u"请先登陆！"

@login_manager.user_loader
def load_user(userid):
    try:
        return User.get(id=userid)
    except User.DoesNotExist:
        return None

@app.route("/login", methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user = None
        password = md5(request.form['password'] + SALT).hexdigest()
        try:
            user = User.get(username=request.form['username'])
        except User.DoesNotExist:
            pass
        if user is None or user.password != password:
            flash(u"请检查用户名和密码", u"登陆失败！")
            return redirect(url_for("login"))
        login_user(user)
        return redirect(url_for("printsrv"))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))
