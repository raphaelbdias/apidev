from flask import Flask, request, jsonify
from flask import render_template, url_for, flash, request, redirect, Response
import sqlite3
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from forms import LoginForm
import os
import sys

if sys.version_info[0] >= 3:
    unicode = str

app = Flask(__name__)

con = sqlite3.connect('birth_death_china_famine.db',check_same_thread=False)
cur = con.cursor()

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}

con.row_factory = dict_factory

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager(app)
login_manager.login_view = "login"
class User(UserMixin):
    def __init__(self, id, email, password):
         self.id = unicode(id)
         self.email = email
         self.password = password
         self.authenticated = False
    def is_active(self):
         return self.is_active()
    def is_anonymous(self):
         return False
    def is_authenticated(self):
         return self.authenticated
    def is_active(self):
         return True
    def get_id(self):
         return self.id
@login_manager.user_loader
def load_user(user_id):
   logconn = sqlite3.connect('login.db')
   logcurs = logconn.cursor()
   logcurs.execute("SELECT * from login where user_id = (?)",[user_id])
   lu = logcurs.fetchone()
   if lu is None:
      return None
   else:
      return User(int(lu[0]), lu[1], lu[2])

@app.route("/login", methods=['GET','POST'])
def login():
  if current_user.is_authenticated:
     return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
     conn = sqlite3.connect('login.db')
     curs = conn.cursor()
     curs.execute("SELECT * FROM login where email = (?)", [form.email.data])
     user = list(curs.fetchone())
     Us = load_user(user[0])
     if form.email.data == Us.email and form.password.data == Us.password:
        login_user(Us, remember=form.remember.data)
        Umail = list({form.email.data})[0].split('@')[0]
        flash('Logged in successfully '+Umail)
        redirect(url_for('home'))
     else:
        flash('Login Unsuccessfull.')
  return render_template('login.html',title='Login', form=form)


@app.route('/home')
def home():
    
    return 'Hello'


@app.route('/get-year/<year>')
def get_year(year):
    data = []
    for row in con.execute(f"SELECT * FROM birth_death_china_famine WHERE year={year};"):
        data.append(row)
    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)
