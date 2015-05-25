# encoding: utf-8

from flask import request, render_template, redirect, url_for, flash
from flask.ext.login import login_required, current_user
from app import app
from models import History
from datetime import datetime, timedelta
from sh import enscript

def check_print(content):
    if len(content) < 50:
        return False, u"打印代码不能少于50B"
    if len(content) > 10240:
        return False, u"打印代码不能超过10K"
    try:
        last = current_user.history.get()
        if datetime.now() - last.timestamp < timedelta(seconds=30):
            return False, "提交打印速度过快"
    except History.DoesNotExist:
        pass
    return True, None

@app.route("/print", methods = ['GET', 'POST'])
@login_required
def printsrv():
    if request.method == 'GET':
        return render_template('print.html')
    else:
        content = request.form['content']
        ret, err = check_print(content)
        if ret:
            record = History.create(user=current_user.id, content=content)
            title = str(record.id) + ' - ' + current_user.username
            enscript(title=title, _in=content)
            flash(u"打印请求已成功提交", "success")
        else:
            flash(err, "error")
        return redirect(url_for("printsrv"))
