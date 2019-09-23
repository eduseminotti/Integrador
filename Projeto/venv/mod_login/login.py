#coding: utf-8
from flask import Blueprint, render_template, request, session, redirect , url_for
from functools import wraps

bp_login = Blueprint('login', __name__, url_prefix='/login', template_folder='templates')

@bp_login.route("/")
def index():
    return render_template('login.html')

    
@bp_login.route("/btnlogin",methods=['POST']) 
def btnlogin():
     user =  request.form.get('user')
     password = request.form.get('pass')

     #Usuario correto
     if user == "user1" and password == "123":
          session.clear()
          session['user'] = user
          return redirect(url_for('admin.index'))
     #user errado
     else:     
          return redirect(url_for('login.index', userIncorrect=1))

@bp_login.route("/btnlogout",methods=['GET','POST']) 
def btnlogout():
     session.pop('user',None)
     session.clear()
     return redirect(url_for('home.index'))

def validaSessao(f):
     @wraps(f)
     def decorated_function(*args, **kwargs):
          if 'user' not in session:
               return redirect(url_for('login.index', falhaSessao=1))
          else:
               return f(*args, **kwargs)
     return decorated_function
