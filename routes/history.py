# encoding: utf-8

from flask import render_template, abort
from flask.ext.login import login_required, current_user
from app import app
from models import History
from playhouse.flask_utils import object_list

@app.route("/history")
@login_required
def history_list():
    return object_list('history_list.html',
                       query=current_user.history,
                       context_variable='object_list',
                       check_bounds=False,
                       paginate_by=10)

@app.route("/history/<id>")
@login_required
def history(id):
    entry = None
    try:
        entry = History.get(id=id)
    except History.DoesNotExist:
        pass
    except ValueError:
        pass
    if entry is None or entry.user.id != current_user.id:
        abort(404)
    return render_template('history.html', entry=entry)
