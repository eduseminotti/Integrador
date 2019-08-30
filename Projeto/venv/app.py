#coding: utf-8
from flask import Flask

from mod_home.index import bp_index
from mod_admin.admin import bp_admin

app = Flask(__name__)

app.register_blueprint(bp_index)
app.register_blueprint(bp_admin)

if __name__ == '__main__':
    app.run()