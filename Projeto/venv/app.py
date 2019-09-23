#coding: utf-8
from flask import Flask ,request , session, redirect , url_for
from datetime import timedelta

from mod_home.home import bp_home
from mod_login.login import bp_login
from mod_admin.admin import bp_admin

import os

app = Flask(__name__)

app.register_blueprint(bp_home)
app.register_blueprint(bp_login)
app.register_blueprint(bp_admin)
app.secret_key = os.urandom(12).hex()


@app.before_request
def before_request():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=30)

if __name__ == '__main__':
    app.run()