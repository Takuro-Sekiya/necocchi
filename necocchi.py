from flask import Flask, render_template, request, redirect, session, url_for, flash, abort
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Mail, Message
import os
import secrets
import sqlite3
import smtplib
# from flask_mail import Mail, Message 


app = Flask(__name__)

app.secret_key = 'necocchi'

@app.route('/') 
def hello_world():
    return 'Hello, World!'

@app.route('/add')
def add_get():
    if 'user_id' in session:
        return render_template('add.html')
    else:
        return redirect('/login')

@app.route('/add', methods=["POST"])
def add_post():
    # name="task" インプットタグに打ち込まれた内容を取得
    if 'user_id'in session:
        user_id=session['user_id']
        py_task = request.form.get("task")
        time_limit = request.form.get("time")
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("INSERT INTO task VALUES(null, ?, ?, ?)",(py_task,time_limit,user_id))
        # DBの保存
        conn.commit()
        conn.close()
        return redirect('/list')

@app.route('/list')
def list():
    if 'user_id' in session:
        user_id = session['user_id']
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("SELECT name from users where id = ?",(user_id,))
        user_name = c.fetchone()[0]
        c.execute("SELECT id, task, time FROM task where user_id = ?", (user_id,))
        tasklist = []
        for row in c.fetchall():
            tasklist.append({"id":row[0], "task":row[1], "time":row[2]})
        c.close
        print(tasklist)
        return render_template('list.html', html_tasklist=tasklist, user_name = user_name)
    else:
        return redirect('/login')

@app.route("/edit/<int:id>")
def edit(id):
    if 'user_id' in session:
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("SELECT task FROM task WHERE id = ?", (id,))
        task = c.fetchone()
        conn.close
        if task is None:
            return "タスクがありません"
        else:
            py_item = {"id":id, "task":task[0]}
            return render_template("edit.html", task = py_item)
    else:
        return redirect("/login")

@app.route('/edit', methods=["POST"])
def post_edit():
    if 'user_id' in session : 
        item_id = request.form.get("task_id")
        item_id = int(item_id)
        # 入力フォームからとってくると文字列型になるのでInt型に整形
        task = request.form.get("task")
        time = request.form.get ("time")
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("UPDATE task SET task = ?, time = ? WHERE id = ?", (task, time, item_id))
        conn.commit()
        c.close
        return redirect('/list')
    else:
        return redirect('/login')

@app.route('/delete/<int:id>')
def delete(id):
    if 'user_id' in session:
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("DELETE FROM task WHERE id = ?", (id,))
        conn.commit()
        c.close
        return redirect('/list')
    else:
        return render_template("login.html")


@app.route('/regist/')
def regist_get():
    # print("HELLO")
    if 'user_id' in session:
        return render_template('list.html')
    else:
        return render_template('regist.html')

@app.route('/regist', methods=['POST'])
def regist_post():
    name = request.form.get("user_name")
    password = request.form.get("user_pass")
    email = request.form.get("user_address")
    conn = sqlite3.connect('necocchi.db')
    c = conn.cursor()
    c.execute("INSERT INTO users VALUES(null, ?, ?, ?)",(name, password, email))
    conn.commit()
    c.close
    return redirect('/login')

@app.route('/login', methods =["GET"])
def login_get():
    if 'user_id' in session:
        return redirect("/list")
    else:
        return render_template("login.html")

@app.route('/login', methods=["POST"])
def login_post():

    name = request.form.get("user_name")
    password = request.form.get("user_pass")
    conn = sqlite3.connect('necocchi.db')
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE name = ? AND password = ?", (name, password))
    user_id = c.fetchone()
    conn.close()
    if user_id is None:
        return render_template('login.html')
    else:
        session['user_id'] = user_id[0]
        return redirect('/list')

@app.route("/logout")
def logout():
    session.pop('user_id', None)
    return redirect('/login')

@app.errorhandler(404)
def notfound(error):
    return "404ページです。URL違いです"

# necocchi hearing page
@app.route('/hearing')
def hearing():
    if 'user_id' in session:
        user_id = session['user_id']
        conn = sqlite3.connect('necocchi.db')
        c = conn.cursor()
        c.execute("SELECT name from users where id = ?",(user_id,))
        user_name = c.fetchone()[0]
        c.execute("SELECT id, task, time FROM task where user_id = ?", (user_id,))
        hearinglist = []
        for row in c.fetchall():
            hearinglist.append({"id":row[0], "task":row[1], "time":row[2]})
        c.close
        print(hearinglist)
        return render_template('hearing.html', html_hearinglist=hearinglist, user_name = user_name)
    else:
        return redirect('/login')

def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')
        
@staticmethod  
def verify_reset_token(token):
    s = Serializer(app.config['SECRET_KEY'])
    try:
        user_id = s.loads(token)['user_id']
    except:
        return None
        return User.query.get(user_id)

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_request():
    if user_email_address.is_authenticated:
        return redirect(url_for('home'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent with instructions to reset your password', 'info')
        return redirect(url_for('login'))
    return render_template('reset_request.html', title='Reset Password', form=form)

@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    if user_email_address.is_authenticated:
        return redirect(url_for('home'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_password
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('reset_token.html', title='Reset Password', form=form)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587  
app.config['MAIL_USE_TLS'] = True  
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  
mail = Mail(app)

if __name__ == '__main__':
    app.run(debug=True)
